# Lab 11: Breadth First Search

from collections import deque

def bfs(graph, start):
    dq = deque()
    visited = [False] * len(graph)
    
    visited[start] = True
    dq.append(start)
    
    while dq:
        current_node = dq.popleft()
        print(current_node, end=" ")
        
        for _ in graph[current_node]:
            if not visited[_]:
                visited[_] = True
                dq.append(_)
                
def add_edge(graph, a, b):
    graph[a].append(b)
    graph[b].append(a)

def main():
    V = 5
    graph = [[] for _ in range(V)]
    
    add_edge(graph, 0, 2)
    add_edge(graph, 0, 1)
    add_edge(graph, 2, 4)
    add_edge(graph, 1, 3)
    add_edge(graph, 3, 4)
    
    bfs(graph, 0)
    
main()