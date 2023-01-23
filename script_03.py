def count_letters(string):
    # Create an empty dict
    count_letters = {}
    
    # Go through each letter in the string
    for letter in string:
        # Only count letters, not spaces
        if letter != " ":
            # Make letter lowercase.
            letter = letter.lower()
            
            # If the letter is not in the dict add it and add 1
            if letter not in count_letters:
                count_letters[letter] = 1
            # If the letter is already in the dict, increment the count
            else:
                count_letters[letter] += 1
    return count_letters

# User input
string = input("Enter a string: ")

# Call the function and print the result
result = count_letters(string)
print(result)
