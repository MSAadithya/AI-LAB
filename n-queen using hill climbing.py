import random

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def conflicts(state, col, row):
    """Count conflicts for placing a queen at (row, col)"""
    count = 0
    n = len(state)
    for c in range(n):
        if c == col:
            continue
        r = state[c]
        if r == row:
            count += 1
        if abs(r - row) == abs(c - col):
            count += 1
    return count

def total_conflicts(state):
    """Calculate total number of attacking pairs"""
    n = len(state)
    total = 0
    for col in range(n):
        total += conflicts(state, col, state[col])
    return total // 2  # each pair counted twice

def hill_climbing(n=4):
    # Start with random state: one queen per column, random rows
    state = [random.randint(0, n-1) for _ in range(n)]

    steps = 0
    while True:
        current_conflicts = total_conflicts(state)
        if current_conflicts == 0:
            # Solution found
            print(f"Solved in {steps} steps.")
            return state

        next_state = list(state)
        min_conflicts = current_conflicts
        # Try moving each queen in its column to all rows, pick the best move
        for col in range(n):
            original_row = state[col]
            for row in range(n):
                if row == original_row:
                    continue
                state[col] = row
                conflicts_count = total_conflicts(state)
                if conflicts_count < min_conflicts:
                    min_conflicts = conflicts_count
                    next_state = list(state)
            state[col] = original_row

        # If no improvement, stuck in local maxima
        if min_conflicts == current_conflicts:
            # print("Stuck in local maxima, no better moves.")
            return None

        state = next_state
        steps += 1

def random_restart_hill_climbing(n=4, max_restarts=100):
    for restart in range(max_restarts):
        # print(f"Restart {restart+1}")
        solution = hill_climbing(n)
        if solution:
            return solution
    print("No solution found after maximum restarts.")
    return None

# Run the algorithm
n = 4
solution = random_restart_hill_climbing(n, max_restarts=100)
if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution found.")
