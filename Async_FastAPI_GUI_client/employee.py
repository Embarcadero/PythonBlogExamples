# Importing packages
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

# Configuring
DB_URL = "sqlite+aiosqlite:///./employees.db"

# Creating a database instance
engine = create_async_engine(DB_URL, future=True, echo=True)

# Creating a session maker
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Creating a base to configure DB models
Base = declarative_base()

# Configuring our DB model with tablename "employees"
class Employee(Base):
    __tablename__ = 'employees'

    # Initializing the columns and their data types
    id = Column(Integer, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    role = Column(String, nullable=False)
    joinYear = Column(Integer, nullable=False)