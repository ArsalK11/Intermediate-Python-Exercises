def get_combined_dict(my_dict_1, my_dict_2):
    # New dict to store the combined values
    combined = {}
    
    # Go through the keys of both dicts
    for key in my_dict_1.keys():
        if key in my_dict_2.keys():
            # If the key is in both dicts, combine the values and store in the new dict
            combined[key] = my_dict_1[key] + my_dict_2[key]
    #Return combined
    return combined

#Test list
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)

