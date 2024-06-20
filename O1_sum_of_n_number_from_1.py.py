# Write a program that calculates the sum of all numbers from 1 to a given positive integer n.
def sum_of_numbers(n):
    # Ensure the input is a positive integer
    if n <= 0:
        return "Please enter a positive integer."
    # Calculate the sum using the formula for the sum of the first n natural numbers
    total_sum = n * (n + 1) // 2
    return total_sum
# Input from the user
n = int(input("Enter a positive integer: "))
# Calculate and print the sum
result = sum_of_numbers(n)
print(f"The sum of all numbers from 1 to {n} is: {result}")