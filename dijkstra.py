import heapq

# function to find the position of the blank space (0)
def find_blank(state):
    return state.index(0)

# function to swap two positions in the puzzle
def swap(state, pos1, pos2):
    state = list(state)
    state[pos1], state[pos2] = state[pos2], state[pos1]
    return tuple(state)

# function to generate all possible moves
def get_neighbors(state):
    neighbors = []
    blank_pos = find_blank(state)
    row, col = divmod(blank_pos, 3)  # get row and column for the blank

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

# Dijkstra’s Algorithm Implementation
def dijkstra(initial_state, goal_state):
    # Priority Queue (min-heap) for minimum path cost
    pq = []
    heapq.heappush(pq, (0, initial_state))  # (path_cost, state)

    # dictionary to store the minimum cost to reach each state
    cost_map = {initial_state: 0}

    #stores the parent of each state for path reconstruction
    parent_map = {initial_state: None}

    # keep track of explored nodes
    nodes_explored = 0

    while pq:
        current_cost, current_state = heapq.heappop(pq)
        nodes_explored += 1

        # check if we've reached the goal state
        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent_map[current_state]
            return path[::-1], current_cost, nodes_explored

        # explore neighbors
        for neighbor in get_neighbors(current_state):
            new_cost = current_cost + 1  # Cost to reach the neighbor (each move costs 1)

            # if we found a cheaper path to the neighbor, update cost and parent
            if neighbor not in cost_map or new_cost < cost_map[neighbor]:
                cost_map[neighbor] = new_cost
                parent_map[neighbor] = current_state
                heapq.heappush(pq, (new_cost, neighbor))

    return None, None, nodes_explored  # No solution found

# Initial and goal states
initial_state = (1, 2, 3, 4, 6, 8, 7, 0, 5)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
#Dijkstra’s Algorithm
solution_path, solution_depth, nodes_explored = dijkstra(initial_state, goal_state)

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
