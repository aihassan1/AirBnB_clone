#!/usr/bin/python3
""" user class definition - inhirits from the baseclass """

from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
