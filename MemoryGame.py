"""
File: MemoryGame.py
Test your ability to remember and match pairs of items. 

https://codeinplace.stanford.edu/public/share/PPherMv8Cx304P0j6ePd
"""

import random

NUM_PAIRS = 3

def main():
    """
    Main function to run the memory game.
    """
    truth = truth_list()  # create truth list
    truth = shuffle_list(truth)  # shuffle list

    displayed = ["*"] * (NUM_PAIRS * 2)

    while True:
        print(displayed)
        index1 = get_valid_index(displayed)  # get first index

        while True:
            index2 = get_valid_index(displayed)  # get second index
            if index2 != index1:
                break

        print(f"Value at index {index1} is {truth[index1]}")
        print(f"Value at index {index2} is {truth[index2]}")

        if truth[index1] == truth[index2]:
            print('Match!')
            displayed[index1] = displayed[index2] = str(truth[index1])
        else:
            print("No match. Try again.")
            time.sleep(2)  # wait briefly before clearing

        clear_terminal()

        if displayed == [str(x) for x in truth]:
            print("Congratulations! You won!")
            break

def truth_list():
    """
    Create a list that has the values 0 through NUM_PAIRS - 1 twice.
    Example output: [0, 0, 1, 1, 2, 2]
    """
    truth = []
    for i in range(NUM_PAIRS):
        for k in range(2):
            truth.append(i)
    return truth

def shuffle_list(truth):
    """
    Shuffle the list to get a random order.
    """
    random.shuffle(truth)
    return truth

def get_valid_index(displayed):
    """
    Get a valid index from user. Must be >= 0 and must correspond to a "*".
    """
    while True:
        try:
            index = int(input("Enter an index: "))
            if 0 <= index < len(displayed) and displayed[index] == "*":
                return index
            else:
                print("Invalid index. Please enter an index again!")
        except ValueError:
            print("Please enter a number")
    
def clear_terminal():
    for i in range(20):
        print('\n')

if __name__ == '__main__':
    main()