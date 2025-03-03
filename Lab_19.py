# Lab 19: 0/1 Knapsack

def knapsack(profit, weights, capacity, items):
    ks = [[0 for _ in range(capacity+1)] for _ in range(items+1)]
    
    for i in range(1, items+1):
        for w in range(1, capacity+1):
            if weights[i] <= w:
                ks[i][w] = max((profit[i] + ks[i-1][w-weights[i]]), ks[i-1][w])
            else:
                ks[i][w] = ks[i-1][w]
    print(f"Final Knapsack is: {ks}\nTotal Profit: {ks[items][capacity]}")

def main():
    profit = [0, 1, 2, 5, 6]
    weights = [0, 2, 3, 4, 5]
    
    capacity, items = 8, 4
    knapsack(profit, weights, capacity, items)
main()