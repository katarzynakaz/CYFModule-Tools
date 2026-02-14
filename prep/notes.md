
def how_many_laptops_match_os(person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    prinet(f"Number of laptops matching your preferred OS: {len(possible_laptops)}")
    return possible_laptops


def get_counts_of_all_laptops_by_os(laptops: List[laptop]) -> dict:
    number_of_laptops = {}

    for laptop in laptops:
        particular_os = laptop.operating_system
        
        if particular_os in number_of_laptops:
            number_of_laptops[particular_os] += 1
        else:
            number_of_laptops[particular_os] = 1
            
    return number_of_laptops

def check_if_there_is_os_with_more_laptops(laptops: List[Laptop], person: Person, possible_laptops: List[Laptop]) -> None:
    not_matching_laptop_counts = get_counts_of_all_laptops_by_os(laptops)


    for laptop in get_counts_of_all_laptops_by_os(laptops):
        if laptop.operating_system != person.preferred_operating_system:
            not_matching_laptop_counts = get_counts_of_all_laptops_by_os(laptops)
    print(f"There are more laptops available with {laptop.operating_system.value} than your preferred OS {person.preferred_operating_system.value}. Consider accepting that OS to increase your chances of getting a laptop.")
