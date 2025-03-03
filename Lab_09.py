# Lab 09: Fractional Knapsack

def frac_knap(values, weights, capacity):
    items = sorted(zip(values, weights), key=lambda item: item[0]/item[1], reverse=True)
    
    total_profit = 0
    
    for values,weights in items:
        if weights<=capacity:
            capacity-=weights
            total_profit+=values
        else:
            total_profit+=values * (capacity/weights)
    return total_profit

def main():
    item = int(input("Enter number of items: "))
    values = []
    weights = []
    
    for _ in range(item):
        value, weight = map(int, input("Enter value and weight: ").split())
        values.append(value)
        weights.append(weight)
    capacity = int(input("Enter total capacity: "))
    print(f"Total Profit : {frac_knap(values, weights, capacity)}")
main()