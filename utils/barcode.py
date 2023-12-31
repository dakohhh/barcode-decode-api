import cv2 as cv
from typing import Union, Dict, List
from pyzbar.pyzbar import decode




class Barcode():
    def __init__(self, image_data:bytes) -> None:
        
        self.image_data = image_data


    async def get_data(self) -> List:

        image_array = bytearray(self.image_data)

        # Decode the barcode(s) in the image
        image = cv.imdecode(image_array, cv.IMREAD_COLOR)

        barcodes = decode(image)

        decoded_barcodes = []
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type
            decoded_barcodes.append({"type": barcode_type, "data": barcode_data})
    
        return decoded_barcodes






        