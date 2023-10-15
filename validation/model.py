from typing import List, Union
from fastapi import Form
from pydantic import BaseModel, validator
from exceptions.custom_exception import BadRequestException


class TokenData(BaseModel):
    username:str
    user_id: str
    refresh_token: Union[str, None]
    expire: int







