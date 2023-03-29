import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Date, Integer, Boolean, ForeignKey


class Notification(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    userId = Column(User, ForeignKey("user.id"))
    message = Column(String, nullable=False)
    date = Column(Date)
