# Lab 18: Heap Sort

def max_heap(arr, n, parent_index):
    largest = parent_index
    left_child = 2*parent_index + 1
    right_child = 2*parent_index + 2
    
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
    
    if largest != parent_index:
        arr[largest], arr[parent_index] = arr[parent_index], arr[largest]
        max_heap(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        max_heap(arr, n, i)
    for j in range(n-1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        max_heap(arr, j, 0)

def main():
    arr = list(map(int, input("Enter heap tree nodes(sorted/unsorted): ").split()))
    heapSort(arr)
    print(arr)
main()