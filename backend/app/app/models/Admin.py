import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from app.app.models.Notification import Notification

class Admin(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    blocking = Column(Boolean, nullable=False)
    notification = Column(Notification, ForeignKey("notification.id"))
    ownership_of_object = Column(String, nullable=False)
    transfer_of_amount = Column(Integer, nullable=False)
    track_of_payment = Column(Boolean, nullable=False)
