def activity_selection(start, finish):
    n = len(finish)
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    selected = [activities[0]]
    last_finish_time = activities[0][1]
    for i in range(1, n):
        if activities[i][0] >= last_finish_time:
            selected.append(activities[i])
            last_finish_time = activities[i][1]
    return selected

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
result = activity_selection(start, finish)
print("Selected activities (start, finish):")
for s, f in result:
    print(f"({s}, {f})")
