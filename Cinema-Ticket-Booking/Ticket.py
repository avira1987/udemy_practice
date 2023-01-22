import random
import string
class Ticket:

    def __init__(self, user, price, seat):
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self):
        pass