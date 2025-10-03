import heapq
def construt(edges,V):
    adj=[[] for _ in range(v)]
    for edge in edges:
        u,v,w=edge