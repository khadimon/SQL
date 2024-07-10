import sqlite3

connection = sqlite3.connect('customer_orders.db')
cursor = connection.cursor()


table = """CREATE TABLE CUSTOMER_ORDERS (
    CustomerID INT,
    FirstName char(25) not null,
    LastName char(25) not null,
    Email varchar (255) not null
); """

cursor.execute(table)

cursor.execute('''INSERT INTO CUSTOMER_ORDERS (001, 'Michael', 'Dell', 'michael.dell@com')''')
cursor.execute('''INSERT INTO CUSTOMER_ORDERS (002, 'Jeff', 'Clarke', 'jeff.clarke@com')''')
cursor.execute('''INSERT INTO CUSTOMER_ORDERS (003, 'Caitlin', 'Clark', 'caitlin.clark@com')''')

print("Data inserted: ")
data = cursor.execute('''SELECT * FROM CUSTOMER_ORDERS''')
for row in data:
    print(row)

connection.commit()
connection.close()
