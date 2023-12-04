# Author: Brandon Hackett, Darnell Lewis, Derek Livermont, Lindsey Yin
# 12/3/23
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

cursor.execute("SELECT * FROM employee")
employees = cursor.fetchall()
print("--DISPLAYING Employee RECORDS --")
for employee in employees:
    print("Employee ID: {}\nEmployee Name: {} {}\nEmployee Position: {}\nEmployee Pay Rate: ${}\nEmployee Hire Date: {}\n".format(employee[0],employee[1],employee[2],employee[3],employee[4],employee[5]))

cursor.execute("SELECT clock_id, emp_first, emp_last, clock_in, clock_out "
               "FROM employee INNER JOIN employee_clock on employee_clock.emp_id=employee.emp_id")
clockrecords = cursor.fetchall()
print("--DISPLAYING Clock-in RECORDS --")
for clockrecord in clockrecords:
    print("Clock-in ID: {}\nEmployee Name: {} {}\nClock In: {}\nClock Out: {}\n".format(clockrecord[0],clockrecord[1],clockrecord[2],clockrecord[3],clockrecord[4]))

cursor.execute("SELECT * FROM distributor")
distributors = cursor.fetchall()
print("--DISPLAYING Distributor RECORDS --")
for distributor in distributors:
    print("Distributor ID: {}\nDistributor Name: {}\nDistributor Contact: {}\nDistributor Email: {}\nDistributor Phone: {}\n".format(distributor[0],distributor[1],distributor[2],distributor[3],distributor[4]))

cursor.execute("SELECT * FROM wine")
wines = cursor.fetchall()
print("--DISPLAYING Wine RECORDS --")
for wine in wines:
    print("Wine ID: {}\nWine Type: {}\nWine Production Date: {}\nWine Quantity: {} bottles\n".format(wine[0],wine[1],wine[2],wine[3]))

cursor.execute("SELECT wine_order_id, distributor_name,order_date,expected_delivery,actual_delivery "
               "FROM wine_order INNER JOIN distributor on distributor.distributor_id=wine_order.distributor_id")
wineorders = cursor.fetchall()
print("--DISPLAYING Wine Order RECORDS --")
for wineorder in wineorders:
    print("Wine Order ID: {}\nDistributor Name: {}\nOrder Date: {}\nExpected Delivery: {}\nActual Delivery: {}\n".format(wineorder[0],wineorder[1],wineorder[2],wineorder[3],wineorder[4]))

cursor.execute("SELECT wine_order_line_id,distributor_name,wine_type,wine_quantity, wine_price "
                "FROM wine_order INNER JOIN distributor on distributor.distributor_id=wine_order.distributor_id "
                "INNER JOIN wine_order_line on wine_order.wine_order_id=wine_order_line.wine_order_id "
		        "INNER JOIN wine on wine.wine_id=wine_order_line.wine_id;")
wineorderlines = cursor.fetchall()
print("--DISPLAYING Wine Order Line RECORDS --")
for wineorderline in wineorderlines:
    print("Wine Order Line ID: {}\nDistributor Name: {}\nWine Type: {}\nWine Quantity: {} bottles\nWine Price: ${}\n".format(wineorderline[0],wineorderline[1],wineorderline[2],wineorderline[3],wineorderline[4]))

cursor.execute("SELECT * FROM supplier")
suppliers = cursor.fetchall()
print("--DISPLAYING Supplier RECORDS --")
for supplier in suppliers:
    print("Supplier ID: {}\nSupplier Name: {}\nSupplier Contact: {}\nSupplier Email: {}\nSupplier Phone: {}\n".format(supplier[0],supplier[1],supplier[2],supplier[3],supplier[4]))

cursor.execute("SELECT * FROM component")
components = cursor.fetchall()
print("--DISPLAYING Component RECORDS --")
for component in components:
    print("Component ID: {}\ncomponent Name: {}\nComponent Quantity On-hand: {}\n".format(component[0],component[1],component[2]))

cursor.execute("SELECT supply_order_id, supplier_name,order_date,expected_delivery,actual_delivery "
               "FROM supply_order INNER JOIN supplier on supplier.supplier_id=supply_order.supplier_id")
supplyorders = cursor.fetchall()
print("--DISPLAYING Supply Order RECORDS --")
for supplyorder in supplyorders:
    print("Supply Order ID: {}\nSupplier Name: {}\nOrder Date: {}\nExpected Delivery: {}\nActual Delivery: {}\n".format(supplyorder[0],supplyorder[1],supplyorder[2],supplyorder[3],supplyorder[4]))

cursor.execute("SELECT supply_order_line_id,supplier_name,component_name,component_quantity,component_price "
                "FROM supply_order INNER JOIN supplier on supplier.supplier_id=supply_order.supplier_id "
                "INNER JOIN supply_order_line on supply_order.supply_order_id=supply_order_line.supply_order_id "
		        "INNER JOIN component on component.component_id=supply_order_line.component_id;")
supplyorderlines = cursor.fetchall()
print("--DISPLAYING Supply Order Line RECORDS --")
for supplyorderline in supplyorderlines:
    print("Supply Order Line ID: {}\nSupplier Name: {}\nSupply Type: {}\nQuantity Ordered: {}\nSupply Price/Unit: ${}\n".format(supplyorderline[0],supplyorderline[1],supplyorderline[2],supplyorderline[3],supplyorderline[4]))

input("Press Enter to Exit...")
db.close()