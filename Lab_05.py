# Lab 05: Perform Binary Search on an array

def binary_search(num, low, high, target):
    while low<=high:
        mid = (low+high) // 2
        if num[mid] == target:
            return mid+1
        elif num[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

num = list(map(int, input("Enter numbers: ").split()))
sorted_num = sorted(num)
target = int(input("Enter target key number: "))

index = binary_search(sorted_num, 0, len(num)-1, target)
print(f"Sorted array: {sorted_num}")
if index != -1:
    print(f"Key number found at {index}")
else:
    print("Key number is not found")