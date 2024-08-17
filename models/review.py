#!/usr/bin/python3
"""The review Module: Holds Review class of the project."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Define the Review Class."""

    place_id = ""
    user_id = ""
    text = ""
