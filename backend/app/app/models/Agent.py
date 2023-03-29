import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from app.app.models.User import User
from app.app.models.Auction import Auction
from app.app.models.Bid import Bid


class Agent(Base):
  id = Column(Integer, primary_key=True, nullable=False)
  userId = Column(User, ForeignKey("user.id"))
  valuation = Column(Integer, nullable=False)
  auctionId = Column(Auction, ForeignKey("auction.id"), nullable=False)
  bid = Column(Bid, nullable=False)

