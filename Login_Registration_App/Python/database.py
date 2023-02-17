# import necessary packages
from sqlalchemy import create_engine, MetaData, Table, Column, VARCHAR

# establish connections - create new file db and connect of connect if it already exists
engine = create_engine(
	'sqlite:///users.db')

# initialize the Metadata Object
meta = MetaData(bind=engine)

# create a table schema
users = Table(
	'users', meta,
	Column('email', VARCHAR, primary_key=True),
	Column('fname', VARCHAR),
	Column('lname', VARCHAR),
    Column('password', VARCHAR)
)

meta.create_all(engine)