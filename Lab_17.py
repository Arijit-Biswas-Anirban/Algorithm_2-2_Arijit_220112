# Lab 17: Hamiltonian Cycle

Node = 5

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

path = [-1] * Node

def display_cycle():
    print("Cycle Found! ")
    for i in range(Node):
        print(path[i], end=" ")
    print(path[0])
    return

def is_valid(v, pos):
    if graph[path[pos-1]][v] == 0:
        return False
    
    for i in range(Node):
        if path[i] == v:
            return False
    return True

def hamiltonianCycle(pos):
    if pos == Node:
        if graph[path[pos-1]][path[0]] == 1:
            return True
        else:
            return False
    
    for v in range(1, Node):
        if is_valid(v, pos):
            path[pos]=v
            if hamiltonianCycle(pos+1):
                return True
            path[pos]=-1
    return False

def main():
    path[0] = 0
    if not hamiltonianCycle(1):
        print("Cycle does not exist!")
        return False
    display_cycle()
    return True
main()