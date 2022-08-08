unit_conversion = 24
unit = "hours"

def days_to_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days * unit_conversion} {unit}")
    

def validate_and_execute():
    try:
        user_input_int = int(num_of_days_element)
        if user_input_int > 0:
                calculated_result = days_to_units(user_input_int)
                print (calculated_result)
        elif user_input_int == 0:
            print("Please, enter a valid positive number!")
        else:
            print ("Your input is not valid!")
    except ValueError:
        print("Your input is not valid!")


user_input = ""
while user_input != "exit":
    user_input = input ("Hello user, please... Insert a number of days and I will convert it to hours!\nAfter you finished your calculation enter 'exit' to finish the program: ")
    list_of_days = user_input.split(", ")

    for num_of_days_element in set(list_of_days):
        validate_and_execute()

