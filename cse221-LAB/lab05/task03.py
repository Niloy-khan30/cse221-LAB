vertices, edges, source, destination = list(map(int, input().split()))
if source == destination :
    print(0)
    print(source)

else:

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





    # BFS traversal 
    visited = {}
    level = {}
    parent = {}
    queue = []
    output = []

    for node in adj_list.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1





    S = source
    visited[S] = True
    level[S] = 0
    queue.append(S)

    while queue :
        u = queue.pop(0)
        output.append(u)
        for v in adj_list[u]:
            if visited[v] == False:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                queue.append(v)




    # the length of the shortest path 
    print(level[destination])


    # printing the shortest path 
    path = []
    z = destination
    while z is not None:
        path.append(z)
        z = parent[z]

    if (path is  []) or (len(path) == 1):
        print(-1)

    else:
        
        path.reverse()
        print(*path)