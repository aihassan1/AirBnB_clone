#!/usr/bin/python3
""" Defines the State class, inheriting from BaseModel """

from models.base_model import BaseModel


class State(BaseModel):
    """State class represents a geographical state"""
    name = ''
