#Lab 14: Bubble Sort and Selection Sort

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selectionSort(arr):
    n = len(arr)
    for ind in range(n):
        min_ind = ind
        for i in range(ind+1, n):
            if arr[i] < arr[min_ind]:
                arr[i], arr[min_ind] = arr[min_ind], arr[i]
                min_ind = i
    return arr  
        
def main():
    arr = list(map(int, input("Enter array elements: ").split()))
    print(f"Sorted array is : {bubbleSort(arr)}")
    print(f"Sorted array is : {selectionSort(arr)}")
main()