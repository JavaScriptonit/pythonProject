calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(days):  # create a message for a user with calculations of hours in "n" days
    return f"{days} days are {days * calculation_to_units} {name_of_unit}"


def validate_and_execute():  # function to check the input with a correct number and throw Error messages to a user if it's not correct
    try:
        # can use "try/except" instead of "if user_input.isdigit():"
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number!")
        else:
            print("You entered a negative number, no conversation for you!")
    except ValueError:
        # "except ValueError:" instead of "else:"
        print("Your input is not a valid number. Please enter a valid positive number!")


user_input = ""
while user_input != "exit":  # while loop stops only when user_input == "exit"
    user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")  # welcome message for a user
    validate_and_execute()  # run validate_and_execute() function