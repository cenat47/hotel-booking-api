from datetime import date
from sqlalchemy import text
from app.DAO.base import BaseDAO
from app.hotels.models import Hotels
from app.database import async_session_maker

class HotelDAO(BaseDAO):
    model = Hotels
    
    @classmethod
    async def find_hotels_with_free_rooms(
        cls, location: str, date_from: date, date_to: date
    ):
        async with async_session_maker() as session:
            query = text("""
                SELECT 
                    h.id,
                    h.name,
                    h.location,
                    h.services::text AS services,
                    h.room_quantity,
                    h.image_id,
                    SUM(r.quantity) - COALESCE(SUM(booked.booked_count), 0) AS rooms_left
                FROM "Hotels" h
                JOIN "rooms" r ON r.hotel_id = h.id
                LEFT JOIN (
                    SELECT 
                        room_id,
                        COUNT(*) AS booked_count
                    FROM "bookings"
                    WHERE 
                        NOT (date_to <= :date_from OR date_from >= :date_to)
                    GROUP BY room_id
                ) AS booked ON r.id = booked.room_id
                WHERE h.location ILIKE :loc_prefix
                GROUP BY h.id, h.name, h.location, h.services::text, h.room_quantity, h.image_id
                HAVING SUM(r.quantity) - COALESCE(SUM(booked.booked_count), 0) > 0
            """).bindparams(
                date_from=date_from,
                date_to=date_to,
                loc_prefix=f"%{location}%",
            )

            result = await session.execute(query)
            return result.mappings().all()