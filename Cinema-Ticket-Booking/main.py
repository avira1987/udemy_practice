import random
import string
from fpdf import FPDF
import sqlite3

class User:
    """Represents a user that can buy a cinema Seat """
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        """Buys the ticket if the card is valid """
        if seat.is_free():
            print("Seat is free")
            if card.validate(price=seat.get_price()):
                print("Card validate passed")
                seat.occupy()
                print("Seat occupy passed")
                ticket = Ticket(user = self, price=seat.get_price(), seat_number=seat_id)
                print("Ticket buy passed")
                ticket.to_pdf()
                return "Purchase successful"
            else:
                return "There was a problem with your card"
        else:
            return "Seat is taken!"

class Seat:

    database= "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Get the price of a certain seat"""
        connetion = sqlite3.connect(self.database)
        cursor = connetion.cursor()
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id" = ?
        """,[self.seat_id])
        price = cursor.fetchall()[0][0]
        return price
    
    def is_free(self):
        """Check in the database if a Seat is taken or not"""
        connetion = sqlite3.connect(self.database)
        cursor = connetion.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id"= ?
        """,[self.seat_id])
        result = cursor.fetchall()[0][0]

        if result == 0:
            return True
        else:
            return False

    def occupy(self):
        """Change value of taken in the databse from 0 to 1 if Seat is free"""
        if self.is_free():
            connetion = sqlite3.connect(self.database)
            connetion.execute("""
            UPDATE "Seat" SET "taken"= ? WHERE "seat_id" = ?
            """,[1,self.seat_id])
            connetion.commit()
            connetion.close()        

class Card:
    
    database= "banking.db"

    def __init__(self, type, number, cvc, holder):
        self.type= type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        """Checks if card is valid and has balance.
        Subtracts price from balance
        """ 
        connetion = sqlite3.connect(self.database)
        cursor = connetion.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number" =? and "cvc" = ?
        """,[self.number, self.cvc])
        result = cursor.fetchall()
        print(result)
        if result:
            balance = result[0][0]
            if balance >= price:
                connetion.execute("""
                UPDATE "Card" SET "balance" = ? WHERE "number" = ? and "cvc"= ?
                """ ,[balance - price, self.number, self.cvc])
                connetion.commit()
                connetion.close()

                return True
        # else:
        #     balance=10
        #     # name1= name
        #     data_tuple=(balance, self.type, self.number, self.cvc, name)
        #     sql_param ="""INSERT INTO "Card"("balance" ,"type" ,"number" ,"cvc" ,"holder" ) VALUES (?,?,?,?,?)"""
        #     connetion.execute(sql_param,data_tuple)

        #     connetion.commit()
        #     connetion.close()
        #     return True

        
class Ticket:
    """Represents a cinema Ticket purchased by a User"""

    def __init__(self, user, price, seat_number):
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.user = user
        self.price = price
        self.seat_number = seat_number

    def to_pdf(self):
        """Create a PDF ticket"""
        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family="Times", style='B', size=24)
        pdf.cell(w=0, h=80, txt="Your Digital Ticket", border=1, ln=1, align="C")

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt = 'Name', border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=self.user.name, border=0, ln= 1)
        pdf.cell(w=0, h=5 ,txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt = 'Ticket ID', border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=self.id, border=0, ln= 1)
        pdf.cell(w=0, h=5 ,txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt = 'Price', border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=0, ln= 1)
        pdf.cell(w=0, h=5 ,txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt = 'Seat Number', border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=self.seat_number, border=0, ln= 1)
        pdf.cell(w=0, h=5 ,txt="", border=0, ln=1)

        pdf.output("sample.pdf", 'F')

if __name__ == "__main__":
    name = input("your full name:")
    seat_id = input("Prederred seat number:")
    card_type = input("Your card type:")
    card_number = input("Your card number:")
    card_cvc = input("Your card cvc:")
    card_holder = input("Card holder name:")

    user = User(name=name)
    seat = Seat(seat_id=seat_id)
    card = Card(type=card_type, number=card_number, cvc= card_cvc, holder= card_holder)

    print(user.buy(seat=seat, card=card))