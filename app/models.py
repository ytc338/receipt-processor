from datetime import date, time
from pydantic import BaseModel, Field

class Item(BaseModel):
    shortDescription: str = Field(pattern="^[\w\s\-]+$")
    price: str = Field(pattern="^\d+\.\d{2}$")

class Receipt(BaseModel):
    retailer: str = Field(pattern="^[\w\s\-&]+$")
    purchaseDate: date
    purchaseTime: time
    items: list[Item]
    total: str = Field(pattern="^\d+\.\d{2}$")
