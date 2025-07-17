# File: prime_number_checker.py

def is_prime(number):

    if number <= 1:
        return False
    if number == 2:
        return True

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def main():
    try:
        num = int(input("Enter a number: "))
        if num == 2:
            print(f"{num} is a prime number — the only even prime.")
        elif is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
