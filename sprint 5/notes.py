# Play computer with this code. Predict what you expect each line will do.
#  Then run the code and check your predictions. (If any lines cause 
#  errors, you may need to comment them out to check later lines).

class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"

person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name()) # prints Elizaveta Alekseeva
print(person1.get_full_name()) # prints Elizaveta Alekseeva
person1.change_last_name("Tyurina") # no print
print(person1.get_name()) # prints Elizaveta Tyurina
print(person1.get_full_name()) # prints Elizaveta Tyurina (née Alekseeva)

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name()) #print Elizaveta Alekseeva
print(person2.get_full_name()) #no full name method
person2.change_last_name("Tyurina") #no change last name method
print(person2.get_name()) # print Elizaveta Alekseeva
print(person2.get_full_name()) #no full name method so err


from dataclasses import dataclass
from enum import Enum
from typing import List
from collections import Counter
import sys

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

def create_a_new_person() -> Person:
    add_name = input("What is your name? \n")
    if not add_name or add_name == "" or len(add_name) > 50:
        print("Enter a valid name.", file=sys.stderr)
        sys.exit(1)

    add_age = int(input("What is your age? \n"))
    if add_age < 0 or add_age > 100:
        print("Enter a valid age.", file=sys.stderr)
        sys.exit(1)

    add_os = input("What is your preferred operating system? \n")

    if add_os not in [os.value for os in OperatingSystem]:
        print("Enter a valid operating system.", file=sys.stderr)
        sys.exit(1)

    return Person(name=add_name, age=add_age, preferred_operating_system=OperatingSystem(add_os))


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    other_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
        else:
            other_laptops.append(laptop)
    return possible_laptops, other_laptops

def compare_counts_of_poss_and_others(possible_laptops: List[Laptop], other_laptops: List[Laptop], person: Person) -> None:
    # counter to get obj
    other_laptops_counted_as_obj = Counter(laptop.operating_system for laptop in other_laptops)
    # and here turn to tuple os+count
    most_common_laptop = other_laptops_counted_as_obj.most_common(1)[0]

    if len(possible_laptops) < most_common_laptop[1]:
        # print(f"There are more laptops available with {str(most_common_laptop[0])} than your preferred OS {person.preferred_operating_system.value}. Consider accepting that OS to increase your chances of getting a laptop.")
        print(f"There are more laptops available with {most_common_laptop[0].value} than your preferred OS {person.preferred_operating_system.value}. Consider accepting that OS to increase your chances of getting a laptop.")
    elif len(possible_laptops) == most_common_laptop[1]:
        print("Your chosen os has the same availability as the most common other os.")s
    else:
        print("Your chosen os has the biggest availability.")

