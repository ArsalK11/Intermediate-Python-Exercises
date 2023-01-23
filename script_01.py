def unique_elements(data):
    # Create a new list with only unique elements of the inputted list
    unique_data = list(set(data))
    return unique_data

# Test list
test_list = [1, 2, 3, 4, 5, 5, 7, 2, 7, 4, 9, 10, 10]

# Call the function and print the result
result = unique_elements(test_list)
print(result)
