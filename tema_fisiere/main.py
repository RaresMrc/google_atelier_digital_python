from validation import *
from colors import *
from help import *
from functools import partial

init(autoreset = True)

prompt_color = Fore.BLUE
info_color = Fore.GREEN
warning_color = Fore.RED
input_color = Fore.LIGHTWHITE_EX

globals = {
    "nrOfCategories": 0,
    "categoriesFile": "categories.txt",
    "tasksFile": "tasks.txt",
}

def get_categories():
    # open the categories file
    categoriesFile = open("categories.txt", "w")

    nrOfCategories = get_number("categories")

    # get the categories from the user and write them to the file
    for i in range(0, nrOfCategories):
        newCategory = input(f"{prompt_color}Introduce the name for the \"{i + 1}\" category: {Style.RESET_ALL}")
        categoriesFile.write(newCategory + '\n')

    # close the categories file
    categoriesFile.close()
    print(f"{info_color}You've finished introducing the categories.\n")
    return nrOfCategories

def get_tasks():
    # open the tasks file
    tasksFile = open("tasks.txt", "w")
    nrOfTasks = get_number("tasks")

    # get the tasks and write them to the file
    for i in range(0, nrOfTasks):
        newTask = input(f"{prompt_color}Introduce the \"{i + 1}\" task: {Style.RESET_ALL}")
        limitDate = get_date()
        accountablePerson = input(f"{prompt_color}Introduce the accountable person for \"{newTask}\". {Style.RESET_ALL}")

        invalidCategory = True
        temp_color = prompt_color
        while invalidCategory:
            taskCategory = input(f"{temp_color}Introduce the category \"{newTask}\" belongs to: {Style.RESET_ALL}")
            temp_color = warning_color

            with open("categories.txt", "r") as categoriesFile:
                for category in categoriesFile:
                    if category.strip().lower() == taskCategory.strip().lower():
                        tasksFile.write(
                            newTask.strip() + " " + limitDate.strip() + " " + accountablePerson.strip() + " " + taskCategory.strip() + '\n')
                        invalidCategory = False
                        break
    tasksFile.close()

globals.__setitem__("nrOfCategories", get_categories())
if globals.__getitem__("nrOfCategories") != 0:
    get_tasks()

def append_categories():
    # open the categories file
    categoriesFile = open("categories.txt", "a")

    nrOfCategories = get_number("categories")

    # get the categories from the user and write them to the file
    for i in range(0, nrOfCategories):
        newCategory = input(f"{prompt_color}Introduce the \"{i + 1}\" category: {Style.RESET_ALL}")
        categoriesFile.write(newCategory + '\n')

    globals.__setitem__("nrOfCategories", globals.get("nrOfCategories") + nrOfCategories)
    # close the categories file
    categoriesFile.close()
    print(f"{info_color}You've finished introducing the categories\n {Style.RESET_ALL}")

def append_tasks():
    if globals.get("nrOfCategories") == 0:
        print(f"{warning_color}There are no categories. Please introduce some categories first.")
        return
    # open the tasks file
    tasksFile = open("tasks.txt", "a")
    nrOfTasks = get_number("tasks")

    # get the tasks and write them to the file
    for i in range(0, nrOfTasks):
        newTask = input(f"{prompt_color}Introduce the \"{i + 1}\" task: {Style.RESET_ALL}")
        limitDate = get_date()
        accountablePerson = input(f"{prompt_color}Introduce the accountable person for \"{newTask}\". {Style.RESET_ALL}")
        invalidCategory = True

        temp_color = prompt_color
        while invalidCategory:
            taskCategory = input(f"{temp_color}Introduce the category \"{newTask}\" belongs to: {Style.RESET_ALL}")
            temp_color = warning_color

            with open("categories.txt", "r") as categoriesFile:
                for category in categoriesFile:
                    if category.strip().lower() == taskCategory.strip().lower():
                        tasksFile.write(
                            newTask.strip() + " " + limitDate.strip() + " " + accountablePerson.strip() + " " + taskCategory.strip() + '\n')
                        invalidCategory = False
                        break
    tasksFile.close()

def list_data():
    with open("categories.txt", "r") as categoriesFile:
        for category in categoriesFile:
            with open("tasks.txt", "r") as tasksFile:
                print(info_color + category.upper(), end = "")
                for task in tasksFile:
                    if (task.split(" ")[-1] == category):
                        print(info_color + "  " + task)

def sort_by_category():
    categories = list()
    with open("categories.txt", "r") as categoriesFile:
        for category in categoriesFile:
            categories.append(category)
    categories.sort()
    for category in categories:
        with open("tasks.txt", "r") as tasksFile:
            print(info_color + category.upper(), end="")
            for task in tasksFile:
                if (task.split(" ")[-1] == category):
                    print(info_color + "  " + task)
def quit_program():
    with open(globals.get("tasksFile"), "w"):
        pass
    with open(globals.get("categoriesFile"), "w"):
        pass
    exit(0)

def default():
    print(f"{warning_color}Please introduce a valid command, ! to append categories, @ to append tasks, # to view the data,"
          f"% to view the data sorted by category, and $ to end the program{Style.RESET_ALL}")


commands = {
    "!": append_categories,
    "@": append_tasks,
    "#": list_data,
    "$": quit_program,
    "%": sort_by_category,
    "help": partial(help, ""),
}

help_commands = {f"help {command}": partial(help, command) for command in commands}
commands.update(help_commands)

print(prompt_color + "Enter ! to append categories, @ to append tasks, # to view the data,"
                     "% to view the data sorted by category, help to view more detailed information, and $ to end the program\n")
while True:
    user_input = input(f"{prompt_color}Enter your next command: ")
    next_command = commands.get(user_input, default)
    next_command()
