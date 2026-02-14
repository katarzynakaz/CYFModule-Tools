from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
import sys

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


#add new person with preferences
def create_a_new_person() -> Person:
    add_name = input("What is your name? \n").title()
    if not add_name or add_name == "" or len(add_name) > 50:
        print("Enter a valid name.", file=sys.stderr)
        sys.exit(1)

    add_age = int(input("What is your age? \n"))
    if add_age < 0 or add_age > 100:
        print("Enter a valid age.", file=sys.stderr)
        sys.exit(1)

    #get strings to rank
    print("Select your 3 favourite operating systems. Type 'macOS', 'Arch Linux' or 'Ubuntu'.")
    os1_str = input("What is your fav os?: \n")
    os2_str = input("What is your second fav os?: \n")
    os3_str = input("What is your third fav os?: \n")

    #chamnge here to enums by using constructor from enums os
    # choice1 = OperatingSystem(os1_str)
    # choice2 = OperatingSystem(os2_str)
    # choice3 = OperatingSystem(os3_str)
    # user_oss_ranked_as_enums = [choice1, choice2, choice3]
    # or shorter
    #here i have strings converted to enums so can compare
    user_oss_ranked_as_enums = [
        OperatingSystem(os1_str),
        OperatingSystem(os2_str),
        OperatingSystem(os3_str)
    ]

    # grab by value of enum str not whole obj like compared in logic[0]
    print(
        f"Hi {add_name}, your choices were saved and your favourite os is {user_oss_ranked_as_enums[0].value}")

    return Person(name=add_name, age=add_age, preferred_operating_system=user_oss_ranked_as_enums)


laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

#here i need to refactor i was changing logic from coursework
#return laptop obj and happiness value
def link_laptops_and_happiness(laptops: List[Laptop], person: Person):

    for laptop in laptops:
        #to comapre to if selected fav sanes 0 = first choice
        if laptop.operating_system == person.preferred_operating_system[0]:
            return laptop, 0

    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system[1]:
            return laptop, 1

    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system[2]:
            return laptop, 2

    #in case laptop not on list
    non_existent_laptop = Laptop(
        id=100,
        manufacturer="Does not exist",
        model="no laptop",
        screen_size_in_inches=0.0,
        operating_system=OperatingSystem.MACOS
    )
    return non_existent_laptop, 100

#this is to sort people
def compare_count_of_choices_and_os(person: Person, available_laptops: List[Laptop]) -> int:
    #from enum for fav
    fav = person.preferred_operating_system[0]

    count_of_available = 0
    for laptop in available_laptops:
        if laptop.operating_system == fav:
            count_of_available += 1

    return count_of_available


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    print(f"Welcome to the laptop allocator")

    #store final
    students_with_laptops_assigned = {}
    available_laptops = list(laptops)

    #minimise unhappiness so ones with least available laptops go first
    people.sort(key=lambda p: compare_count_of_choices_and_os(p, available_laptops))

    for person_being_checked in people:

        laptop, sadness = link_laptops_and_happiness(available_laptops, person_being_checked)
        #non listed os
        if laptop.id !=100:
            students_with_laptops_assigned[person_being_checked] = laptop
            #remove from available to allocate
            available_laptops.remove(laptop)
            print(f"Allocated {laptop.model} to {person_being_checked.name} with a sadness score of {sadness}.")
        else:
            #if no laptop on list give them popped one
            remaining = available_laptops.pop(0)
            students_with_laptops_assigned[person_being_checked] = remaining
            print(f"Allocated non-matching {remaining.model} to {person_being_checked.name} with a sadness score of 100)")

    return students_with_laptops_assigned



def main():
    # add people
    people = []
    for i in range(4):
        people.append(create_a_new_person())

    final_dict = allocate_laptops(people, laptops)

    print("All people have been assigned laptops.")

main()