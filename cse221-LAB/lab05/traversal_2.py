vertices , edges = list(map(int, input().split()))
starts = list(map(int, input().split()))
ends = list(map(int, input().split()))


# creating adj_list
adj_list = {}
for i in range(1, vertices+1):
    adj_list[i] = []


# updating the list 
for j in range(edges):
    if ends[j] not in adj_list[starts[j]]:
        adj_list[starts[j]].append(ends[j])

    if starts[j] not in adj_list[ends[j]]:
        adj_list[ends[j]].append(starts[j])

for x in adj_list:
    adj_list[x].sort()



# coloring for indentifying visited or unvisited
color = {}
for c in adj_list.keys():
    color[c] = 0

# DFS traversal 
def DFS(G , u):
    color[u] = 1
    print(u, end=' ')

    for v in G[u]:
        if color[v] == 0 :
            DFS(G, v)
    

DFS(adj_list, 1)