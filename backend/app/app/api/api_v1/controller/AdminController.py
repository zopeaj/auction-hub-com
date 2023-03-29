import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter
from fastapi.responses import Response
from app.core.business.abstracts.UserService import UserService

userService = UserService()
adminroutes = APIRouter()

@adminroutes.post("/")
def create_admin():
    pass


