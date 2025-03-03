# Lab 03: Compare the performance of linear and binary search on a large dataset of usernames

import random, timeit

def analyze_linear(usernames, target):
    for _ in usernames:
        if _ == target:
            return _
    return -1
def analyze_binary(username, target):
    low, high = 0, len(username)-1
    while low<=high:
        mid = (low + high) // 2
        if username[mid] == target:
            return mid
        elif username[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def generate_username(n):
    username = ["user"+str(i) for i in range(n)]
    random.shuffle(username)
    return username

def main():
    user = int(input("Enter how many users are there: "))
    usernames = generate_username(user)
    sorted_usernames = sorted(usernames)
    target = random.choice(usernames)
    
    
    linear_analysis = timeit.timeit(lambda: analyze_linear(usernames, target), number=10000)
    binary_analysis = timeit.timeit(lambda: analyze_binary(sorted_usernames, target), number=10000)
    
    print(f"Total users: {user}")
    print("*"*40)
    print(f"In linear analysis, time complexity is: {linear_analysis:.6f}")
    print("*"*40)
    print(f"In Binary analysis, time complexity is: {binary_analysis:.6f}")
    
main()