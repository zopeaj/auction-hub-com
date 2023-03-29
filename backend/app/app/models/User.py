import os
import sys
from dotenv import load_dotenv

from app.app.db.base_class import Base
from sqlalchemy import String, Column, Integer, Date, Boolean
from uuid import uuid4

class User(Base):
    id = Column(Integer, primary_key=True, default=uuid4)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)

