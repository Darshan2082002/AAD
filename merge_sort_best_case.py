import random
import time
import math
import pandas as pd
import matplotlib.pyplot as plt

# Merge sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # merge
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged

# Timer wrapper
def time_merge_sort(arr):
    start = time.perf_counter()
    _ = merge_sort(arr)
    end = time.perf_counter()
    return end - start

# Experiment settings
sizes = [500, 1000, 2000, 4000, 8000, 16000]  # input sizes to test
trials = 5  # number of trials per case and size

results = []
for n in sizes:
    best_times = []
    avg_times = []
    worst_times = []
    for t in range(trials):
        # Average case: random list
        rnd = [random.randint(0, 10**6) for _ in range(n)]
        avg_times.append(time_merge_sort(list(rnd)))
        # Best case: already sorted
        sorted_list = sorted(rnd)
        best_times.append(time_merge_sort(list(sorted_list)))
        # Worst case: reverse sorted
        rev_sorted = sorted_list[::-1]
        worst_times.append(time_merge_sort(list(rev_sorted)))
    results.append({
        "n": n,
        "best_mean_s": sum(best_times)/len(best_times),
        "avg_mean_s": sum(avg_times)/len(avg_times),
        "worst_mean_s": sum(worst_times)/len(worst_times),
        "best_std_s": pd.Series(best_times).std(),
        "avg_std_s": pd.Series(avg_times).std(),
        "worst_std_s": pd.Series(worst_times).std(),
    })

df = pd.DataFrame(results)

# Plotting (single plot)
plt.figure(figsize=(9,6))
plt.plot(df["n"], df["best_mean_s"], marker='o', label="Best case")
plt.plot(df["n"], df["avg_mean_s"], marker='o', label="Average case")
plt.plot(df["n"], df["worst_mean_s"], marker='o', label="Worst case")
plt.xlabel("Input size (n)")
plt.ylabel("CPU time (seconds)")
plt.title("Merge Sort: Best / Average / Worst case CPU time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
