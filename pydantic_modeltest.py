"""
outcome after running the program

guest='Sam' nights=3 email=None
guest='Sam' nights=3 email=None
error in the exection of the 3 line
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='three', input_type=str]
"""
from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class Booking(BaseModel):
    guest: str
    nights: int
    email: Optional[str] = None
    
print(Booking(guest="Sam", nights=3))   
print(Booking(guest="Sam", nights="3"))        # coercion: "3" -> 3
print(Booking(guest="Sam", nights="three"))    # raises ValidationError
