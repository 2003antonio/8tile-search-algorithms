from collections import deque

# function finds the position of the blank space (0)
def find_blank(state):
    return state.index(0)


#function swaps the two positions in the puzzle
def swap(state, pos1, pos2):
    state = list(state)
    state[pos1], state[pos2] = state[pos2], state[pos1]
    return tuple(state)


# function generates all possible moves
def get_neighbors(state):
    neighbors = []
    blank_pos = find_blank(state)
    row, col = divmod(blank_pos, 3)  # Get row and column for the blank

    # possible moves: up, down, left, right
    moves = {
        "up": (row - 1, col),
        "down": (row + 1, col),
        "left": (row, col - 1),
        "right": (row, col + 1)
    }

    for direction, (new_row, new_col) in moves.items():
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_pos = new_row * 3 + new_col
            neighbors.append(swap(state, blank_pos, new_blank_pos))

    return neighbors


# BFS implementation
def bfs(initial_state, goal_state):
    # initialize the queue and visited set
    queue = deque([(initial_state, 0)])  # (state, depth)
    visited = set()
    visited.add(initial_state)
    parent_map = {initial_state: None}  # solution path reconstruction

    #keep track of nodes explored
    nodes_explored = 0

    while queue:
        current_state, depth = queue.popleft()
        nodes_explored += 1

        # check if we've reached the goal state
        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent_map[current_state]
            return path[::-1], depth, nodes_explored  # return path, depth, and nodes explored

        # explore neighbors
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))  # increase depth for neighbors
                parent_map[neighbor] = current_state

    return None, None, nodes_explored  # no solution found

initial_state = (1, 2, 3, 4, 6, 8, 7, 0, 5)  # initial puzzle
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # goal state

solution_path, solution_depth, nodes_explored = bfs(initial_state, goal_state)

if solution_path:
    print("Path to goal:")
    for step in solution_path:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print()
    print(f"Solution found at depth {solution_depth}! Nodes explored: {nodes_explored}")
else:
    print(f"No solution exists. Nodes explored: {nodes_explored}")

#code by antonio martinez, 1/31/2025