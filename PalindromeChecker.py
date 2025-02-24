def is_palindrome(text):
    """
    Checks if a given string is a palindrome (ignoring spaces and case).

    Args:
        text: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    processed_text = "".join(char.lower() for char in text if char.isalnum())
    return processed_text == processed_text[::-1]

# Get input from the user
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")