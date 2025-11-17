# ---------------------------------------------------------
# Simple FOL Resolution Theorem Prover in Python (CNF based)
# ---------------------------------------------------------

import itertools

def negate_literal(literal):
    """Negate a literal."""
    if literal.startswith("¬"):
        return literal[1:]
    else:
        return "¬" + literal

def resolve(ci, cj):
    """
    Resolve two clauses ci and cj. 
    Each clause = set of literals.
    Returns resolvents (list of new clauses).
    """
    resolvents = []

    for li in ci:
        for lj in cj:
            if li == negate_literal(lj):
                # Remove complementary literals and unite rest
                new_clause = (ci - {li}) | (cj - {lj})
                resolvents.append(new_clause)

    return resolvents


def resolution(kb, query):
    """
    Resolution refutation:
    KB ∧ ¬Query ⊢ ⊥  (empty clause)
    """
    clauses = kb.copy()
    clauses.append({negate_literal(query)})

    new = set()

    while True:
        pairs = list(itertools.combinations(clauses, 2))

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)

            for r in resolvents:
                if len(r) == 0:  # empty clause found
                    return True
                new.add(frozenset(r))

        new_clauses = [set(c) for c in new]

        # If no new clauses, proof fails
        if all(c in clauses for c in new_clauses):
            return False

        # Add new clauses to KB
        for c in new_clauses:
            if c not in clauses:
                clauses.append(c)


# ---------------------------------------------------------
# Example Knowledge Base (CNF)
# ---------------------------------------------------------

# 1. Human(Socrates)
# 2. ∀x Human(x) → Mortal(x)
# Query: Mortal(Socrates)

# After CNF conversion:
kb = []

# Human(Socrates)
kb.append({"Human(Socrates)"})

# ¬Human(x) ∨ Mortal(x)
# Instantiate for Socrates
kb.append({"¬Human(Socrates)", "Mortal(Socrates)"})


# ---------------------------------------------------------
# Run Resolution
# ---------------------------------------------------------

query = "Mortal(Socrates)"
result = resolution(kb, query)

print("Query:", query)
print("Is the query entailed by the KB (Resolution)?", result)
