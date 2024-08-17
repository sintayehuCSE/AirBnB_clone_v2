#!/usr/bin/python3
"""User Management Module. It contains User() class that inherit
    From BaseModel() class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the User object interface for the project."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
