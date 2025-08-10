from datetime import date
from fastapi import APIRouter, Depends, Request
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.exceptions import CantDeleteBookings, RoomCannotBeBooked
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users
from pydantic import  parse_obj_as

router = APIRouter(prefix="/bookings", tags=["Бронирование"])

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user))-> list[SBooking] :
    return await BookingDAO.find_all(user_id=user.id)

@router.post("")
async def add_booking(room_id: int, date_from: date, date_to:date, user: Users = Depends(get_current_user)):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked()
    booking_schema = SBooking.from_orm(booking)
    send_booking_confirmation_email.delay(booking_schema.dict(), user.email)
    return booking
    
@router.delete("/{booking_id}")
async def delete_booking(booking_id: int, user: Users = Depends(get_current_user)):
    bookings = await BookingDAO.find_one_or_none(id = booking_id)
    if not bookings or bookings.user_id != user.id: 
        raise CantDeleteBookings
    await BookingDAO.delete(booking_id)