vertices, edges = list(map(int, input().split()))


#creating adj_list 
adj_list = {}
for i in range(1, vertices+1):
    adj_list[i] = []


for j in range(edges):
    starts , ends = list(map(int, input().split()))

    if ends not in adj_list[starts]:
        adj_list[starts].append(ends)

    if starts not in adj_list[ends]:
        adj_list[ends].append(starts)

for x in adj_list:
    adj_list[x].sort()

#graph traversal 

def BFS(G, s):

    queue = []
    color = {}

    for i in G.keys() :
        color[i] = 0

    color[s] = 1
    queue.append(s)

    while queue:
        u = queue.pop(0)
        print(u, end = ' ')
        for v in G[u]:
            if color[v] == 0 :
                color[v] = 1
                queue.append(v)

    


    


G = adj_list
s = 1

BFS(G, s)