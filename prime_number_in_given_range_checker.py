# File: prime_number_checker.py

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def prime_in_range(start, stop):

    print(f"Prime numbers between {start} and {stop}:")
    for num in range(start, stop + 1):
        if is_prime(num):
            print(num)

def main():
    try:
        start = int(input("Enter start of range: "))
        stop = int(input("Enter end of range: "))
        if start > stop:
            print("Start should be less than or equal to stop.")
        else:
            prime_in_range(start, stop)
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
