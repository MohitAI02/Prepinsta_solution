# Program to find the n-th Fibonacci number using iteration

def get_nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    try:
        n = int(input("Enter the term number (n): "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return

        result = get_nth_fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Entry point
if __name__ == "__main__":
    main()
