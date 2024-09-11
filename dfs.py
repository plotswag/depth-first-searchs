

'''Depth First Search uses STACK AND RECURSION
'''

from collections import defaultdict
def dfs(graph,start,visited,path):
    path.append(start)
    visited[start]=True
    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(graph,neighbour,visited,path)
    return path
graph=defaultdict(list)
n,e=map(int,input().split())
for i in range(e):
    u,v=input().split()
    graph[v].append(u)
print(graph)
start='A'
visited=defaultdict(bool)
path=[]
traversedpath=dfs(graph,start,visited,path)
print(traversedpath)
