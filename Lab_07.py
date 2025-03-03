# Lab 07: Quick Sort

def partition(numbers, low, high):
    pivot = numbers[low]
    i = low+1
    j = high
    
    while True:
        if i<=j and numbers[i] <= pivot:
            i+=1
        elif i<=j and numbers[j] > pivot:
            j-=1
        elif i<=j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        else:
            break
    
    numbers[low], numbers[j] = numbers[j], numbers[low]
    return j

def quickSort(numbers, low, high):
    if low < high:
        partition_pos = partition(numbers, low, high)
        quickSort(numbers, low, partition_pos-1)
        quickSort(numbers, partition_pos+1, high)
        
        return numbers
    

def main():
    numbers = list(map(int, input("Enter unsorted numbers: ").split()))
    print(f"Unsorted array: {numbers}")
    print("*"*40)
    print(f"Sorted array: {quickSort(numbers, 0, len(numbers)-1)}")
main()