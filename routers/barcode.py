import cv2 as cv
import numpy as np
from fastapi import Request, APIRouter, File, UploadFile
from response.response import CustomResponse
from pyzbar.pyzbar import decode



router = APIRouter(tags=["Barcode"], prefix="/barcode")




@router.get("/")
async def get_barcode_data(request:Request, image:UploadFile = File(...)):

    image_data = await image.read()

    nparr = np.frombuffer(image_data, np.uint8)

    image = cv.imdecode(nparr, cv.IMREAD_COLOR)

    barcodes = decode(image)

    decoded_barcodes = []
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        decoded_barcodes.append({"type": barcode_type, "data": barcode_data})


    print(decoded_barcodes)


    return CustomResponse("barcode scanned", data=decoded_barcodes)

