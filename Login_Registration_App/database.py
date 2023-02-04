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

# # insert records into the table
# dummy1 = users.insert().values(email='zain10@gmail.com', fname='Zain', lname='Khan', password='123xyz')

# # execute the insert record statement
# engine.execute(dummy1)
  
# # write the SQL query inside the text() block
# sql = text('SELECT * from users')
# # results = engine.execute(sql)
  
# # Fetch all the records
# result = engine.execute(sql).fetchall()
    
# # View the records
# for record in result:
#     print("\n", record)