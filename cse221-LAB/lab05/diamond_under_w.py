rows, cols = list(map(int, input().split()))
grid = []
for i in range(rows):
    text = input()
    grid.append(text)

# applying bfs to this grid 
visited = [[False]*cols for _ in range(rows)]
directions = [(-1, 0), (1,0),(0, -1), (0, 1)]

def BFS(x, y):
    queue = []
    queue.append((x, y))
    visited[x][y] = True
    diamonds = 0

    while queue :
        a, b = queue.pop(0)
        if grid[a][b] == 'D':
            diamonds += 1

        for d in directions:
            e, f = a + d[0], b + d[1]

            if( 0 <= e < rows and 0 <= f < cols ) and not visited[e][f] and grid[e][f] != '#':
                visited[e][f] = True
                queue.append((e, f))


    return diamonds




max_diamond = 0
for i in range(rows):
    for j in range(cols):
        if not visited[i][j] and grid[i][j] != '#':
            max_diamond = max(max_diamond, BFS(i, j))

print(max_diamond)