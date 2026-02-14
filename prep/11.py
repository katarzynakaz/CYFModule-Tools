# exercise
# Write a program which:

# Already has a list of Laptops that a library has to lend out.
# Accepts user input to create a new Person - it should use the input 
# function to read a person’s name, age, and preferred operating system.
# Tells the user how many laptops the library has that have that 
# operating system.
# If there is an operating system that has more laptops available, 
# tells the user that if they’re willing to accept that operating 
# system they’re more likely to get a laptop.
# You should convert the age and preferred operating system input from 
# the user into more constrained types as quickly as possible, and 
# should output errors to stderr and terminate 
# the program with a non-zero exit code if the user input bad values.

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