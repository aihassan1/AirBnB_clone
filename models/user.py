#!/usr/bin/python3
""" user class definition - inhirits from the baseclass """

from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""

    def __init__(self):
        """class constructor"""
        super().__init__() 
        
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
