def greatest_division (a,b):
    if a == b:
        return a
    else:
        return greatest_division(max(a,b) - min(a,b),min(a,b))

def merge_sort(lst = list):
    if len(lst) == 1:
        return lst
    else:
        sorted_list = []
        left  = merge_sort( lst[: (len(lst) // 2)] )
        right = merge_sort( lst[(len(lst) // 2):] )
        l = 0
        r = 0
        while True:
            if left[l] >= right[r]:
                sorted_list.append(right[r])
                r += 1
                if r == len(right):
                    return sorted_list + left[l:]
            else:
                sorted_list.append(left[l])
                l += 1
                if l == len(left):
                    return sorted_list + right[r:]
                
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
lst = [3,1,8,124,23,6,2,56,8,1,2]
print(quick_sort(lst))
            