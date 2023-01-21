

import sqlite3
def create_table():
    connection=sqlite3.connect("cinam.db")

    connection.execute("""
    CREATE TABLE "Seat" (
        "seat_id"	TEXT,
        "taken"	INTEGER,
        "price"	REAL
    );
    """)

    connection.commit()
    connection.close()

def insert_record():
    connection=sqlite3.connect("cinam.db")
    connection.execute("""
    INSERT INTO "Seat"("seat_id","taken","price") VALUES ("A3", "0", "90"),("A4", "1", "90"),("A5", "0", "90") 
    """)
    connection.commit()
    connection.close()

def select_all():
    connection = sqlite3.connect("cinam.db")
    curser = connection.cursor()
    curser.execute("""
    SELECT * FROM "Seat"
    """)
    result = curser.fetchall()
    connection.close()
    return result

def select_sepecific_clumns():
    connection = sqlite3.connect("cinam.db")
    curser = connection.cursor()
    curser.execute("""
    SELECT "seat_id", "price" FROM "Seat"
    """)
    result = curser.fetchall()
    connection.close()
    return result

def select_with_condition():
    connection = sqlite3.connect("cinam.db")
    curser = connection.cursor()
    curser.execute("""
    SELECT "seat_id", "price" FROM "Seat" WHERE "price">80
    """)
    result = curser.fetchall()
    connection.close()
    return result

def update_value(occupied, seat_id):
    connetion = sqlite3.connect("cinam.db")
    connetion.execute("""
    UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?
    """,[occupied,seat_id])
    connetion.commit()
    connetion.close()

def delete_value():
    connetion = sqlite3.connect("cinam.db")
    connetion.execute("""
    DELETE FROM "Seat" WHERE "seat_id"="A3"
    """)
    connetion.commit()
    connetion.close()



# delete_value()
update_value(occupied=0,seat_id="A4")
# print(select_with_condition())
# print(select_sepecific_clumns())
# print(select_all())
# insert_record()
