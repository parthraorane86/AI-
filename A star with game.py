# A* Algorithm for Maze Pathfinding (Game-like Search Problem)

import heapq

# Maze representation
# S = Start, G = Goal, . = Free path, # = Wall
maze = [
    ['S', '.', '.', '#'],
    ['.', '#', '.', '.'],
    ['.', '.', '.', 'G']
]

# Directions (up, down, left, right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Find start and goal positions
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

# Heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, goal):
    open_set = [(heuristic(start, goal), 0, start, [start])]
    closed_set = set()

    while open_set:
        est_total, cost, node, path = heapq.heappop(open_set)

        if node in closed_set:
            continue
        closed_set.add(node)

        if node == goal:
            return path, cost

        for move in moves:
            ni, nj = node[0] + move[0], node[1] + move[1]
            if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] != '#':
                new_cost = cost + 1
                heapq.heappush(open_set, (new_cost + heuristic((ni, nj), goal), new_cost, (ni, nj), path + [(ni, nj)]))

    return None, None

path, cost = a_star_search(start, goal)

if path:
    print("A* Path Found:", path)
    print("Total Steps:", cost)
else:
    print("No path found!")
