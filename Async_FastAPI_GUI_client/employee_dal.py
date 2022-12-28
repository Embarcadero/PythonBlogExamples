from typing import List, Optional
from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from employee import Employee


class EmployeeDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_employee(self, firstName: str, lastName: str, gender: str, role: str, joinYear: int):
        # Creating an Employee object
        new_employee = Employee(firstName=firstName,lastName=lastName, gender=gender, role=role, joinYear=joinYear)

        # Saving employee to the database
        self.db_session.add(new_employee)
        await self.db_session.flush()

    async def get_employees(self) -> List[Employee]:
        # Retrieving all employees from database and returning them
        q = await self.db_session.execute(select(Employee).order_by(Employee.id))
        return q.scalars().all()

    async def update_employee(self, employee_id: int, firstName: Optional[str], lastName: Optional[str], gender: Optional[str], role: Optional[str], joinYear: Optional[int]):
        # Retrieve employee from database
        q = update(Employee).where(Employee.id == employee_id)

        # Change the employee details
        if firstName:
            q = q.values(firstName=firstName)
        if lastName:
            q = q.values(lastName=lastName)
        if gender:
            q = q.values(gender=gender)
        if role:
            q = q.values(role=role)
        if joinYear:
            q = q.values(joinYear=joinYear)

        # Update employee entity in the database
        q.execution_options(synchronize_session="fetch")
        await  self.db_session.execute(q)

    async def delete_employee(self, employee_id: int):
        # Deleting an employee from database and returning them
        await self.db_session.execute(delete(Employee).where(Employee.id == employee_id))


