import sys
from classes.parking_lot import ParkingLot
from commands import *


def execute_command(parking_lot, command):
    if command[0] == "create_parking_lot":
        parking_lot = ParkingLot(int(command[1]))
        print("Created a parking lot with {0} slots".format(command[1]))
    elif command[0] == "park":
        park_new_car(parking_lot, command[1], command[2])
    elif command[0] == "leave":
        car_departure(parking_lot, int(command[1]))
    elif command[0] == "status":
        get_status(parking_lot)
    elif command[0] == "registration_numbers_for_cars_with_colour":
        get_registration_by_colour(parking_lot, command[1])
    elif command[0] == "slot_numbers_for_cars_with_colour":
        get_slot_by_colour(parking_lot, command[1])
    elif command[0] == "slot_number_for_registration_number":
        get_slot_by_registration(parking_lot, command[1])
    else:
        print('No such command')
    return parking_lot


def interactive_mode():
    parking_lot = None
    command = input().split()
    while not command[0] == 'exit':
        parking_lot = execute_command(parking_lot, command)
        command = input().split()


def file_read_mode(file_name):
    parking_lot = None
    with open(file_name) as file:
        commands = file.readlines()
        for command in commands:
            command = command.replace('\n', '').split(' ')
            parking_lot = execute_command(parking_lot, command)


def main():
    if len(sys.argv) > 1:
        file_read_mode(sys.argv[1])
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
