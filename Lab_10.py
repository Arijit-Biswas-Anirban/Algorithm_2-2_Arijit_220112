# Lab 10: Travelling Salesman Person 

def tsp(dist_mat, start):
    n = len(dist_mat)
    vis = [False] * n
    vis[start] = True
    path = [start]
    current_city = start
    total_distance=0
    for _ in range(n-1):
        nearest_city = None
        minimum_dist = float ('inf')
        for city in range(n):
            if not vis[city] and dist_mat[current_city][city] < minimum_dist:
                nearest_city = city
                minimum_dist = dist_mat[current_city][city]
        path.append(nearest_city)
        vis[nearest_city] = True
        current_city = nearest_city
        total_distance += minimum_dist
    path.append(start)
    total_distance+=dist_mat[current_city][start]
    
    return path, total_distance

def main():
    dist_mat = [
        (0, 10, 20, 25),
        (10, 0, 35, 20),
        (15, 20, 0, 10),
        (25, 30, 15, 0),
    ]
    path, total_distance = tsp(dist_mat, 0)
    print(f"Path is: {path} and total distance covered: {total_distance}")

main()