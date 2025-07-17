# File: armstrong_number_checker.py

def is_armstrong_for(number):
    power = len(str(number))
    total = 0
    for digit in str(number):
        total += int(digit) ** power
    return total == number

def is_armstrong_while(number):
    power = len(str(number))
    total = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return total == number

def main():
    try:
        num = int(input("Enter a number: "))
        print("Choose method:")
        print("1. Using for loop")
        print("2. Using while loop")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            result = is_armstrong_for(num)
        elif choice == '2':
            result = is_armstrong_while(num)
        else:
            print("Invalid choice.")
            return

        if result:
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
