def get_categories():
    # open the categories file
    categoriesFile = open("categories.txt", "w")

    nrOfCategories = int(input("Introduce the number of categories: "))

    # get the categories from the user and write them to the file
    for i in range(0, nrOfCategories):
        newCategory = input(f"Introduce the \"{i}\" category: ")
        categoriesFile.write(newCategory + '\n')

    # close the categories file
    categoriesFile.close()
    print("You've finished introducing the categories\n")

def get_tasks():
    # open the tasks file
    tasksFile = open("tasks.txt", "w")
    nrOfTasks = int(input("Introduce the number of tasks: "))

    # get the tasks and write them to the file
    for i in range(0, nrOfTasks):
        newTask = input(f"Introduce the \"{i}\" task: ")
        limitDate = input(f"Introduce a limit date for \"{newTask}\". ")
        accountablePerson = input(f"Introduce the accountable person for \"{newTask}\". ")
        invalidCategory = True
        while invalidCategory:
            taskCategory = input(f"Introduce the category \"{newTask}\" belongs to. ")

            with open("categories.txt", "r") as categoriesFile:
                for category in categoriesFile:
                    if category.strip().lower() == taskCategory.strip().lower():
                        tasksFile.write(
                            newTask.strip() + " " + limitDate.strip() + " " + accountablePerson.strip() + " " + taskCategory.strip() + '\n')
                        invalidCategory = False
                        break
    tasksFile.close()

def append_categories():
    # open the categories file
    categoriesFile = open("categories.txt", "a")

    nrOfCategories = int(input("Introduce the number of categories: "))

    # get the categories from the user and write them to the file
    for i in range(0, nrOfCategories):
        newCategory = input(f"Introduce the \"{i}\" category: ")
        categoriesFile.write(newCategory + '\n')

    # close the categories file
    categoriesFile.close()
    print("You've finished introducing the categories\n")

def append_tasks():
    # open the tasks file
    tasksFile = open("tasks.txt", "a")
    nrOfTasks = int(input("Introduce the number of tasks: "))

    # get the tasks and write them to the file
    for i in range(0, nrOfTasks):
        newTask = input(f"Introduce the \"{i}\" task: ")
        limitDate = input(f"Introduce a limit date for \"{newTask}\". ")
        accountablePerson = input(f"Introduce the accountable person for \"{newTask}\". ")
        invalidCategory = True
        while invalidCategory:
            taskCategory = input(f"Introduce the category \"{newTask}\" belongs to. ")

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
            with open ("tasks.txt", "r") as tasksFile:
                print(category.upper(), end = "")
                for task in tasksFile:
                    if (task.split(" ")[-1] == category):
                        print("  " + task)
def default():
    print("Please introduce a valid command, ! to append categories, @ to append tasks, # to view the data, and $ to end the program")

get_categories()
get_tasks()

commands = {
    "!": append_categories,
    "@": append_tasks,
    "#": list_data
}

print("Enter ! to append categories, @ to append tasks, # to view the data, and $ to end the program\n")
while True:
    user_input = input("Enter your next command: ")
    next_command = commands.get(user_input, default)
    next_command()

get_tasks()