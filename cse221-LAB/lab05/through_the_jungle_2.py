from collections import deque

vertices, edges, source, destination, mandatory_node = map(int, input().split())

# Build adjacency list
adj_list = {i: [] for i in range(1, vertices + 1)}
for _ in range(edges):
    u, v = map(int, input().split())
    adj_list[u].append(v)

def bfs(start, target):
    visited = {i: False for i in adj_list}
    parent = {i: None for i in adj_list}
    level = {i: -1 for i in adj_list}

    queue = deque([start])
    visited[start] = True
    level[start] = 0

    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                queue.append(v)
                if v == target:
                    break

    return parent, level

# Shortcut if source == destination
parent1, level1 = bfs(source, mandatory_node)
parent2, level2 = bfs(mandatory_node, destination)



if source == destination:
    print(0)
    print(source)

else:
    
    if level1[mandatory_node] == -1:
        print(-1)
        

    
    elif level2[destination] == -1:
        print(-1)

    # Reconstruct paths
    else:
        path1 = []
        node = mandatory_node
        while node is not None:
            path1.append(node)
            node = parent1[node]
        path1.reverse()

        path2 = []
        node = destination
        while node is not None:
            path2.append(node)
            node = parent2[node]
        path2.reverse()

        full_path = path1 + path2[1:]

        print(len(full_path) - 1)
        print(*full_path)
