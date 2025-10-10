from collections import deque

# Define goal state
goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)  # 0 is the blank tile

# Possible moves for blank (index): up, down, left, right
moves = {
    'up': -3,
    'down': 3,
    'left': -1,
    'right': 1
}

def get_blank_pos(state):
    return state.index(0)

def is_valid_move(blank_pos, move):
    if move == 'up':
        return blank_pos > 2
    elif move == 'down':
        return blank_pos < 6
    elif move == 'left':
        return blank_pos % 3 != 0
    elif move == 'right':
        return blank_pos % 3 != 2
    return False

def move_blank(state, blank_pos, move):
    new_pos = blank_pos + moves[move]
    state_list = list(state)
    # Swap blank and target tile
    state_list[blank_pos], state_list[new_pos] = state_list[new_pos], state_list[blank_pos]
    return tuple(state_list)

def depth_limited_dfs(state, depth, max_depth, path, visited):
    if state == goal_state:
        return path
    if depth == max_depth:
        return None

    visited.add(state)
    blank_pos = get_blank_pos(state)

    for move in ['up', 'down', 'left', 'right']:
        if is_valid_move(blank_pos, move):
            new_state = move_blank(state, blank_pos, move)
            if new_state not in visited:
                result = depth_limited_dfs(new_state, depth + 1, max_depth, path + [new_state], visited)
                if result is not None:
                    return result
    visited.remove(state)
    return None

def iterative_deepening_search(start_state, max_depth=50):
    for depth in range(max_depth):
        print(f"Searching at depth limit: {depth}")
        visited = set()
        path = depth_limited_dfs(start_state, 0, depth, [start_state], visited)
        if path is not None:
            return path
    return None

def print_puzzle(state):
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(' '.join(str(x) if x != 0 else '_' for x in row))
    print()

# Example initial state (easy scramble)
initial_state = (1, 2, 3,
                 0, 4, 6,
                 7, 5, 8)

solution_path = iterative_deepening_search(initial_state, max_depth=20)

if solution_path:
    print(f"Solution found in {len(solution_path)-1} moves!")
    for step in solution_path:
        print_puzzle(step)
else:
    print("No solution found within depth limit.")
