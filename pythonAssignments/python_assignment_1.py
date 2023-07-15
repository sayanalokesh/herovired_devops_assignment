def check_password_strength(password):
    
# We use boolean variables (has_uppercase, has_lowercase, has_digit, and has_special) to check whether each category is present in the password or not.
# Check the strength of a password based on below criteria.
# Minimum length: The password should be at least 8 characters long.
# Contains both uppercase and lowercase letters.
# Contains at least one digit (0-9).
# Contains at least one special character (e.g., !, @, #, $, %).
    uppercase_letter = False 
    lowercase_letter = False
    atleast_1_digit = False
    atleast_1_special = False
    
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    if len(password) < 8:
        return False

    for char in password:
        if char.isupper():
            uppercase_letter = True  # Check for uppercase letters
        elif char.islower():
            lowercase_letter = True  # Check for lowercase letters
        elif char.isdigit():
            atleast_1_digit = True  # Check for at least one digit
        elif char in special_characters:
            atleast_1_special = True # Check for at least one special character

    if uppercase_letter and lowercase_letter and atleast_1_digit and atleast_1_special:
        return True
    else:
        return False

# Test the function
password = input("Enter a password: ")
if check_password_strength(password):
    print("Password is strong!")
else:
    print("Password is weak. Strong password should contain morethan 8 characters, upper and lowercase letters, atleast one digit, and one special character.")