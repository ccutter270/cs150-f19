def new(dictionary):
    new_dict = {}
    prev_values = []
    for key in dictionary:
        value = dictionary[key]
        if value not in prev_values:
            new_dict[key] = value
            prev_values.append(value)
    return new_dict