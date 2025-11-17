# -----------------------------------------------------------
# Alpha-Beta Pruning (Minimax) Implementation in Python
# -----------------------------------------------------------

import math

def alphabeta(node, depth, alpha, beta, maximizingPlayer, values, tree):
    """
    node  : current node index
    depth : current depth in game tree
    alpha : best score for maximizer
    beta  : best score for minimizer
    maximizingPlayer : True/False
    values: values of leaf nodes
    tree  : adjacency list of game tree
    """

    # If leaf node → return leaf value
    if node in values:
        return values[node]

    if maximizingPlayer:
        maxEval = -math.inf

        for child in tree[node]:
            eval = alphabeta(child, depth + 1, alpha, beta, False, values, tree)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)

            # Pruning
            if beta <= alpha:
                break

        return maxEval

    else:
        minEval = math.inf

        for child in tree[node]:
            eval = alphabeta(child, depth + 1, alpha, beta, True, values, tree)
            minEval = min(minEval, eval)
            beta = min(beta, eval)

            # Pruning
            if beta <= alpha:
                break

        return minEval


# -----------------------------------------------------------
# Example Tree
# (You can modify the tree easily)
# -----------------------------------------------------------

# Tree structure:
#       A
#     /   \
#    B     C
#   / \   / \
#  D  E  F   G

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"]
}

# Leaf node values
values = {
    "D": 3,
    "E": 5,
    "F": 6,
    "G": 9,
}

# -----------------------------------------------------------
# Run Alpha-Beta
# -----------------------------------------------------------

best_score = alphabeta("A", 0, -math.inf, math.inf, True, values, tree)

print("Best achievable score for maximizer:", best_score)
