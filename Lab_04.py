# Lab 04: Find max and min element using Divide and Conquer method

def find_max_min(numbers, low, high):
    if low == high:
        return numbers[low], numbers[low]
    elif high == low+1:
        if numbers[low] < numbers[high]:
            return numbers[high], numbers[low]
    mid = (low+high) // 2
    left_max, left_min = find_max_min(numbers, low, mid)
    right_max, right_min = find_max_min(numbers, mid+1, high)
    
    final_max, final_min = max(left_max, right_max), min(left_min, right_min)
    return final_max, final_min
    
def main():
    numbers = list(map(int, input("Enter numbers: ").split()))
    max, min = find_max_min(numbers, 0, len(numbers)-1)
    print(f"Max: {max}\nMin: {min}")
    
main()