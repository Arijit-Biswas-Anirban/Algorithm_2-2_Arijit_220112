# Lab 21: Dijkstra's Algorithm

import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float ('inf')] * n
    distances[start] = 0
    pq = [(0, start)]
    prev = [-1] * n
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        for neighbors in range(n):
            if graph[node][neighbors] > 0:
                new_dist = dist + graph[node][neighbors]
                if new_dist < distances[neighbors]:
                    distances[neighbors] = new_dist
                    heapq.heappush(pq, (new_dist, neighbors))
                    prev[neighbors] = node
    
    path = []
    curr = end
    
    while curr != -1:
        path.append(chr(ord('A') + curr))
        curr = prev[curr]
    path.reverse()
    
    return distances[end], path

def main():
    graph = [
        [0, 5, 3, 0, 0],  # A
        [5, 0, 1, 3, 0],  # B
        [3, 1, 0, 2, 6],  # C
        [0, 3, 2, 0, 4],  # D
        [0, 0, 6, 4, 0]   # E
    ]
    start = 0
    end = 4
    
    shortest_distance, shortest_path = dijkstra(graph, start, end)
    print(f"Shortest Path is: {'->'.join(shortest_path)}")
    print(f"Shortest distance : {shortest_distance}")
main()    