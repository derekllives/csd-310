# Author: Brandon Hackett, Darnell Lewis, Derek Livermont, Lindsey Yin
# 12/5/23
# Pull up reports


import mysql.connector
from mysql.connector import errorcode

config = {
    "user":"bacchus_user",
    "password":"ILoveWine!",
    "host":"127.0.0.1",
    "database":"bacchus",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    
    else:
        print(err)

cursor = db.cursor()

print("-- LATE WINE ORDERS --")
cursor.execute("SELECT distributor_name, order_date, DATEDIFF(actual_delivery,expected_delivery) "
               "FROM wine_order INNER JOIN distributor ON wine_order.distributor_id=distributor.distributor_id;")
orders = cursor.fetchall()
for order in orders:
    try:
        if int(order[2]) > 0:
            print("Distributor: {}\nOrder Date: {}\nExpected vs. Actual Delivery: {} day(s) late\n".format(order[0],order[1],order[2]))
    except:
        continue

print("-- LATE SUPPLY ORDERS --")
cursor.execute("SELECT supplier_name, order_date, DATEDIFF(actual_delivery,expected_delivery) "
               "FROM supply_order INNER JOIN supplier ON supply_order.supplier_id=supplier.supplier_id;")
orders = cursor.fetchall()
for order in orders:
    try:
        if int(order[2]) > 0:
            print("Supplier: {}\nOrder Date: {}\nExpected vs. Actual Delivery: {} day(s) late\n".format(order[0],order[1],order[2]))
    except:
        continue

input("Press Enter to Exit...")
db.close()