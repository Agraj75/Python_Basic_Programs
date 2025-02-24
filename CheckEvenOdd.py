def check_even_odd():
    """
    Checks if a number entered by the user is even or odd.
    """
    try:
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")

    except ValueError:
        print("Invalid input. Please enter an integer.")

# Call the function to run the check
check_even_odd()