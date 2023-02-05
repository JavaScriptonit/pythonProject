calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(days):
    return f"{days} days are {days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number!")
    else:
        print("Your input is not a valid number. Please enter a valid positive number!")


user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
validate_and_execute()
