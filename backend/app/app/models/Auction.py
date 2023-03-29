import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Boolean, Date
from app.app.models.Bid import Bid


class Auction(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_bid = Column(Date, nullable=False)
    last_bid = Column(Bid, nullable=False)
    category = Column(String, nullable=False)
    bid_history = Column(Bid, uselist=True)

