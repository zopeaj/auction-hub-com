import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Date, Boolean

class Bidder(Base):
    id = Column(Integer, nullable=False)
    maxBidAmount = Column(Integer, nullable=False)
