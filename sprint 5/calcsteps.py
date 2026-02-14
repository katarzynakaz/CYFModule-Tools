# from art import logo

# def add(n1, n2):
#     return n1 + n2

# def multiply(n1, n2):
#     return n1 * n2

# def subtract(n1, n2):
#     return n1 - n2

# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# # print(operations["*"](4,8))

# def perform_first_calc():
#     first_number = int(input("What's your first number?: \n"))
#     for key in operations:
#         print(key)
#     choose_operation = input("Pick an operation. Use only '+', '-', '*' or '/': \n")
#     second_number = int(input("What's your second number?: \n"))
#     if choose_operation in operations:
#         first_calc_result = operations[choose_operation](first_number, second_number)
#         print(f"{first_number} {choose_operation} {second_number} = {first_calc_result}")
#         # return first_calc_result
#     else:
#         print("Invalid operator. Try again.")
# # def perform_second_calc():

#     choice = input("Do you want to continue with the result? y/n: \n").lower()
#     if choice == "y":
#         first_number = first_calc_result
#         choose_operation = input("Pick an operation. Use only '+', '-', '*' or '/': \n")
#         second_number = int(input("What's your second number?: \n"))

#         if choose_operation in operations:
#             second_calc_result = operations[choose_operation](first_number, second_number)
#             print(f"{first_number} {choose_operation} {second_number} = {second_calc_result}")
#     elif choice == "n":
#         print("Bye")

# # def main():
# #     outcome_of_first_calc = perform_first_calc()
# #     perform_second_calc(outcome_of_first_calc)
# # main()

# perform_first_calc()


# now i wanna put in a loop
from art import logo

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(operations["*"](4,8))

def perform_first_calc():
    first_number = int(input("What's your first number?: \n"))
    for key in operations:
        print(key)
    choose_operation = input("Pick an operation. Use only '+', '-', '*' or '/': \n")
    second_number = int(input("What's your second number?: \n"))
    if choose_operation in operations:
        first_calc_result = operations[choose_operation](first_number, second_number)
        print(f"{first_number} {choose_operation} {second_number} = {first_calc_result}")
        # return first_calc_result
    else:
        print("Invalid operator. Try again.")
# def perform_second_calc():

    choice = input("Do you want to continue with the result? y/n: \n").lower()
    if choice == "y":
        first_number = first_calc_result
        choose_operation = input("Pick an operation. Use only '+', '-', '*' or '/': \n")
        second_number = int(input("What's your second number?: \n"))

        if choose_operation in operations:
            second_calc_result = operations[choose_operation](first_number, second_number)
            print(f"{first_number} {choose_operation} {second_number} = {second_calc_result}")
    elif choice == "n":
        print("Bye")

# def main():
#     outcome_of_first_calc = perform_first_calc()
#     perform_second_calc(outcome_of_first_calc)
# main()

perform_first_calc()