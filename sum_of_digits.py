# File: sum_of_digits.py

def sum_of_digit_using_for_loop(number):
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total

def sum_of_digits_using_while_loop(number):

    number = abs(number)
    total = 0
    while number > 0:
        total = total + number % 10
        number //= 10
    return total

def main():
    try:
        n = int(input("Enter an integer: "))

        print("\nChoose method to calculate sum of digits:")
        print("1. For loop")
        print("2. While loop")
        choice = input("Enter choice (1 or 2): ")

        if choice == '1':
            result = sum_of_digit_using_for_loop(n)
            print(f"Sum of digits of {n} (using for loop): {result}")
        elif choice == '2':
            result = sum_of_digits_using_while_loop(n)
            print(f"Sum of digits of {n} (using while loop): {result}")
        else:
            print("Invalid choice. Please select 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()


