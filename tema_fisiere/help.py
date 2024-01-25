from colors import *

def help(command):
    if command == '!':
        print(f"{info_color}Add new categories")
        return
    elif command == '@':
        print(f"{info_color}Add new tasks")
        return
    elif command == '#':
        print(f"{info_color}View the entered data")
        return
    elif command == '$':
        print(f"{info_color}Quit the program")
        return
    elif command == '%':
        print(f"{info_color}View the entered data sorted alphabetically by the category")
        return
    print(f"{info_color}help [command_name] to see detailed information on the commands")