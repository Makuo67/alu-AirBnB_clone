#!/usr/bin/python3
""" Class user that inherits from baseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """user representation"""
    email=""
    password=""
    first_name=""
    last_time=""
