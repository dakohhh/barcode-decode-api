from fastapi import Request, APIRouter, BackgroundTasks, status
from authentication.hashing import hashPassword
from response.response import CustomResponse



router = APIRouter(tags=["User"], prefix="/user")




@router.get("/")
async def get_user(request:Request, background_task:BackgroundTasks):

    return CustomResponse("user successfully")

















    







