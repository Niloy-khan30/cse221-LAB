vertices, edges = list(map(int, input().split()))


#creating adj_list 
adj_list = {}
for i in range(1, vertices+1):
    adj_list[i] = []


for j in range(edges):
    starts , ends = list(map(int, input().split()))
    adj_list[starts].append(ends)

for x in adj_list:
    adj_list[x].sort()

print(adj_list)


# cycle detection using BFS 
graph = adj_list
color = {node : 'W' for node in graph}


def DFS(start, color):
    color[start] = 'G'

    for v in graph[start]:
        if color[v] == 'W':
            cycle=DFS(v, color)
            if cycle == True:
                return True


        elif color[v] == 'G':
            return True
    color[start] = 'B'
    return False

is_cyclic = False
for u in graph.keys():
    if color[u] ==  'W' :
        if DFS(u, color):
            is_cyclic = True
            break


if is_cyclic:
    print('YES')

else:
    print('NO')

