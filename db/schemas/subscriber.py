def subscriber_schema(subscriber) -> dict:
    return {
        "id": str(subscriber["_id"]),
        "email": subscriber["email"],
    }

def subscribers_schema(subscribers) -> list:
    return [subscriber_schema(subscriber) for subscriber in subscribers]