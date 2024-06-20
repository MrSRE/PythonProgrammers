def validate_password():
    # Predefined correct password
    correct_password = "Devopsengineer"
    while True:
        # Prompt the user to enter the password
        user_input = input("Enter the password: ")

        # Check if the entered password is correct
        if user_input == correct_password:
            print("Password is correct. Access granted.")
            break
        else:
            print("Incorrect password. Please try again.")

# Call the function to start the password validation process
validate_password()