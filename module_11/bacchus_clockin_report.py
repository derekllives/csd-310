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

cursor.execute("SELECT emp_first,emp_last,emp_rate, \
               DATE_FORMAT(clock_in,'%a %b %c'),TIME_TO_SEC(clock_out - clock_in) / 3600 \
               FROM employee INNER JOIN employee_clock ON employee.emp_id=employee_clock.emp_id \
               WHERE clock_in BETWEEN '2023-11-27 00:00:00' AND '2023-11-27 23:59:59'")
shifts = cursor.fetchall()

print("--DISPLAYING Shift RECORDS --")
laborcost = 0
for shift in shifts:
    print("Employee Name: {} {}\nPay Rate: {}\nShift Day: {}\nShift Length: {:.2f} hours\n".format(shift[0],shift[1],shift[2],shift[3],shift[4]))
    laborcost += shift[2] * shift[4]
print("Total labor cost: ${:.2f}".format(laborcost))

input("Press Enter to Exit...")
db.close()