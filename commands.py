def park_new_car(parking_lot, registration_no, colour):
    if parking_lot is None:
        print('Parking lot not initialized')
    else:
        print(parking_lot.park_new_car(registration_no, colour))


def car_departure(parking_lot, slot_number):
    if parking_lot is None:
        print('Parking lot not initialized')
    elif slot_number > parking_lot.get_parking_lot_size():
        print('No such parking lot')
    else:
        print(parking_lot.car_departure(slot_number))


def get_status(parking_lot):
    if parking_lot is None:
        print('Parking lot not initialized')
        return
    res = parking_lot.get_status()
    print("Slot No.    Registration No    Colour")
    for s, r, c in res:
        print("{:<12}{:<19}{}".format(s, r, c))


def get_registration_by_colour(parking_lot, colour):
    if parking_lot is None:
        print('Parking lot not initialized')
        return
    res = parking_lot.registration_numbers_for_cars_with_colour(colour)
    if len(res) == 0:
        print("No {0} cars are parked".format(colour))
    else:
        print(*res, sep=', ')


def get_slot_by_colour(parking_lot, colour):
    if parking_lot is None:
        print('Parking lot not initialized')
        return
    res = parking_lot.slot_numbers_for_cars_with_colour(colour)
    if len(res) == 0:
        print("No {0} cars are parked".format(colour))
    else:
        print(*res, sep=', ')


def get_slot_by_registration(parking_lot, registration_no):
    if parking_lot is None:
        print('Parking lot not initialized')
    else:
        print(parking_lot.slot_number_for_registration_number(registration_no))
