#!/usr/bin/python3
"""Class of User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
