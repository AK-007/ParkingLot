import unittest
from commands import *
from classes.parking_lot import ParkingLot


class ParkingLotUnitTest(unittest.TestCase):
    def test_parking_lot_creation(self):
        parking_lot = ParkingLot(15)
        self.assertEqual(parking_lot.__number_of_slots, 15)

    def test_parking_lot_initialized(self):
        res = park_new_car(None, "KA-01-P-333", "White")
        self.assertEqual(res, 'Parking lot not initialized')
        res2 = car_departure(None, 3)
        self.assertEqual(res2, 'Parking lot not initialized')

    def test_parking_lot_full(self):
        parking_lot = ParkingLot(1)
        res = park_new_car(parking_lot, "KA-01-P-333", "White")
        res2 = park_new_car(parking_lot, "KA-01-P-344", "Black")
        self.assertEqual(res2, 'Sorry, parking lot is full')

    def test_parking_allocated(self):
        parking_lot = ParkingLot(1)
        res = park_new_car(parking_lot, "KA-01-P-333", "White")
        self.assertEqual(res, 'Allocated slot number: 1')
        res2 = get_slot_by_registration(parking_lot, "KA-01-P-333")
        self.assertEqual(res2, 1)

    def test_incorrect_slot_departure(self):
        parking_lot = ParkingLot(3)
        res = car_departure(parking_lot, 4)
        self.assertEqual(res, 'No such parking lot')

    def test_empty_slot_departure(self):
        parking_lot = ParkingLot(3)
        res = car_departure(parking_lot, 2)
        self.assertEqual(res, 'Slot number 2 is already empty')

    def test_successful_departure(self):
        parking_lot = ParkingLot(3)
        r = park_new_car(parking_lot, "KA-01-P-333", "White")
        res = car_departure(parking_lot, 1)
        self.assertEqual(res, 'Slot number 1 is free')
        self.assertEqual(parking_lot.__slot_details[1].is_empty(), True)

    def test_get_registration_by_colour(self):
        parking_lot = ParkingLot(4)
        p1 = park_new_car(parking_lot, "KA-01-P-533", "White")
        p2 = park_new_car(parking_lot, "AD-21-P-313", "Black")
        p3 = park_new_car(parking_lot, "PA-01-P-433", "Black")
        res = get_registration_by_colour(parking_lot, "Black")
        self.assertEqual(res, "AD-21-P-313, PA-01-P-433")
        res2 = get_registration_by_colour(parking_lot, "Green")
        self.assertEqual(res2, "No Green cars are parked")

    def test_get_slot_by_colour(self):
        parking_lot = ParkingLot(4)
        p1 = park_new_car(parking_lot, "KA-01-P-533", "White")
        p2 = park_new_car(parking_lot, "AD-21-P-313", "Black")
        p3 = park_new_car(parking_lot, "PA-01-P-433", "Black")
        res = get_slot_by_colour(parking_lot, "White")
        self.assertEqual(res, '1')
        res2 = get_slot_by_colour(parking_lot, "Green")
        self.assertEqual(res2, "No Green cars are parked")

    def test_get_slot_by_registration(self):
        parking_lot = ParkingLot(4)
        p1 = park_new_car(parking_lot, "KA-01-P-533", "White")
        p2 = park_new_car(parking_lot, "AD-21-P-313", "Black")
        p3 = park_new_car(parking_lot, "PA-01-P-433", "Black")
        res = get_slot_by_registration(parking_lot, "AD-21-P-313")
        self.assertEqual(res, 2)
        res2 = get_slot_by_registration(parking_lot, "QA-11-W-444")
        self.assertEqual(res2, "Not found")


if __name__ == '__main__':
    unittest.main()
