from heapq import heappop, heappush

def best_first_search(start, goal, heuristic):
    open_set = []
    heappush(open_set, (heuristic[start], start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic[start]}

    while open_set:
        current = heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                if neighbor not in [i[1] for i in open_set]:
                    heappush(open_set, (f_score[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def get_neighbors(node):
    
    return []
if __name__ == "__main__":
    start = (0, 0)
    goal = (5, 5)
    heuristic = {
        (0, 0): 10,
        (0, 1): 9,
        (0, 2): 8,
        (0, 3): 7,
        (0, 4): 6,
        (0, 5): 5,
        (1, 0): 9,
        (1, 1): 8,
        (1, 2): 7,
        (1, 3): 6,
        (1, 4): 5,
        (1, 5): 4,
        (2, 0): 8,
        (2, 1): 7,
        (2, 2): 6,
        (2, 3): 5,
        (2, 4): 4,
        (2, 5): 3,
        (3, 0): 7,
        (3, 1): 6,
        (3, 2): 5,
        (3, 3): 4,
        (3, 4): 3,
        (3, 5): 2,
        (4, 0): 6,
        (4, 1): 5,
        (4, 2): 4,
        (4, 3): 3,
        (4, 4): 2,
        (4, 5): 1,
        (5, 0): 5,
        (5, 1): 4,
        (5, 2): 3,
        (5, 3): 2,
        (5, 4): 1,
        (5, 5): 0,
    }
    path = best_first_search(start, goal, heuristic)
    print("Path found:", path)