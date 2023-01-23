# Variable to store the sum
total = 0

# User input for 5 integers
for i in range(5):
    while True:
        try:
            number = int(input(f"Enter integer {i+1}: "))
            total += number
            break
        except ValueError:
            print("Invalid input. Please enter a valid int.")

# Print the results
print("Sum:", total)
