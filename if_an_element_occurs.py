#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: June 2021
# This program checks whether an element occurs in a list


def search_elements(inputs, input_to_search):
    # this function searches the list for the specified element
    position = 1
    result = "The element is not in the list"

    for counter in inputs:
        if counter == input_to_search:
            result = ("{0} was found in position {1} of the list"
                      .format(counter, position))
            break
        position += 1

    return result


def main():
    # this function receives input and calls a function

    # declaration
    inputs = []

    # input
    input_to_search = input("Which element would you like to check for?: ")
    print("Enter elements to add to the list. Enter 'STOP' to end inputting:")
    element = input("Element: ")
    inputs.append(element)
    while element != "STOP":
        element = input("Element: ")
        if element != "STOP":
            inputs.append(element)
    answer = search_elements(inputs, input_to_search)
    print(answer)
    print("Done.")


if __name__ == "__main__":
    main()
