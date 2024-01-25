from datetime import datetime
from colors import prompt_color, warning_color, info_color, input_color, Style

def is_valid_date(date_str):
    try:
        datetime_object = datetime.strptime(date_str, '%Y-%m-%d')  # Assuming the date format is 'YYYY-MM-DD'
        return True
    except ValueError:
        return False

def get_date():
    limitDate = input(f"{prompt_color}Introduce a date in the format YYYY-MM-DD: {Style.RESET_ALL}")
    while not is_valid_date(limitDate):
        limitDate = input(f"{warning_color} The date you introduced was not valid, please reintroduce it: {Style.RESET_ALL}")
    return limitDate

def is_valid_number(nr):
    try:
        int(nr)
        return True
    except ValueError:
        return False

def get_number(subject):
    nrOfCategories = input(f"{prompt_color}Introduce the number of {subject}: {Style.RESET_ALL}")
    while not is_valid_number(nrOfCategories):
        nrOfCategories = input(f"{warning_color}Your input is invalid, please try reintroducing a number: {Style.RESET_ALL}")
    return int(nrOfCategories)