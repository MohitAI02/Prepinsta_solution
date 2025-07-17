# File: armstrong_in_range_for_loop.py

def is_armstrong(num):
    power = len(str(num))
    total = 0
    for digit in str(num):
        total += int(digit) ** power
    return total == num

def find_armstrong_in_range(start, end):
    print(f"Armstrong numbers between {start} and {end} are:")
    for number in range(start, end + 1):
        if is_armstrong(number):
            print(number, end=' ')

def main():
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        find_armstrong_in_range(start, end)
    except ValueError:
        print("Please enter valid integer values.")

if __name__ == "__main__":
    main()
