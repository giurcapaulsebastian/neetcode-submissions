from typing import List


def sort_words(words: List[str]) -> List[str]:
    return sorted(words)

def sort_numbers(numbers: List[int]) -> List[int]:
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left_half = sort_decimals(numbers[:mid])
    right_half = sort_decimals(numbers[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
