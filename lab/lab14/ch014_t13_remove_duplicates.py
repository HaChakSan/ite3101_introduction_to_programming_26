def remove_duplicates(numbers):
    new_list = []
    for i in numbers:
        if i not in new_list:
            new_list.append(i)
    return new_list