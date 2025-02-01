import heapq

# function finds the position of the blank space (0)
def find_blank(state):
    return state.index(0)

# function swaps the two positions in the puzzle
def swap(state, pos1, pos2):
    state = list(state)
    state[pos1], state[pos2] = state[pos2], state[pos1]
    return tuple(state)

# function generates all possible moves
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

# manhattan distance
def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(9):  # for each tile (0 to 8)
        if state[i] != 0:  # skip blank space
            goal_pos = goal_state.index(state[i])
            goal_row, goal_col = divmod(goal_pos, 3)
            current_row, current_col = divmod(i, 3)
            distance += abs(goal_row - current_row) + abs(goal_col - current_col)
    return distance

# A* Search Algorithm
def a_star(initial_state, goal_state):
    # Priority Queue (min-heap) for minimum f(n) = g(n) + h(n)
    pq = []
    heapq.heappush(pq, (0 + manhattan_distance(initial_state, goal_state), 0, initial_state))  # (f(n), g(n), state)

    # dictionaries to store g(n), f(n), and parent for path reconstruction
    g_map = {initial_state: 0}  # g(n): cost to reach the state
    parent_map = {initial_state: None}  # parent map for path reconstruction

    # set to keep track of visited states
    visited = set()

    nodes_explored = 0  # nodes explored counter

    while pq:
        _, current_cost, current_state = heapq.heappop(pq)
        nodes_explored += 1

        # check if we've reached the goal state
        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent_map[current_state]
            return path[::-1], current_cost, nodes_explored  # return path, depth, and nodes explored

        visited.add(current_state)

        # Explore neighbors
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                new_cost = current_cost + 1  # cost to reach the neighbor (1 cost)
                h_value = manhattan_distance(neighbor, goal_state)  # heuristic value (Manhattan distance)

                # calculate f(n) = g(n) + h(n)
                f_value = new_cost + h_value

                # If we found a cheaper path to the neighbor, update g and parent
                if neighbor not in g_map or new_cost < g_map[neighbor]:
                    g_map[neighbor] = new_cost
                    parent_map[neighbor] = current_state
                    heapq.heappush(pq, (f_value, new_cost, neighbor))

    return None, None, nodes_explored  # No solution found

# Initial and goal states
initial_state = (1, 2, 3, 4, 6, 8, 7, 0, 5)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# A* Search
solution_path, solution_depth, nodes_explored = a_star(initial_state, goal_state)

#results
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

# code by diana rivera, 1/31/2025
