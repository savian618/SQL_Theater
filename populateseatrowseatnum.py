import mysql.connector
import keyring

keyring.set_password("MySQL", "root", "Savian02")

keyring.get_password("MySQL", "root")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Savian02",
    database="theater"
)


mycursor = mydb.cursor()

seatRows = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH"]

for i in seatRows:
    mycursor.execute('INSERT into SeatRow values ("{}")'.format(i))

for i in range(1, 16):
    mycursor.execute('INSERT into SeatNum values("{}")'.format(str(i)))

for i in range(101, 127):
    mycursor.execute('INSERT into SeatNum values("{}")'.format(str(i)))

mydb.commit()
mydb.close()
