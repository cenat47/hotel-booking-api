from datetime import date
from sqlalchemy import text
from app.DAO.base import BaseDAO
from app.hotels.rooms.models import Rooms
from app.database import async_session_maker

class RoomDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_rooms_by_hotel(
        cls, hotel_id: int, date_from: date, date_to: date
    ):
        async with async_session_maker() as session:
            query = text("""
                SELECT 
                    r.id,
                    r.hotel_id,
                    r.name,
                    r.description,
                    r.services,
                    r.price,
                    r.quantity,
                    r.image_id,
                    (r.price * (DATE(:date_to) - DATE(:date_from))) AS total_cost,
                    (r.quantity - COALESCE(booked_rooms.booked_count, 0)) AS rooms_left
                FROM 
                    public.rooms r
                LEFT JOIN (
                    SELECT 
                        room_id,
                        COUNT(*) AS booked_count
                    FROM 
                        public.bookings
                    WHERE 
                        (DATE(date_from) <= DATE(:date_to) AND DATE(date_to) >= DATE(:date_from))
                    GROUP BY 
                        room_id
                ) AS booked_rooms ON r.id = booked_rooms.room_id
                WHERE 
                    r.hotel_id = :hotel_id
            """).bindparams(
                date_from=date_from,
                date_to=date_to,
                hotel_id=hotel_id
            )

            result = await session.execute(query)
            return result.mappings().all()