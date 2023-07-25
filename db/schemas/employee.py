def employee_schema(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "photo_url": employee["photo_url"],
        "description": employee["description"],
        "name": employee["name"],
        "position": employee["position"],
        "company": employee["company"]
    }

def employees_schema(employees) -> list:
    return [employee_schema(employee) for employee in employees]