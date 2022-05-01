def sortArray(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left = sortArray(left)
    right = sortArray(right)

    return mergeTwoLists(left, right)


def mergeTwoLists(a, b):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while (i < len_a):
        sorted_list.append(a[i])
        i += 1
    while (j < len_b):
        sorted_list.append(b[j])
        j += 1

    return sorted_list

print(sortArray([5,2,3,1]))


