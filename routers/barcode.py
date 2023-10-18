import cv2 as cv
import numpy as np
from fastapi import Request, APIRouter, File, UploadFile
from response.response import CustomResponse
from utils.barcode import Barcode


router = APIRouter(tags=["Barcode"], prefix="/barcode")




@router.get("/")
async def get_barcode_data(request:Request, image:UploadFile = File(...)):

    image_data = await image.read()

    barcode = Barcode(image_data)

    decoded_barcodes = await barcode.get_data()

    return CustomResponse("barcode scanned", data=decoded_barcodes)

