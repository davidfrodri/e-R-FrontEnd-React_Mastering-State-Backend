from pydantic import BaseModel

class Employee(BaseModel):
    id: str | None
    photo_url: str
    description: str
    name: str
    position: str
    company: str