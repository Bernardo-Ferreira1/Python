import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generate a secure random password that satisfies specific character constraints.

    Parameters:
        length (int): Total length of the password. Default is 16.
        nums (int): Minimum number of numeric characters. Default is 1.
        special_chars (int): Minimum number of special characters. Default is 1.
        uppercase (int): Minimum number of uppercase letters. Default is 1.
        lowercase (int): Minimum number of lowercase letters. Default is 1.

    Returns:
        str: A randomly generated password that meets the constraints.
    """
    # Define the possible characters for the password
    letters = string.ascii_letters  # Includes both uppercase and lowercase letters
    digits = string.digits          # Includes numeric characters (0-9)
    symbols = string.punctuation    # Includes special characters like @, #, $, etc.

    # Combine all characters to form the pool of possible password characters
    all_characters = letters + digits + symbols

    # Continuously generate passwords until one satisfies all constraints
    while True:
        password = ''
        # Randomly select characters to form the password
        for _ in range(length):
            password += secrets.choice(all_characters)

        # Define constraints as pairs of (minimum count, regex pattern)
        constraints = [
            (nums, r'\d'),                   # Check for numeric characters
            (special_chars, fr'[{symbols}]'), # Check for special characters
            (uppercase, r'[A-Z]'),           # Check for uppercase letters
            (lowercase, r'[a-z]')            # Check for lowercase letters
        ]

        # Check if the generated password meets all constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break  # Exit loop if password satisfies all constraints

    return password
if __name__ == '__main__':
	new_password = generate_password()
	print('Generated password:', new_password)