# Simple Calculator in Python with Comments

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:  # Check to avoid division by zero error
        return x / y
    else:
        return "Error! Division by zero."

# Main function where the program starts
def main():
    # Display options to the user
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            # Ask for two numbers from the user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            # Handle the error if the input is not a number
            print("Invalid input. Please enter numbers.")
            return

        # Perform the selected operation
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        # Handle invalid operation choice
        print("Invalid choice.")

# This ensures that the main() function runs when the script is executed
if __name__ == "__main__":
    main()
