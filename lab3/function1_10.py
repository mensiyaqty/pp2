def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(unique_list(numbers))
