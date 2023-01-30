# print command:

print('Test message')  # String format
print(1)  # Float format
print(1.1)  # Integer format

print(20 * 24 * 60)
print("20 days are " + str(20 * 24 * 60) + " minutes")
print(f"20 days are {20 * 24 * 60 * 60} seconds")

# Variables:

calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"

print(f"35 days are {35 * calculation_to_seconds} {name_of_unit}")
print(f"50 days are {50 * calculation_to_seconds} {name_of_unit}")
print(f"110 days are {110 * calculation_to_seconds} {name_of_unit}")


# Functions:


def days_to_units(days, message):
    print(f"{days} days are {days * calculation_to_seconds} {name_of_unit}")
    print(message)


days_to_units(500, "Hello!")
days_to_units(10, "Bye!")
days_to_units(1, "Hello again!")

# Scope:

# Global scope = variables available from within any scope.
# Local scope = variables created inside function.
