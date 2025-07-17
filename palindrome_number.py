# File: palindrome_number.py

def reverse_number(n):
    reverse = ''
    for digit in str(n)[::-1]:
        reverse += digit
    return int(reverse)

def is_palindrome(n):
    return n == reverse_number(n)

def main():
    try:
        num = int(input("Enter a number: "))

        print("\nChoose option:")
        print("1. Reverse the number")
        print("2. Check if palindrome")

        choice = input("Enter choice (1 or 2): ")

        if choice == '1':
            reversed_num = reverse_number(num)
            print(f"Reverse of {num} is {reversed_num}")
        elif choice == '2':
            if is_palindrome(num):
                print(f"{num} is a Palindrome number.")
            else:
                print(f"{num} is NOT a Palindrome number.")
        else:
            print("Invalid choice. Please select 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
