class Ticket:
    def __init__(self, seat_id, peric, availability):
        self.seat_id = seat_id
        self.peric = peric
        self.availvabity = availability

    def is_free(self, availability):
        pass

    def occupy(self):
        pass
        