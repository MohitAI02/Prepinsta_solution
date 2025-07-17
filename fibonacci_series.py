# Program to display the Fibonacci sequence up to n-th term

def generate_fibonacci(n):
    a, b = 0, 1
    print("\nFibonacci sequence:")
    for _ in range(n):
        print(a)
        a, b = b, a + b

def main():
    try:
        n = int(input("Enter the number of terms to generate the Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            generate_fibonacci(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    main()
