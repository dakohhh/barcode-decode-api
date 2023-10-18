import os
import certifi
from fastapi import FastAPI
from routers.barcode import router as barcode
from exceptions.custom_exception import *
from dotenv import load_dotenv




load_dotenv()



CERTIFICATE = os.path.join(os.path.dirname(certifi.__file__), "cacert.pem")



app = FastAPI()



app.include_router(barcode)
app.add_exception_handler(UserExistException, user_exist_exception_handler)
app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)
app.add_exception_handler(ServerErrorException, server_exception_handler)
app.add_exception_handler(NotFoundException, not_found)
app.add_exception_handler(CredentialsException, credentail_exception_handler)
app.add_exception_handler(BadRequestException, bad_request_exception_handler)









