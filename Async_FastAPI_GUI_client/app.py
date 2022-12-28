# Importing necessary packages
from typing import List, Optional
import uvicorn
from fastapi import FastAPI
from employee import Employee, engine, Base, async_session
from employee_dal import EmployeeDAL

# Creating an app instance
app = FastAPI()

# Initializing the database on startup
@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

# Initial get endpoint.
@app.get("/")
async def home():
    return "Employee Management! Visit Swagger Docs to test it out."

# Creating a POST endpoint
@app.post("/employees")
async def create_employee(firstName: str, lastName: str, gender: str, role: str, joinYear: int):
    # Creating an async session
    async with async_session() as session:
        async with session.begin():
            # Creating an EmployeeDAL instance (i.e., our employee)
            employee_dal = EmployeeDAL(session)
            # Adding said employee to the database
            await employee_dal.create_employee(firstName, lastName, gender, role, joinYear)
            return {"firstName": firstName, "lastName": lastName, "gender": gender, "role": role, "joinYear": joinYear}

# Creating a GET endpoint
@app.get("/employees")
async def get_all_employees() -> List[Employee]:
    # Creating an async session
    async with async_session() as session:
        async with session.begin():
            # Get and return all employees from database
            employee_dal = EmployeeDAL(session)
            return await employee_dal.get_employees()

@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    # Creating an sync session
    async with async_session() as session:
        async with session.begin():
            employee_dal = EmployeeDAL(session)
            # Update employee with new updated details
            await employee_dal.delete_employee(employee_id)
            return {"id": employee_id}

# Creating a PUT endpoint
@app.put("/employees/{employee_id}")
async def update_employee(employee_id: int, firstName: Optional[str] = None, lastName: Optional[str] = None, gender: Optional[str] = None, role: Optional[str] = None, joinYear: Optional[int] = None):
    # Creating an sync session
    async with async_session() as session:
        async with session.begin():
            employee_dal = EmployeeDAL(session)
            # Update employee with new updated details
            await employee_dal.update_employee(employee_id, firstName, lastName, gender, role, joinYear)
            return {"id": employee_id}

# Starting a FastAPI application
if __name__ == '__main__':
    uvicorn.run("app:app", port=8000, host='127.0.0.1')