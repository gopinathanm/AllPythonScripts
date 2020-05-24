def find_max(list_items):
    numbers = list_items
    max     = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max
