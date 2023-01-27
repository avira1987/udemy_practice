import sqlite3

def create_table():
    connection=sqlite3.connect("cinema.db")

    connection.execute("""
    CREATE TABLE "Seat" (
        "seat_id"	TEXT,
        "taken"	INTEGER,
        "price"	REAL
    );
    """)

    connection.commit()
    connection.close()

# create_table()

def create_table_card():
    connection=sqlite3.connect("Banking.db")

    connection.execute("""
    CREATE TABLE "Card" (
        "balance" INTEGER,
        "type" TEXT,
        "number" INTEGER,
        "cvc" INTEGER,
        "holder" TEXT
    );
    """)

    connection.commit()
    connection.close()

create_table_card()