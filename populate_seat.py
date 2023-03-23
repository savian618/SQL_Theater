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

c = 0
while c < 25:
    c1 = 1
    c2 = 101

    if c == 1:
        while c1 <= 10:
            mycursor.execute('INSERT into Seat values("A", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("B", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("C", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            c1 += 1
        while c2 <= 114:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("A", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("B", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("C", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("A", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("B", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("C", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
            c2 += 1

        while c2 <= 116:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("B", "{}", "Main Floor", "Right", "Side", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("C", "{}", "Main Floor", "Right", "Side", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("B", "{}", "Main Floor", "Left", "Side", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("C", "{}", "Main Floor", "Left", "Side", {})'.format(c2, False))
            c2 += 1

    if c == 4:
        while c1 <= 11:
            mycursor.execute('INSERT into Seat values("D", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("E", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("F", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            c1 += 1
        while c2 <= 116:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("D", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("E", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("F", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("D", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("E", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("F", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
            c2 += 1
        while c2 <= 118:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("F", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("F", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
            c2 += 1

    if c == 7:
        while c1 <= 12:
            mycursor.execute('INSERT into Seat values("G", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("H", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("J", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            c1 += 1
        while c2 <= 118:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("G", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("H", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("J", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("G", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("H", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("J", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
            c2 += 1

    if c == 10:
        while c1 <= 13:
            mycursor.execute('INSERT into Seat values("K", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("L", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("M", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            c1 += 1
        while c2 <= 120:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("K", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("L", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("M", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("K", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("L", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("M", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
            c2 += 1

    if c == 13:
        while c1 <= 14:
            mycursor.execute('INSERT into Seat values("N", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("O", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("P", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            c1 += 1
        while c2 <= 120:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("N", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("O", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                if c2 <= 108:
                    mycursor.execute('INSERT into Seat values("P", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                if c2 > 108:
                    mycursor.execute('INSERT into Seat values("P", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, True))
            else:
                mycursor.execute('INSERT into Seat values("N", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("O", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                if c2 <= 107:
                    mycursor.execute('INSERT into Seat values("P", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                if c2 > 107:
                    mycursor.execute('INSERT into Seat values("P", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, True))
            c2 += 1
        while c2 <= 122:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("O", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                if c2 <= 108:
                    mycursor.execute('INSERT into Seat values("P", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                if c2 > 108:
                    mycursor.execute('INSERT into Seat values("P", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, True))
            else:
                mycursor.execute('INSERT into Seat values("O", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                if c2 <= 108:
                    mycursor.execute('INSERT into Seat values("P", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                if c2 > 108:
                    mycursor.execute('INSERT into Seat values("P", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, True))
            c2 += 1

    if c == 16:
        while c1 <= 15:
            mycursor.execute('INSERT into Seat values("Q", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("R", "{}", "Main Floor", "Middle", "Orchestra", {})'.format(c1, False))
            c1 += 1
        while c2 <= 122:
            if c2 % 2 == 0:
                if c2 <= 108:
                    mycursor.execute('INSERT into Seat values("Q", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                    mycursor.execute('INSERT into Seat values("R", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, False))
                if c2 > 108:
                    mycursor.execute('INSERT into Seat values("Q", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, True))
                    mycursor.execute('INSERT into Seat values("R", "{}", "Main Floor", "Right", "Orchestra", {})'.format(c2, True))
            else:
                if c2 <= 107:
                    mycursor.execute('INSERT into Seat values("Q", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                    mycursor.execute('INSERT into Seat values("R", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, False))
                if c2 > 107:
                    mycursor.execute('INSERT into Seat values("Q", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, True))
                    mycursor.execute('INSERT into Seat values("R", "{}", "Main Floor", "Left", "Orchestra", {})'.format(c2, True))
            c2 += 1

    if c == 18:
        while c1 <= 13:
            mycursor.execute('INSERT into Seat values("AA", "{}", "Balcony", "Middle", "Orchestra", {})'.format(c1, False))
            c1 += 1
        while c2 <= 124:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("AA", "{}", "Balcony", "Right", "Side", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("AA", "{}", "Balcony", "Left", "Side", {})'.format(c2, False))
            c2 += 1

    if c == 19:
        while c1 <= 14:
            mycursor.execute('INSERT into Seat values("BB", "{}", "Balcony", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("CC", "{}", "Balcony", "Middle", "Orchestra", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("DD", "{}", "Balcony", "Middle", "Orchestra", {})'.format(c1, False))
            c1 += 1
        while c2 <= 124:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("BB", "{}", "Balcony", "Right", "Side", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("CC", "{}", "Balcony", "Right", "Side", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("DD", "{}", "Balcony", "Right", "Side", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("BB", "{}", "Balcony", "Left", "Side", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("CC", "{}", "Balcony", "Left", "Side", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("DD", "{}", "Balcony", "Left", "Side", {})'.format(c2, False))
            c2 += 1
        while c2 <= 126:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("DD", "{}", "Balcony", "Right", "Side", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("DD", "{}", "Balcony", "Left", "Side", {})'.format(c2, False))
            c2 += 1

    if c == 22:
        while c1 <= 10:
            mycursor.execute('INSERT into Seat values("EE", "{}", "Balcony", "Middle", "Upper Balcony", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("FF", "{}", "Balcony", "Middle", "Upper Balcony", {})'.format(c1, False))
            c1 += 1
        while c2 <= 122:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("EE", "{}", "Balcony", "Right", "Upper Balcony", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("FF", "{}", "Balcony", "Right", "Upper Balcony", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("EE", "{}", "Balcony", "Left", "Upper Balcony", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("FF", "{}", "Balcony", "Left", "Upper Balcony", {})'.format(c2, False))
            c2 += 1

    if c == 24:
        while c1 <= 11:
            mycursor.execute('INSERT into Seat values("GG", "{}", "Balcony", "Middle", "Upper Balcony", {})'.format(c1, False))
            mycursor.execute('INSERT into Seat values("HH", "{}", "Balcony", "Middle", "Upper Balcony", {})'.format(c1, False))
            c1 += 1
        while c2 <= 118:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("GG", "{}", "Balcony", "Right", "Upper Balcony", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("HH", "{}", "Balcony", "Right", "Upper Balcony", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("GG", "{}", "Balcony", "Left", "Upper Balcony", {})'.format(c2, False))
                mycursor.execute('INSERT into Seat values("HH", "{}", "Balcony", "Left", "Upper Balcony", {})'.format(c2, False))
            c2 += 1
        while c2 <= 120:
            if c2 % 2 == 0:
                mycursor.execute('INSERT into Seat values("GG", "{}", "Balcony", "Right", "Upper Balcony", {})'.format(c2, False))
            else:
                mycursor.execute('INSERT into Seat values("GG", "{}", "Balcony", "Left", "Upper Balcony", {})'.format(c2, False))
            c2 += 1
    c += 1

rows = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R"]

for c in rows:
    mycursor.execute("UPDATE Seat set PricingTier = %s WHERE SeatRow = %s and SeatNumber > 106" % ("Side", c))

mydb.commit()
mydb.close()
