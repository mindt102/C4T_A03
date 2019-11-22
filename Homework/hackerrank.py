def reduceList(arr):
    final_arr = []
    for elem in arr:
        if elem not in final_arr:
            final_arr.append(elem)
    return final_arr

def position(score,arr,first_index,last_index):
    # if score in arr:
    #     return arr.index(score) + 1
    # if score > arr[0]:
    #     return first_index + 1
    # if score < arr[last_index]:
    #     return last_index + 2
    # if first_index + 1 == last_index:
    #     return last_index + 1
    # else:
    #     mid_index = (first_index + last_index) // 2
    #     if score > arr[mid_index]:
    #         return position(score,arr,first_index,mid_index)
    #     else:
    #         return position(score,arr,mid_index,last_index)
    if score >= arr[0]:
        return first_index + 1
    if score <= arr[last_index]:
        return last_index + 2
    if first_index + 1 == last_index:
        return last_index + 1
    print("score",score)
    while last_index - first_index > 1:
        print("first",first_index)
        print("last",last_index)
        mid_index = (first_index + last_index) // 2
        print("mid",arr[mid_index])
        if score == arr[mid_index]:
            return mid_index + 1
        elif score > arr[mid_index]:
            last_index = mid_index
        else:
            first_index = mid_index
    return last_index + 1

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = reduceList(scores)
    print(scores)
    position_list = []
    for score in alice:
        position_list.append(position(score,scores,0,len(scores)-1))
    return position_list

scores_count = int(input())

scores = list(map(int, input().rstrip().split()))

alice_count = int(input())

alice = list(map(int, input().rstrip().split()))

result = climbingLeaderboard(scores, alice)

print('\n'.join(map(str, result)))
print('\n')