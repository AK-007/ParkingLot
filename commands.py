def park_new_car(parking_lot, registration_no, colour):
    print(parking_lot.park_new_car(registration_no, colour))


def car_departure(parking_lot, slot_number):
    print(parking_lot.car_departure(slot_number))


def get_status(parking_lot):
    res = parking_lot.get_status()
    print("Slot No.    Registration No    Colour")
    for s, r, c in res:
        print("{:<12}{:<19}{}".format(s, r, c))


def get_registration_by_colour(parking_lot, colour):
    res = parking_lot.registration_numbers_for_cars_with_colour(colour)
    if len(res) == 0:
        print("No {0} cars are parked".format(colour))
    else:
        print(*res, sep=', ')


def get_slot_by_colour(parking_lot, colour):
    res = parking_lot.slot_numbers_for_cars_with_colour(colour)
    if len(res) == 0:
        print("No {0} cars are parked".format(colour))
    else:
        print(*res, sep=', ')


def get_slot_by_registration(parking_lot, registration_no):
    print(parking_lot.slot_number_for_registration_number(registration_no))
