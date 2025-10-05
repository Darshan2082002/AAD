def flyod(arr):
    v=len(arr)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if (arr[i][k]!=100000000 and arr[j][k]!=100000000):
                    arr[i][j]=min(arr[i][j],arr[i][k]+arr[j][k])
                    
if __name__ == "__main__":
    
    INF = 100000000
    dist = [
        [0, 4, INF, 5, INF],
        [INF, 0, 1, INF, 6],
        [2, INF, 0, 3, INF],
        [INF, INF, 1, 0, 2],
        [1, INF, INF, 4, 0]
    ]
    
    floydWarshall(dist)
    for i in range(len(dist)):
        for j in range(len(dist)):
            print(dist[i][j], end=" ")
        print()