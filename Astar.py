from heapq import heappush, heappop

def astar(graph, start, goal, h):
    open_list = []
    heappush(open_list, (0 + h[start], 0, start, [start]))
    closed = set()
    while open_list:
        f, g, node, path = heappop(open_list)
        if node == goal:
            return path
        if node in closed:
            continue
        closed.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in closed:
                g_new = g + cost
                f_new = g_new + h[neighbor]
                heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))
    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
h = {'A': 6, 'B': 4, 'C': 4, 'D': 4, 'E': 2, 'F': 0}
path = astar(graph, 'A', 'F', h)
print("Path found:", path)
