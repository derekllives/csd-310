# Group 5
# Display Tables and Labels

# Couldn't write a method that allowed for the granularity of good label names so we followed
# the norm of performing a query, fetching the results, printing a title line,
# then iterating through the entries and putting them with proper labels.

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

# Execute SQL query to retrieve information on which distributor carries which wine
cursor.execute("SELECT distributor_name, wine_type FROM wine_order_line "
               "INNER JOIN wine_order ON wine_order_line.wine_order_id = wine_order.wine_order_id "
               "INNER JOIN distributor ON wine_order.distributor_id = distributor.distributor_id "
               "INNER JOIN wine ON wine_order_line.wine_id = wine.wine_id")

wine_distributor_info = cursor.fetchall()

# Display the report
print("-- DISTRIBUTOR AND WINE INFORMATION --")
for info in wine_distributor_info:
    print("Distributor: {}\nWine Type: {}\n".format(info[0], info[1]))


input("Press Enter to Exit...")
db.close()