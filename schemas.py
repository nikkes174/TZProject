from datetime import date
from typing import Optional

from pydantic import BaseModel


class ClientBase(BaseModel):
    user_name: str
    start_subscription: date
    end_subscription: date
    period_subscription: int


class CreateClient(ClientBase):
    pass


class ClientUpdate(BaseModel):
    user_name: Optional[str] = None
    start_subscription: Optional[date] = None
    end_subscription: Optional[date] = None
    period_subscription: Optional[int] = None


class ClientResponse(ClientBase):
    client_id: int

    class Config:
        orm_mode = True
