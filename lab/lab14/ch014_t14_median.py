def median(numbers):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        mid1 = numbers[length // 2 - 1]
        mid2 = numbers[length // 2]
        return (mid1 + mid2) / 2
    else:
        return numbers[length // 2]