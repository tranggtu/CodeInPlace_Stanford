"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one. (Hailstone sequence)
"""

def main():
    num = int(input("Enter a number: "))
    remainder = num % 2
    if remainder == 0:
        result = int(num / 2)
        print(f"{num} is even, so I take half: {result}")
    else:
        result = int(3*num + 1)
        print(f"{num} is odd, so I make 3n + 1: {result}")

        while result > 1: 
            if result % 2 == 0:
                print(f"{result} is even, so I take half: {int(result/2)}")
                result = int(result/2) # update result
            else:
                print(f"{result} is odd, so I take 3n + 1: {int(3 * result + 1)}")
                result = int(3*result + 1) # update result

if __name__ == "__main__":
    main()