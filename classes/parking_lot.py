import heapq
from .ticket import Ticket
from .slot import Slot


class ParkingLot():
    def __init__(self, number_of_slots):
        self.__number_of_slots = number_of_slots
        self.__empty_slots = list(range(1, number_of_slots+1))
        self.__slot_details = {}
        self.__ticket_details = {}
        self.__ticket_counter = 0
        heapq.heapify(self.__empty_slots)

    def get_next_empty_slot(self):
        return self.__empty_slots[0]

    def park_new_car(self, registration_no, colour):
        self.__ticket_counter = self.__ticket_counter + 1
        next_slot = self.get_next_empty_slot()
        self.__ticket_details[self.__ticket_counter] = Ticket(self.__ticket_counter, registration_no, colour, next_slot, False)
        self.__slot_details[next_slot] = Slot(next_slot, False, registration_no, colour, self.__ticket_counter)
        heapq.heappop(self.__empty_slots)

