import heapq
from .ticket import Ticket
from .slot import Slot


class ParkingLot():
    def __init__(self, number_of_slots):
        self.__number_of_slots = number_of_slots
        self.__empty_slots = list(range(1, number_of_slots+1))
        self.__slot_details = {}
        self.__ticket_details = {}
        # ticket_counter maintains the ticket_id for next parking
        self.__ticket_counter = 0
        # heapq is used to get the first empty slot for next parking
        heapq.heapify(self.__empty_slots)

    def get_parking_lot_size(self):
        return self.__number_of_slots

    def get_next_empty_slot(self):
        return self.__empty_slots[0]

    def is_slot_empty(self, slot_number):
        return self.__slot_details[slot_number].is_empty()

    def park_new_car(self, registration_no, colour):
        # Check if any empty slots left
        if len(self.__empty_slots) == 0:
            return "Sorry, parking lot is full"

        self.__ticket_counter = self.__ticket_counter + 1
        next_slot = self.get_next_empty_slot()

        # Issuing new ticket for car parking
        self.__ticket_details[self.__ticket_counter] = Ticket(self.__ticket_counter, registration_no, colour, False)

        # Updating the slot with the car details
        self.__slot_details[next_slot] = Slot(next_slot, False, registration_no, colour, self.__ticket_counter)

        # Removing current slot from empty_slots list
        heapq.heappop(self.__empty_slots)
        return "Allocated slot number: {0}".format(next_slot)

    def car_departure(self, slot_number):
        # Case when the no car was ever parked on this slot
        if slot_number not in self.__slot_details.keys():
            return "Slot number {0} is already empty".format(slot_number)

        if self.__slot_details[slot_number].is_empty():
            return "Slot number {0} is already empty".format(slot_number)

        # Fetching the ticket_id associated with the slot to mark it as expired so that the user can't use it again
        ticket_id = self.__slot_details[slot_number].get_associated_ticket()
        self.__slot_details[slot_number].mark_empty()
        self.__ticket_details[ticket_id].mark_expired()

        # Adding current slot to empty_slots list
        heapq.heappush(self.__empty_slots, slot_number)
        return "Slot number {0} is free".format(slot_number)

    # Returns the registration numbers of all the cars which are parked and have the given colour
    def registration_numbers_for_cars_with_colour(self, colour):
        registration_list = []
        for i in range(1, self.__number_of_slots+1):
            # Case when the no car was ever parked on ith slot
            if i not in self.__slot_details.keys():
                continue
            slot = self.__slot_details[i]
            if not slot.is_empty():
                if slot.get_colour() == colour:
                    registration_list.append(slot.get_registration_no())

        return registration_list

    # Slot numbers of all slots where a car of a particular colour is parked
    def slot_numbers_for_cars_with_colour(self, colour):
        slot_list = []
        for i in range(1, self.__number_of_slots+1):
            # Case when the no car was ever parked on ith slot
            if i not in self.__slot_details.keys():
                continue
            slot = self.__slot_details[i]
            if not slot.is_empty():
                if slot.get_colour() == colour:
                    slot_list.append(slot.get_slot_number())

        return slot_list

    # Slot number in which a car with a given registration number is parked
    def slot_number_for_registration_number(self, registration_no):
        for i in range(1, self.__number_of_slots+1):
            # Case when the no car was ever parked on ith slot
            if i not in self.__slot_details.keys():
                continue
            slot = self.__slot_details[i]
            if not slot.is_empty():
                if slot.get_registration_no() == registration_no:
                    return slot.get_slot_number()

        return "Not found"

    # Get the details of filled slots in parking lot
    def get_status(self):
        result = []
        for i in range(1, self.__number_of_slots+1):
            # Case when the no car was ever parked on ith slot
            if i not in self.__slot_details.keys():
                continue
            slot = self.__slot_details[i]
            if not slot.is_empty():
                result.append((slot.get_slot_number(), slot.get_registration_no(), slot.get_colour()))

        return result

