# File: reverse_number.py

def reverse_number_with_for(n):
    reverse = ''
    for i in str(n)[::-1]:
        reverse += i  # Concatenating characters to form reversed string
    return int(reverse)  # Convert final string back to integer


def reverse_number_with_while(n):
    reverse = []
    while n > 0:
        digit = n % 10
        reverse.append(digit)
        n = n // 10
    reversed_str = ''.join(map(str, reverse))  # Join list of digits
    return int(reversed_str)  # Convert to int


def main():
    try:
        num = int(input("Enter a number: "))

        print("\nChoose method to reverse:")
        print("1. Using for loop and string slicing")
        print("2. Using while loop and list")

        choice = input("Enter choice (1 or 2): ")

        if choice == '1':
            reversed_num = reverse_number_with_for(num)
            print(f"Reverse of {num} is {reversed_num}")
        elif choice == '2':
            reversed_num = reverse_number_with_while(num)
            print(f"Reverse of {num} is {reversed_num}")
        else:
            print("Invalid choice. Please select 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
