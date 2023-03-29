import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Date
from app.app.models.Bid import Bid


class Item(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    currentBid = Column(Bid, nullable=False)
    bidIncrement = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    photo = Column(String, nullable=False)


