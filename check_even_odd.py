# File: even_odd_checker.py

def check_even_or_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

def main():
    try:
        num = int(input("Enter an integer: "))
        result = check_even_or_odd(num)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

main()
