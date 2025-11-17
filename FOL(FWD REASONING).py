# -------------------------------------------
# Forward Chaining Rule Engine (Horn Clauses)
# -------------------------------------------

class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, premises, conclusion):
        self.rules.append((premises, conclusion))

    def forward_chain(self, query):
        inferred = set()
        added = True

        while added:
            added = False

            for premises, conclusion in self.rules:
                # check if rule can fire
                if all(p in self.facts for p in premises):
                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        inferred.add(conclusion)
                        added = True

                if query in self.facts:
                    return True
        
        return query in self.facts


# -------------------------------------------
# Example KB (First Order–style facts)
# -------------------------------------------

kb = KnowledgeBase()

# Facts
kb.add_fact("Human(Socrates)")
kb.add_fact("Human(Plato)")

# Rules (FOL Horn clauses)
# Human(x) → Mortal(x)
kb.add_rule(["Human(Socrates)"], "Mortal(Socrates)")
kb.add_rule(["Human(Plato)"], "Mortal(Plato)")

# Query
query = "Mortal(Socrates)"

# Reason
result = kb.forward_chain(query)

print("Query:", query)
print("Is it entailed by the KB?:", result)
print("Final Facts in KB:", kb.facts)
