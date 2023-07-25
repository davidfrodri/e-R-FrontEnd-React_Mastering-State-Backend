from fastapi import FastAPI
from routers import employees
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(employees.router)