#!/usr/bin/python3
""" Defines the Amenity class, inheriting from BaseModel """

from models.base_model import BaseModel


class Amenity (BaseModel):
    """Represents a Amenity with name attributes"""
    name = ''