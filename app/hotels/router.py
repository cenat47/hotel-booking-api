import asyncio
from datetime import date

from fastapi import APIRouter, Depends
from app.hotels.rooms.dao import RoomDAO
from app.hotels.dao import HotelDAO
from fastapi_cache.decorator import cache

router = APIRouter(prefix="/hotels", tags=["Отели"])

@router.get("/{location_user}")
async def get_hotels(location_user: str, date_from: date, date_to:date):
    return await HotelDAO.find_hotels_with_free_rooms(location_user, date_from, date_to)

@router.get("/{id}/rooms")
async def get_rooms(id: int, date_from: date, date_to:date):
    return await RoomDAO.find_rooms_by_hotel(id, date_from, date_to)
