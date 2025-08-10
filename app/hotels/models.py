from sqlalchemy import Column, Integer, String, JSON
from app.database import Base 
from sqlalchemy.orm import relationship

class Hotels(Base):
    __tablename__ = "Hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    location = Column(String,nullable=False)
    services = Column(JSON,)
    room_quantity = Column(Integer,nullable=False)
    image_id = Column(Integer)

    rooms = relationship("Rooms", back_populates="hotel")

    def __str__(self):
        return f"Отель {self.name} {self.location[:30]}"
