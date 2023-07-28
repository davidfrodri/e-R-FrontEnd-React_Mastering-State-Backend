from fastapi import APIRouter, HTTPException, status
from db.models.subscriber import Subscriber
from db.schemas.subscriber import subscriber_schema, subscribers_schema
from db.client import subscribers_database
from bson import ObjectId

router = APIRouter(tags=["Subscribe"])

@router.get("/subscribe", response_model=list[Subscriber])
async def subscribers():
    return subscribers_schema(subscribers_database.subscriber.find())

def search_subscriber(field: str, key):
    try:
        subscriber = subscriber_schema(subscribers_database.subscriber.find_one({field: key}))
        return Subscriber(**subscriber)
    except:
        return {"error": "Subscriber not found"}

@router.post("/subscribe", response_model=Subscriber, status_code=201)
async def subscriber(subscriber: Subscriber):
    if type(search_subscriber("email", subscriber.email)) == Subscriber:
        raise HTTPException(status_code=409, detail="Subscriber already exist") 

    subscriber_dict = dict(subscriber)
    del subscriber_dict["id"]

    id = subscribers_database.subscriber.insert_one(subscriber_dict).inserted_id

    new_subscriber = subscriber_schema(subscribers_database.subscriber.find_one({"_id": id}))

    return Subscriber(**new_subscriber)

@router.delete("/subscribe")
async def subscriber(email: str, status_code=status.HTTP_204_NO_CONTENT):

    found = subscribers_database.subscriber.find_one_and_delete({"email": email})

    if not found:
        raise HTTPException(status_code=404, detail="Subscriber not found")
    else:
        return {"success": f"Subscriber with email = {email} has been deleted"}
