from heapq import heappop, heappush

# Function to find the position of the blank space (0)
def find_blank(state):
    return state.index(0)

# Function to swap two positions in the puzzle
def swap(state, pos1, pos2):
    state = list(state)
    state[pos1], state[pos2] = state[pos2], state[pos1]
    return tuple(state)

# Function to generate all possible moves
def get_neighbors(state):
    neighbors = []
    blank_pos = find_blank(state)
    row, col = divmod(blank_pos, 3)  # Get row and column for the blank

    # Possible moves: up, down, left, right
    moves = {
        "left": (row, col - 1),
        "right": (row, col + 1),
        "up": (row - 1, col),
        "down": (row + 1, col)
    }

    for direction, (new_row, new_col) in moves.items():
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_pos = new_row * 3 + new_col
            neighbors.append(swap(state, blank_pos, new_blank_pos))

    return neighbors

# Manhattan Distance Heuristic
def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(9):
        if state[i] == 0:
            continue  # Ignore blank space
        goal_pos = goal_state.index(state[i])
        row_dist = abs(i // 3 - goal_pos // 3)
        col_dist = abs(i % 3 - goal_pos % 3)
        distance += row_dist + col_dist
    return distance

# Greedy Best-First Search Implementation
def gbfs(initial_state, goal_state):
    priority_queue = []
    heappush(priority_queue, (manhattan_distance(initial_state, goal_state), initial_state, 0))  # (heuristic, state, depth)
    visited = set()
    visited.add(initial_state)
    parent_map = {initial_state: None}

    nodes_explored = 0  # Counter for nodes explored

    while priority_queue:
        _, current_state, depth = heappop(priority_queue)
        nodes_explored += 1

        # Check if we reached the goal state
        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent_map[current_state]
            return path[::-1], depth, nodes_explored  # Return path, depth, and nodes explored

        # Explore neighbors
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                heappush(priority_queue, (manhattan_distance(neighbor, goal_state), neighbor, depth + 1))
                parent_map[neighbor] = current_state

    return None, None, nodes_explored  # No solution found

# Initial and goal states
initial_state = (1, 2, 3, 4, 6, 8, 7, 0, 5)  # Initial puzzle state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Goal state

# Run GBFS
solution_path, solution_depth, nodes_explored = gbfs(initial_state, goal_state)

# Print results
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

#code by diana rivera, 1/31/2025