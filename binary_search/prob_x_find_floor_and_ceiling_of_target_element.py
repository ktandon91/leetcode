def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    if target < arr[start]:
        return arr[start]
    if target > arr[end]:
        return - 1
    #TODO: Extra condition to check if target < arr[start]
    # return -1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return arr[mid]
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return arr[start], arr[end]

ceil, floor = binary_search([2,3,5,7,14,16,19], 9)
print(f"floor: {floor} and ceil: {ceil}")