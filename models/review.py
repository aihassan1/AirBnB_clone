#!/usr/bin/python3
""" Defines the Review class, inheriting from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review with attributes"""
    place_id = ''
    user_id = ''
    text = ''
