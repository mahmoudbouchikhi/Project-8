# -*- coding: utf-8 -*-
"""
Description: Programming Assignment #4 - Processing Lists in Functions

Course: CSC119
Name:Mahmoud Bouchikhi

Design:

    Description: This program will Process different tasks
                 on a list that the user will choose.

    Input:        Get a list of from user

    Processing:   Convert list to integers

    Output:       Display list to user and main menu to choose tasks

    Input:        Get Menu selection from user

    Processing:   Depend on the task selected by user, program execute
                  the function in subject

    output:       print the result of the function related to task
                  selected by user

    Test Cases:   case 1: input 1,2,3,4,6,9,28 and expect my list in the
                  first output to look like [1,2,3,4,6,9,28]
                PASS
                  case 2: select number 4 from the menu to Check if the list
                  is sorted in increasing order and expect to get True
                PASS
                  case 3: select number 6 to Remove the middle element if
                          the list length is odd, or the middle two,
                          if it is even and expect [1, 2, 3, 6, 9, 28]

                PASS

                  All other functions were tested the same way
                  and they all pass

                All tests are documented in the attached file
                (Unit_testing.doc)
"""


# Imports #################################################################
# from foo import bar   # remove and add a real import statement


# Functions #############################################################

def get_even_indices(nums):
    """
Takes a list and return the values that have
even indices.

    """
    evens = []
    for i in range(0, len(nums)):
        if i % 2 == 0:
            evens.append(nums[i])
    return evens


def swap_first_and_last(nums):
    return (nums[-1:] + nums[1:-1] + nums[:1])


def zero_in_evens(nums):
    for i in range(0, len(nums)):
        if not (i % 2):
            nums[i] = 0
    return nums


def if_sorted_increasing(nums):
    if nums == sorted(nums):
        return True
    return False


def if_duplicate_exist(nums):
    List = []
    for i in (nums):
        if ((nums).count(i) >= 2):
            List.append(i)
    if list:
        return True
    else:
        return False


def remove_middle(nums):
    if len(nums) % 2 == 0:
        nums.pop(len(nums) // 2 - 1)
        nums.pop(len(nums) // 2)

    else:
        nums.pop(len(nums) // 2)
    return nums


def if_adjacent_exist(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


# Tests #################################################################

def test_get_even_indices():
    nums = [0, 1, 2, 3, 4, 5, 6]
    assert get_even_indices(nums) == [0, 2, 4, 6]


def test_swap_first_and_last():
    nums = [0, 1, 2, 3, 4, 5, 6]
    assert swap_first_and_last(nums) == [6, 1, 2, 3, 4, 5, 0]


def test_zero_in_evens():
    nums = [0, 1, 2, 3, 4, 5, 6]
    assert zero_in_evens(nums) == [0, 1, 0, 3, 0, 5, 0]


def test_if_sorted_increasing():
    nums = [0, 1, 2, 3, 4, 5, 6]
    assert if_sorted_increasing(nums) == True


def test_if_duplicate_exist():
    nums = [0, 1, 2, 3, 4, 1]
    assert if_duplicate_exist(nums) == True


def test_remove_middle():
    nums = [0, 1, 2, 3, 4, 5, 6]
    assert remove_middle(nums) == [0, 1, 2, 4, 5, 6]


def test_if_adjacent_exist():
    nums = [0, 1, 2, 2, 3, 4, 5]
    assert if_adjacent_exist(nums) == True


def make_menu():
    # This menu will have 6 items and the option to exit
    # 1. Get the even indices from a list
    print("1. Get the even indices of a list")
    # 2. Swap the first and last element of a list
    print("2. Swap the first and last element of a list")
    # 3. Replace all even elements with 0
    print("3. Replace all even elements with 0")
    # 4. Check if the list is sorted in increasing order
    print("4. Check if the list is sorted in increasing order")
    # 5. Check if the list contains duplicate elements
    print("5. Check if the list contains duplicate elements")
    # 6. Remove the middle element if the list length is odd,
    #    or the middle two, if it is even
    print("6. Remove the middle element if the list length is odd,"
          " or the middle two, if it is even")
    print("7. Check if the list contains two adjacent duplicate elements ")
    # 7. Exit
    print("8. Exit the program")


def get_user_input():
    while True:
        answer = int(input("Selection: "))
        if 1 <= answer <= 8:
            break
    return answer


# Main #################################################################

def main():
    """
    Implement the main function of program here
    """

    # introduce the program to user
    print("Hi,This program will Process different tasks on a list of "
          "integers that you can choose its elements by yourself.")
    input("please press enter to get started")
    print("Great, let's create our list, first")
    # get list from user
    values = input("Please enter now the numbers of your list,"
                   " and don't forget to separate them "
                   ""
                   "with a comma ").split(',')
    # convert input to integers
    #values = [int(i) for i in values]
    print("Ok, so list now is ", values, "\nlet's get started")
    input("please press enter to see the main menu")
    # introduce main menu to user
    while True:
        print("In main")
        make_menu()
        selection = get_user_input()
        # get even indices
        if selection == 1:
            print("paramater:\t", values)
            print("result:\t", get_even_indices(values))
        # swap first and last element
        elif selection == 2:
            print("paramater:\t", values)
            print("result:\t", swap_first_and_last(values))
        # Replace all even elements with 0
        elif selection == 3:
            print("paramater:\t", values)
            print("result:\t", zero_in_evens(values))
        # Check if the list is sorted in increasing order
        elif selection == 4:
            print("paramater:\t", values)
            print("result:\t", if_sorted_increasing(values))
        # Check if the list contains duplicate elements
        elif selection == 5:
            print("paramater:\t", values)
            print("result:\t", if_duplicate_exist(values))
        # Remove the middle element if the list length is odd,
        # or the middle two, if it is even
        elif selection == 6:
            print("paramater:\t", values)
            print("result:\t", remove_middle(values))
        # Check if the list contains two adjacent duplicate elements
        elif selection == 7:
            print("paramater:\t", values)
            print("result:\t", if_adjacent_exist(values))

        # quit the program
        elif selection == 8:
            break

    input("Press any key to exit")


if __name__ == '__main__':
    print("running")
    main()
else:
    print("imported")
    print("__name__", __name__)
