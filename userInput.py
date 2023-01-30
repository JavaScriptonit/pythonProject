calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(days):
    return f"{days} days are {int(days) * calculation_to_units} {name_of_unit}"


user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
calculated_value = days_to_units(user_input)
print(calculated_value)
