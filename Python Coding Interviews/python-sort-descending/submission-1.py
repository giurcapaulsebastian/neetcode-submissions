from typing import List


def sort_words(words: List[str]) -> List[str]:
    return sorted(words, reverse=True)


# [1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]
def sort_numbers(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]

    greater = [x for x in numbers if x > pivot]
    equal   = [x for x in numbers if x == pivot]
    less    = [x for x in numbers if x < pivot]

    return sort_numbers(greater) + equal + sort_numbers(less)



def sort_decimals(numbers: List[float]) -> List[float]:
    if len(numbers) <= 1:
        return numbers
    
    mid = len(numbers) // 2
    left_arr = sort_decimals(numbers[:mid])
    right_arr = sort_decimals(numbers[mid:])

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    sorted_list = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            sorted_list.append(left_arr[i])
            i+=1
        else:
            sorted_list.append(right_arr[j])
            j+=1
    sorted_list.extend(left_arr[i:])
    sorted_list.extend(right_arr[j:])
    return sorted_list


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
