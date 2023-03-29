import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Boolean, Date
from app.app.models.Bid import Bid


class Bid(Base):
    current_bid = Column(Bid, nullable=False)
    maximum_bid = Column(Integer, nullable=False)

    def sort_bidding_amount(self):
        pass


