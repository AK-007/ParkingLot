import sys


def execute_command(command):
    print(command)


def interactive_mode():
    command = input().split()
    while not command[0] == 'exit':
        execute_command(command)
        command = input().split()


def file_read_mode(file_name):
    with open(file_name) as file:
        commands = file.readlines()
        for command in commands:
            command.replace('\n', '').split()
            execute_command(command)


def main():
    if len(sys.argv) > 1:
        file_read_mode(sys.argv[1])
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
