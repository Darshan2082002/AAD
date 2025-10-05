def ford(V,edge,src):
    dist=[100000000]*V
    dist[src]=0
    for i in range(V):
        for edge in edges:
            u,v,wt=edge
            