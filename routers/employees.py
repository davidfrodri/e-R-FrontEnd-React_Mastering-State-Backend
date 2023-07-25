from fastapi import APIRouter, HTTPException, status
from db.models.employee import Employee
from db.client import my_database
from db.schemas.employee import employee_schema, employees_schema
from bson import ObjectId

router = APIRouter(tags=["employees"])

@router.get("/employees", response_model=list[Employee])
async def employees():
    return employees_schema(my_database.employees.find())

def search_employee(field: str, key):
    try:
        employee = employee_schema(my_database.employees.find_one({field: key}))
        return Employee(**employee)
    except:
        return {"error": "Employee not found"}

@router.get("/employee/{id}")
async def employee(id: str):
    return search_employee("_id", ObjectId(id))


@router.post("/employee/", response_model=Employee, status_code=201)
async def employee(employee: Employee):
    if type(search_employee("name", employee.name)) == Employee:
        raise HTTPException(status_code=409, detail="Employee already exist") 

    employee_dict = dict(employee)
    del employee_dict["id"]

    id = my_database.employees.insert_one(employee_dict).inserted_id

    new_employee = employee_schema(my_database.employees.find_one({"_id": id}))

    return Employee(**new_employee)


@router.put("/employee/", response_model=Employee, status_code=201)
async def employee(employee: Employee):
    employee_dict = dict(employee)
    
    del employee_dict["id"]

    try:

        my_database.employees.find_one_and_replace({"_id": ObjectId(employee.id)}, employee_dict)

    except:
        return {"error": "Employee not found"}

    return search_employee("_id", ObjectId(employee.id))



@router.delete("/employee/{id}")
async def employee(id: str, status_code=status.HTTP_204_NO_CONTENT):

    found = my_database.employees.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "Employee not found"}
    else:
        return {"success": f"Employee with id = {id} has been deleted"}
