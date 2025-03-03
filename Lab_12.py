# Lab 12: Depth First Search

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    
    for _ in graph[start]:
        if not visited[_]:
            dfs(graph, _, visited)

def add_edge(graph, a, b):
    graph[a].append(b)
    graph[b].append(a)

def main():
    V = 12
    graph = [[] for _ in range(V)]
    
    add_edge(graph, 1, 2)
    add_edge(graph, 1, 3)
    add_edge(graph, 1, 4)
    add_edge(graph, 2, 5)
    add_edge(graph, 2, 6)
    add_edge(graph, 5, 9)
    add_edge(graph, 5, 10)
    add_edge(graph, 4, 7)
    add_edge(graph, 4, 8)
    add_edge(graph, 7, 11)
    
    visited = [False] * len(graph)
    
    dfs(graph, 1, visited)
    
main()