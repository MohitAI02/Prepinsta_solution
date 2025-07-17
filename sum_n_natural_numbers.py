# File: sum_n_natural_numbers.py

def sum_using_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

#using the formula
def sum_using_formula(n):
    return n * (n + 1) // 2

def main():
    try:
        n = int(input("Enter a positive integer (N): "))
        if n <= 0:
            return print("Please enter a number greater than 0.")


        print("\nChoose method:")
        print("1. Loop method")
        print("2. Formula method")
        choice = input("Enter choice (1 or 2): ")

        if choice == '1':
            result = sum_using_loop(n)
            print(f"Sum of first {n} natural numbers (loop): {result}")
        elif choice == '2':
            result = sum_using_formula(n)
            print(f"Sum of first {n} natural numbers (formula): {result}")
        else:
            print("Invalid choice. Please select 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")


main()
