import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Sonshynedc84!",
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("Connected to the Outland Adventures database successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The username or password is incorrect.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The database does not exist.")
    else:
        print(err)

tables = [
    "CUSTOMER",
    "LOCATION",
    "TRIP",
    "EQUIPMENT",
    "BOOKING",
    "EQUIPMENT_TRANSACTION"
]

for table in tables:
    print("\n" + "=" * 60)
    print(table)
    print("=" * 60)

    cursor.execute(f"SELECT * FROM {table}")

    column_names = [column[0] for column in cursor.description]
    print(" | ".join(column_names))

    for row in cursor.fetchall():
        print(" | ".join(str(value) for value in row))

cursor.close()
db.close()

