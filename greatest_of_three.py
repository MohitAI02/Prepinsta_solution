# File: greatest_of_two.py


def find_greatest(a, b, c):
    if a == b == c:
        return "All three numbers are equal."
    elif a >= b and a >= c:
        return f"{a} is the greatest."
    elif b >= a and b >= c:
        return f"{b} is the greatest."
    else:
        return f"{c} is the greatest."


def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the second number: "))

        result = find_greatest(num1, num2, num3)
        print(result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


# function calling
if __name__ == '__main__':
    main()
