# Binary Search Algorithm
# Create a list of random numbers between 0 and 100,
# with every succeeding numbers having a difference of 2 between them.

# When the user inputs a random number, the program will check if that number is included in the list.

# It will do so by creating two halves of the list. If the program finds the number in the first half of the list,
# it will eliminate the other half and vice versa.

# The search will continue until the program finds the number input of the user or until the subarray size becomes 0
# (this means that the number is not in the list).

# TODO (by me): Extra: Make the numbers within the list unique.

import random 


def generate_random_number():
    """Generates a random number between 0 and 100."""
    return random.randint(0, 100)


# Extra
def replace_number_at(position, new_number, numbers_list):
    """Replaces the @new_number in @numbers_list at position @position."""
    numbers_list[position] = new_number

    return numbers_list


# Extra
def is_number_repeated(number, gen_list):
    """Checks if a number repeats within the list."""
    return gen_list.count(number) > 1


def generate_list_of_random_numbers():
    """Generates the list of random numbers."""
    random_numbers = []
    for _ in range(random.randint(10, 25)):
        num = generate_random_number()
        random_numbers.append(num)
    
    return random_numbers


# Extra
def get_unique_number(i, numbers_list):
    """Returns a unique number in the list of numbers."""
    if not is_number_repeated(numbers_list[i], numbers_list):
        return numbers_list[i]

    new_number = numbers_list[i]

    while is_number_repeated(new_number, numbers_list):
        new_number = generate_random_number()

        numbers_list = replace_number_at(i, new_number, numbers_list)

    return new_number


# Extra
def get_list_of_unique_numbers(initial_generated_list):
    """Returns the final list with each number unique."""
    list_of_unique_numbers = initial_generated_list

    for i in range(len(list_of_unique_numbers)):
        list_of_unique_numbers = replace_number_at(i, get_unique_number(i, list_of_unique_numbers),
                                                   list_of_unique_numbers)

    return list_of_unique_numbers


# Extra
def generate_unique_numbers_list():
    """Generates the list with each number unique"""
    initial_generated_list = generate_list_of_random_numbers()

    return get_list_of_unique_numbers(initial_generated_list)
        

def difference_between_2_succeeding_numbers_is_less_than_2(pos, list_of_numbers):
    """Returns True if the difference between 2 succeeding numbers is less than 2."""
    return -2 < list_of_numbers[pos] - list_of_numbers[pos + 1] < 2


def generate_final_list():
    """Returns the list with a new random number if the difference between 2 succeeding numbers is less than 2."""
    generated_list = generate_unique_numbers_list()
    for i in range(len(generated_list) - 1):
        if difference_between_2_succeeding_numbers_is_less_than_2(i, generated_list):
            new_number = generate_random_number()
            generated_list[i + 1] = new_number
    
    return generated_list


def divide_the_final_list_in_two_halves():
    """Divides the final list in two halves."""
    divided_list = []
    final_list = generate_final_list()

    first_half = final_list[round((len(final_list))/2):]
    second_half = final_list[:round((len(final_list))/2)]

    divided_list.append(first_half)
    divided_list.append(second_half)
    
    return divided_list


def is_user_number_included_in_sublist(user_input, sublist):
    """Checks if the number guessed by the user is included in the sublist."""
    return user_input in sublist
    

def main():
    user_number = int(input("Type a number between 0 and 100: "))

    print("Final generated list will be printed below.")
    divided_list = divide_the_final_list_in_two_halves()
    print(divided_list)

    print("\nFirst half of the list will be printed below.")
    first_half = divided_list[0]
    print(first_half)

    print("\nSecond half half of the list will be printed below.")
    second_half = divided_list[1]
    print(second_half)

    if is_user_number_included_in_sublist(user_number, first_half):  
        second_half.clear()
        print(f"The number chosen by the user, {user_number}, was found in the first half of the list.")
        print(divided_list)
    elif is_user_number_included_in_sublist(user_number, second_half):  
        first_half.clear()
        print(f"The number chosen by the user, {user_number}, was found in the second half of the list.")
        print(divided_list)
    else:
        return f"\nThe number {user_number} you entered wasn't found in the list."
    

print(main())