people = [
    # Person(name="Imran", age=22, preferred_operating_system=OperatingSystem.UBUNTU),
    # Person(name="Eliza", age=34, preferred_operating_system=OperatingSystem.ARCH),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {possible_laptops}")


def execute():
    new_person = create_a_new_person()
    possible_laptops, other_laptops = find_possible_laptops(laptops, new_person)
    print(f"Number of laptops matching your preferred OS: {len(possible_laptops)}")
    compare_counts_of_poss_and_others(possible_laptops, other_laptops, new_person)


execute()



In the prep, there was an exercise around finding possible laptops for a group of people.

Your exercise is to extend this to actually allocate laptops to the people.

Given these class definitions:

from dataclasses import dataclass
from enum import Enum
from typing import List

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_system: List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem
Write a function with this signature:

def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
Every person should be allocated exactly one laptop.

If we define "sadness" as the number of places down in someone's ranking the operating system 
the ended up with (i.e. if your preferences were [UBUNTU, ARCH, MACOS] and you were allocated 
a MACOS machine your sadness would be 2), we want to minimise the total sadness of all people. 
If we allocate someone a laptop with an operating system not in their preferred list, treat 
them as having a sadness of 100.

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = "Exceeds expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

to access

order = {
    "starter" : {1: "soup", 2: "salad"},
    "main" : {1: ["steak", "pasta"], 2: ["fish"]},
    "dessert" : {1: ["ice cream"], 2: []},
    "drink" : []
}
print(order["main"][1][0]) #steak
print(order["dessert"][2])  #[]
print(order["starter"][2])  #salad

order2 = [
    {1: "soup", 2: "salad"},
    {1: ["steak", "pasta"], 2: ["fish"]},
    {1: ["ice cream"], 2: []},
    "drink"
]
print(order2[1][1][0]) #steak
print(order2[2][2])  #[]
print(order2[0][2])  #salad

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
print(cars)
cars.sort(key=myFunc, reverse=True)
print(cars)
# cars.sort(key=myFunc)
# print(cars)

def sorting_func(sortedby):
    return sortedby['bid']


here  we place fuctions as values in a dict
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

print(operations["*"](4,8))
to access specific one we suse thw argument as param for specific key

def perform_first_calc():
    first_number = int(input("What's your first number?: \n"))
    choose_operation = input("Pick an operation. Use only '+', '-', '*' or '/': \n")
    second_number = int(input("What's your second number?: \n"))
    if choose_operation in operations:
        result = operations[choose_operation](first_number, second_number)
        print(f"{first_number} {choose_operation} {second_number} = {result}")
        return result

    else:
        print("Invalid operator. Try again.")

perform_first_calc()


# from dataclasses import dataclass
# from enum import Enum
# from typing import List

# class OperatingSystem(Enum):
#     MACOS = "macOS"
#     ARCH = "Arch Linux"
#     UBUNTU = "Ubuntu"

# @dataclass(frozen=True)
# class Person:
#     name: str
#     age: int
#     # Sorted in order of preference, most preferred is first.
#     preferred_operating_system: List[OperatingSystem]


# @dataclass(frozen=True)
# class Laptop:
#     id: int
#     manufacturer: str
#     model: str
#     screen_size_in_inches: float
#     operating_system: OperatingSystem

# def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
#     possible_laptops = []
#     other_laptops = []
#     for laptop in laptops:
#         if laptop.operating_system == person.preferred_operating_system:
#             possible_laptops.append(laptop)
#         else:
#             other_laptops.append(laptop)
#     return possible_laptops, other_laptops


# def compare_counts_of_poss_and_others(possible_laptops: List[Laptop], other_laptops: List[Laptop], person: Person) -> None:
#     # counter to get obj
#     other_laptops_counted_as_obj = Counter(laptop.operating_system for laptop in other_laptops)
#     # and here turn to tuple os+count
#     most_common_laptop = other_laptops_counted_as_obj.most_common(1)[0]

#     if len(possible_laptops) < most_common_laptop[1]:
#         # print(f"There are more laptops available with {str(most_common_laptop[0])} than your preferred OS {person.preferred_operating_system.value}. Consider accepting that OS to increase your chances of getting a laptop.")
#         print(f"There are more laptops available with {most_common_laptop[0].value} than your preferred OS {person.preferred_operating_system.value}. Consider accepting that OS to increase your chances of getting a laptop.")
#     elif len(possible_laptops) == most_common_laptop[1]:
#         print("Your chosen os has the same availability as the most common other os.")s
#     else:
#         print("Your chosen os has the biggest availability.")

# def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
# #allocate 1 laptop
# people_given_laptop = []
# sadness = 0

# for person in people:
#     possible_laptops, other_laptops = find_possible_laptops(laptops, person)
#     people_given_laptop.append(person.name + " given laptop " + possible_laptops[0].model)
#     laptops.remove(possible_laptops[0])
# # if not preferred sanness 100
# #if preferrred sadness 0
# if os in possible_laptops:
#     sadmness += 0
# else:    
#     sadness += 100


# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score >= 91:
#         student_grades[student] = 'Outstanding'
#     elif score >= 81:
#         student_grades[student] = "Exceeds expectations"
#     elif score >= 71:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"


# preferrred_laptops = {
#     # 'person': 'os'
# }

# people_with_a_laptop_and_score = {}

# def allocate():
#     for person in people:
#     preferred = Person.preferred_operating_system
#     if preferred in possible_laptops:
#         people_with_a_laptop_and_score[person] = 0

#     else:
#         people_with_a_laptop_and_score[person] = 100
    
#     return people_with_a_laptop_and_score


# people_with_a_laptop_and_score = {
#   "person1": {
#     "allocated": "osversion",
#     "happiness_scor": 100
#    },
#     "person2": {
#     "allocated": "osversion",
#     "happiness_score": 0
#    },
# }
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary




print(f"Welcome to the laptop allocator")
users_with_favs_os = []

# was og {} and below
# users_with_favs_os[name] = bid because changed {} to []


def gather_info_from_users():
    name = input("What is your name?: \n").title()
    fav_os = input("What is your fav os?: \n")
    second_fav_os = input("What is your second fav os?: \n")

    if name == "" or fav_os == "" or second_fav_os == "" or len(name) > 50:
        print("Please enter valid input", file=sys.stderr)
        sys.exit(1)
    
    if fav_os not in OperatingSystem.value or second_fav_os not in OperatingSystem.value:
        print("Please enter a valid operating system", file=sys.stderr)
        sys.exit(1)


    each_entry = {"name": name, "fav os": fav_os, "second fav os": second_fav_os}
    users_with_favs_os.append(each_entry)

    return users_with_favs_os

# so i am building a dict
# users_with_favs_os = [
#     {'Name': 'name', 'fav os': 0, 'second fav os': 0},
# ]


def check_if_we_have_more_users():
    while True:
        choice = input("Any more users? y/n \n")

        if choice == "y":
            print("\n" * 20)
            gather_info_from_users()
        elif choice == "n":
            print("Users input complete")
            return False
        else:
            print("Please type y or n")

# def sort_by_fav_os(entry):
#     return

def allocated_laptop(users_with_favs_os, people):
    for entry in users_with_favs_os:
        if users_with_fav_os[0]["fav os"] = person.preferred_operating_system
        users_with_fav_os[0]["allocated" = person.preferred_operating_system]
    # users_with_favs_os.sort(key=sort_by_fav_os)
    print(users_with_favs_os)

def main():
    gather_info_from_users()
    check_if_we_have_more_users()
    print(users_with_favs_os)
    # sort_and_announce_winner()

main()

