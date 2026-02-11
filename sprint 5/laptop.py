
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
    name = input("What is your name?: \n")
    fav_os = int(input("What is your fav os?: \n"))
    second_fav_os = int(input("What is your second fav os?: \n"))

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

