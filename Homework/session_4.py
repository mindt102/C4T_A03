def quick_sort(array = list):
    if len(array) == 1 or len(array) == 0:
        return array
    else:
        pivot_index  = 0
        current_index = len(array) - 1
        delta = -1
        while current_index != pivot_index:
            if array[pivot_index] > array[current_index] and pivot_index < current_index:
                array[pivot_index], array[current_index] = array[current_index],array[pivot_index]
                pivot_index, current_index = current_index, pivot_index
                delta = 1
            if array[pivot_index] < array[current_index] and pivot_index > current_index:
                array[pivot_index], array[current_index] = array[current_index],array[pivot_index]
                pivot_index, current_index = current_index, pivot_index
                delta = -1
            current_index += delta
        lower = quick_sort(array[:pivot_index])
        higher = quick_sort(array[pivot_index+1:])
        return lower + [array[pivot_index]] + higher

def first_capital(input_str):
    if len(input_str) == 0:
        return "There is no capital letter in this string"
    else:
        if input_str[0].isupper():
            return input_str[0]
        else:
            return first_capital(input_str[1:])

def same_head_tail(input_str):
    if len(input_str) == 0:
        return 0
    else:
        valid_substring = same_head_tail(input_str[1:]) + same_head_tail(input_str[:-1]) - same_head_tail(input_str[1:-1])
        if input_str[0] == input_str[-1]:
            valid_substring += 1
        return valid_substring






