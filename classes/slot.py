class Slot():
    def __init__(self, slot_number, is_empty, registration_no, colour, associated_ticket):
        self.__slot_number = slot_number
        self.__is_empty = is_empty
        self.__registration_no = registration_no
        self.__colour = colour
        self.__associated_ticket = associated_ticket

    def get_registration_no(self):
        return self.__registration_no

    def get_slot_number(self):
        return self.__slot_number

    def get_colour(self):
        return self.__colour

    def get_associated_ticket(self):
        return self.__associated_ticket

    def is_empty(self):
        return self.__is_empty

    def mark_empty(self):
        self.__is_empty = True
        self.__registration_no = None
        self.__colour = None
        self.__associated_ticket = None
