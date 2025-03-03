# Lab 01: Calculate the time complexity of an algorithm(linear) for finding the max and min in an unsorted array

import random
import time

def find_mx_mn(numbers, count):
    mx = mn = numbers[0]
    for _ in numbers[1:]:
        count+=1
        if _<mn:
            mn = _
        if _>mx:
            mx = _
    return mx, mn, count

def generate_numbers(num):
    return [random.randint(1,100) for _ in range(num)]

def main():
    while True:
        print(f"What to do?\n1.Find Max\n2.Find Min\n3.Exit\n")
        choice = int(input("Enter choice: "))
        if choice == 3:
            print("Exiting...")
            break
        elif choice in [1,2]:
            num = int(input("Enter how many numbers: "))
            numbers = generate_numbers(num)
            count=0
            start_time = time.perf_counter()
            mx, mn, count = find_mx_mn(numbers,count)
            total_time = time.perf_counter()-start_time
            
            if choice == 1:
                print(f"Max value is: {mx} and total comparison: {count} and time taken: {total_time}")
            elif choice == 2:
                print(f"Min value is: {mn} and total comparison: {count} and time taken: {total_time}")
            else:
                print("Invalid!")
main()