from typing import Optional

from pydantic import BaseModel


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_model = True
        schema_extra = {
            "example": {
                "username": "Paul",
                "email": "paul@gmail.com",
                "password": "paulolocco4365",
                "is_staff": False,
                "is_active": True,
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = "eba52c9cc05ee42ebcf9141f0cb6f3b8ac893a17af9ccd19c657c82b1cb1371f"


class LoginModel(BaseModel):
    username_or_email: str
    password: str


class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = "PENDING"
    user_id: Optional[int]
    product_id: int

    class Config:
        orm_model = True
        schema_extra = {"example": {"quantity": 2, "product_id": 2374}}


class OrderStatusModel(BaseModel):
    order_status: Optional[str] = "PENDING"

    class Config:
        orm_model = True
        schema_extra = {
            "example": {
                "order_status": "PENDING",
            }
        }


class ProductModel(BaseModel):
    id: Optional[int]
    name: str
    price: int

    class Config:
        orm_model = True
        schema_extra = {"example": {"product_id": 2374, "name": "Nike Shoes", "price": 89}}
