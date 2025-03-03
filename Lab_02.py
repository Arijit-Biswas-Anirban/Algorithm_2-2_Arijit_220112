# Lab 02: Analyze the average and worst case time complexity of the Binary Search algorithm

import random
import timeit

def binary_search(arr, low, high, target):
    while low<=high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

def generate_array(n):
    numbers = sorted(random.randint(1,n*10) for _ in range(n))
    target = random.choice(numbers)
    
    worst_case =  timeit.timeit(lambda: binary_search(numbers, 0, n-1, -1), number=1000)
    average_case = timeit.timeit(lambda: binary_search(numbers, 0, n-1, target), number=1000)
    
    print(f"Array size: {n}")
    print(f"Average case time complexity: {average_case:.6f}")
    print(f"Worst case time complexity: {worst_case:.6f}")
    print("*"*40)

def main():
    for n in [10, 100, 1000, 10000]:
        generate_array(n)
        
main()