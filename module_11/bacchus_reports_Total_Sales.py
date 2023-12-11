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


print("-- Total Orders and Sales by Wine Type --")

# Define the SQL query to group by one column and calculate the sum of another column
sql_query = "SELECT wine_order_line.wine_id, wine.wine_type, SUM(wine_order_line.wine_quantity), SUM(wine_order_line.wine_quantity * wine_order_line.wine_price) \
             FROM wine_order_line \
             JOIN wine ON wine.wine_id = wine_order_line.wine_id \
             GROUP BY wine_order_line.wine_id \
             ORDER BY SUM(wine_order_line.wine_quantity * wine_order_line.wine_price);"

# Execute the query
cursor.execute(sql_query)

# Fetch all the rows
result = cursor.fetchall()

# Display the results
for row in result:
    print("Wine: {}\nQuantity: {}\nTotal Sales: {}\n".format(row[1], row[2], row[3]))



input("Press Enter to Exit...")
db.close()