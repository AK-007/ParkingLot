def park_new_car(parking_lot, registration_no, colour):
    if parking_lot is None:
        return 'Parking lot not initialized'
    else:
        return parking_lot.park_new_car(registration_no, colour)


def car_departure(parking_lot, slot_number):
    if parking_lot is None:
        return 'Parking lot not initialized'
    # Case when slot_number is not present in the parking lot
    elif slot_number > parking_lot.get_parking_lot_size():
        return 'No such parking lot'
    else:
        return parking_lot.car_departure(slot_number)


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
        return 'Parking lot not initialized'
    res = parking_lot.registration_numbers_for_cars_with_colour(colour)
    if len(res) == 0:
        return "No {0} cars are parked".format(colour)
    else:
        return res


def get_slot_by_colour(parking_lot, colour):
    if parking_lot is None:
        return 'Parking lot not initialized'
    res = parking_lot.slot_numbers_for_cars_with_colour(colour)
    if len(res) == 0:
        return "No {0} cars are parked".format(colour)
    else:
        return res


def get_slot_by_registration(parking_lot, registration_no):
    if parking_lot is None:
        return 'Parking lot not initialized'
    else:
        return parking_lot.slot_number_for_registration_number(registration_no)
