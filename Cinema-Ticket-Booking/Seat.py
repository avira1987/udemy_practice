class Ticket:

    database= "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        pass

    def is_free(self, availability):
        pass

    def occupy(self):
        pass
        