# File: positive_negative.py

def check_number_sign(number):
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."

def main():
    try:
        num = float(input("Enter a number: "))
        result = check_number_sign(num)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#main program or function call
main()
