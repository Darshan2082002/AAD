import sys
import heapq

def construct(edges, V):
    adj = [[] for _ in range(V)]
    for edge in edges:
        u, v, wt = edge
        adj[u].append([v, wt])
        adj[v].append([u, wt])   # undirected graph
    return adj

def dijkstra(V, edges, src):
    adj = construct(edges, V)
    pq = []
    dist = [sys.maxsize] * V
    dist[src] = 0
    heapq.heappush(pq, [0, src])

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:  # Skip outdated entries
            continue
        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, [dist[v], v])
    return dist

if __name__ == "__main__":
    V = 5
    src = 0
    edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10],[4,5,6]]

    result = dijkstra(V, edges, src)

    print("Shortest distances from source:", ' '.join(map(str, result)))
