from pydantic import BaseModel

class Subscriber(BaseModel):
    id: str | None
    email: str
