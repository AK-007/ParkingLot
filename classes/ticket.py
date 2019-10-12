class Ticket():
    def __init__(self, ticket_id, registration_no, colour, expired):
        self.__ticket_id = ticket_id;
        self.__registration_no = registration_no;
        self.__colour = colour;
        self.__expired = expired;

    def get_registration_no(self):
        return self.__registration_no

    def get_colour(self):
        return self.__colour

    def is_expired(self):
        return self.__expired

    def mark_expired(self):
        self.__expired = True