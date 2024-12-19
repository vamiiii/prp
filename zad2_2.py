def group_characters(input_string):
    characters = input_string.split()
    
    result = []
    current_group = []
    
    for char in characters:
        if not current_group or current_group[0] == char:
            current_group.append(char)
        else:
            result.append(current_group)
            current_group = [char]
    
    if current_group:
        result.append(current_group)
    
    return result

input_data = "c c c o o o w w w k k k a a a"
output_data = group_characters(input_data)
print(output_data)
