# File: greatest_of_two.py


def find_greatest(a,b):
    if a > b:
        return f"{a} is greater than {b}."
    elif a < b:
        return f"{b} is greater than {a}"
    else:
        return f"Both numbers are equal."


def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result= find_greatest(num1,num2)
        print(result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


# function calling
if __name__ == '__main__':
    main()