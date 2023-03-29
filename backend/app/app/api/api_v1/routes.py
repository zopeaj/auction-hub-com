import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter
from app.api.api_v1.controller.AdminController import adminroutes
from app.api.api_v1.controller.AuctionController import auctionroutes
from app.api.api_v1.controller.BidderController import bidderroutes
from app.api.api_v1.controller.UserController import userroutes

api_router = APIRouter()
api_router.include_router(adminroutes, prefix="/admin", tags=["admin"])
api_router.include_router(auctionroutes, prefix="/auction", tags=["auction"])
api_router.include_router(bidderroutes, prefix="/bidder", tags=["bidder"])
api_router.include_router(userroutes, prefix="/user", tags=["user"])

