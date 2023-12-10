#!/usr/bin/python3
""" Defines the City class, inheriting from BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """defines a city class """
    state_id = ''
    name = ''
