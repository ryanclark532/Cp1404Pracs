"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Value Error will occur when a non int number is entered
2. When will a ZeroDivisionError occur?
when user enters 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Using a while loop for error checking avoids the need for and exception
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator==0:
        print("please enter a valid denominator")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")