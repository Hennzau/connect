def check_victory(grid, points):
    if len(points) < 2:
        return True

    # grid is a 2D numpy array where there is a 1 or a 0
    # we want to construct a dictionary (a graph) where the keys are the coordinates of the 1 and the values are the
    # coordinates of the 1s that are adjacent to it

    graph = {}

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                graph[(i, j)] = []
                if i > 0 and grid[i - 1, j] == 1:
                    graph[(i, j)].append((i - 1, j))
                if i < grid.shape[0] - 1 and grid[i + 1, j] == 1:
                    graph[(i, j)].append((i + 1, j))
                if j > 0 and grid[i, j - 1] == 1:
                    graph[(i, j)].append((i, j - 1))
                if j < grid.shape[1] - 1 and grid[i, j + 1] == 1:
                    graph[(i, j)].append((i, j + 1))

    # we want to check if there is a path of 1s that connects the points
    # we will use a breadth first search algorithm

    visited = set()
    queue = [points[0]]
    visited.add(points[0])

    while queue:
        current = queue.pop(0)
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    # check if all points are connected

    for point in points:
        if point not in visited:
            return False

    return True
