def flyod(arr):
    v=len(arr)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if (arr[i][k]!=100000000 and arr[j][k]!=100000000):
                    arr[i][j]=min(arr[i][j],arr[i][k]+arr[j][k])
                    