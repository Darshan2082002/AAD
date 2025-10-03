import heapq
def construt(edges,V):
    adj=[[] for _ in range(v)]
    for edge in edges:
        u,v,w=edge
        adj[u].append[v,wt]
        adj[v].append[u,wt]
    return adj
def dijisktra(V,edges,src):
    