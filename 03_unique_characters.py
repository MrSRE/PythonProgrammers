# Write a Python program that takes a string as input and finds and displays all the unique characters in the string
# Requirements
#   Prompt the user to enter a string.
#   Convert the string into a set to remove duplicate characters.
#   Display the unique characters found in the string, in the order of their occurrence.

def find_unique_characters():
    # Prompt the user to enter a string
    input_string = input("Enter a string: ")

    # Use a set to track characters we've seen
    seen = set()
    # Use a list to maintain the order of unique characters
    unique_chars = []

    # Iterate through the input string
    for char in input_string:
        if char not in seen:
            # Add the character to the set and the list if it's not already seen
            seen.add(char)
            unique_chars.append(char)

    # Display the unique characters in the order of their occurrence
    print("Unique characters in the string:", ''.join(unique_chars))

# Call the function to execute the program
find_unique_characters()
