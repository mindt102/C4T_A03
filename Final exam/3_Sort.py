def Ascending_sort(arr):
    if len(arr) == 0:
        return arr
    else:
        pivot = arr[0]
        greater = []
        smaller = []
        for i in range(1, len(arr)):
            if arr[i] >= pivot:
                greater.append(arr[i])
            else:
                smaller.append(arr[i])
        return Ascending_sort(smaller) + [pivot] + Ascending_sort(greater)

def Descending_sort(arr):
    return Ascending_sort(arr)[::-1]
    
arr = [0, 10, 20, 3, 1, 2, 3, 5, 12]
print(Ascending_sort(arr))
print(Descending_sort(arr))