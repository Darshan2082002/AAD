import itertools 
variables = ['A', 'B',]
truth_values=list(itertools.product([True, False], repeat=len(variables)))
formulas = [
    ("p", lambda p, q: p),
    ("q", lambda p, q: q),
    ("¬p", lambda p, q: not p),
    ("¬q", lambda p, q: not q),
    ("p ∧ q", lambda p, q: p and q),
    ("p ∨ q", lambda p, q: p or q),
    ("p → q", lambda p, q: (not p) or q),
    ("q → p", lambda p, q: (not q) or p),
    ("p ↔ q", lambda p, q: p == q),
    ("p ⊕ q (XOR)", lambda p, q: p ^ q),
    ("¬(p ∧ q)", lambda p, q: not (p and q)),
    ("¬(p ∨ q)", lambda p, q: not (p or q)),
    ("(¬p) ∧ q", lambda p, q: (not p) and q),
    ("p ∧ (¬q)", lambda p, q: p and (not q)),
    ("(¬p) ∨ q", lambda p, q: (not p) or q),
    ("p ∨ (¬q)", lambda p, q: p or (not q)),
    ("(p → q) ∧ (q → p)", lambda p, q: ((not p) or q) and ((not q) or p)), # equivalence
    ("(p → q) ∨ (q → p)", lambda p, q: ((not p) or q) or ((not q) or p)),
    ("(p ∧ q) → (p ∨ q)", lambda p, q: (not (p and q)) or (p or q)),
    ("(p ∨ q) → (p ∧ q)", lambda p, q: (not (p or q)) or (p and q)),
]
formulas = [
    ("p", lambda p, q: p),
    ("q", lambda p, q: q),
    ("¬p", lambda p, q: not p),
    ("¬q", lambda p, q: not q),
    ("p ∧ q", lambda p, q: p and q),
    ("p ∨ q", lambda p, q: p or q),
    ("p → q", lambda p, q: (not p) or q),
    ("q → p", lambda p, q: (not q) or p),
    ("p ↔ q", lambda p, q: p == q),
    ("p ⊕ q (XOR)", lambda p, q: p ^ q),
    ("¬(p ∧ q)", lambda p, q: not (p and q)),
    ("¬(p ∨ q)", lambda p, q: not (p or q)),
    ("(¬p) ∧ q", lambda p, q: (not p) and q),
    ("p ∧ (¬q)", lambda p, q: p and (not q)),
    ("(¬p) ∨ q", lambda p, q: (not p) or q),
    ("p ∨ (¬q)", lambda p, q: p or (not q)),
    ("(p → q) ∧ (q → p)", lambda p, q: ((not p) or q) and ((not q) or p)), # equivalence
    ("(p → q) ∨ (q → p)", lambda p, q: ((not p) or q) or ((not q) or p)),
    ("(p ∧ q) → (p ∨ q)", lambda p, q: (not (p and q)) or (p or q)),
    ("(p ∨ q) → (p ∧ q)", lambda p, q: (not (p or q)) or (p and q)),
]
formulas = [
    ("p", lambda p, q: p),
    ("q", lambda p, q: q),
    ("¬p", lambda p, q: not p),
    ("¬q", lambda p, q: not q),
    ("p ∧ q", lambda p, q: p and q),
    ("p ∨ q", lambda p, q: p or q),
    ("p → q", lambda p, q: (not p) or q),
    ("q → p", lambda p, q: (not q) or p),
    ("p ↔ q", lambda p, q: p == q),
    ("p ⊕ q (XOR)", lambda p, q: p ^ q),
    ("¬(p ∧ q)", lambda p, q: not (p and q)),
    ("¬(p ∨ q)", lambda p, q: not (p or q)),
    ("(¬p) ∧ q", lambda p, q: (not p) and q),
    ("p ∧ (¬q)", lambda p, q: p and (not q)),
    ("(¬p) ∨ q", lambda p, q: (not p) or q),
    ("p ∨ (¬q)", lambda p, q: p or (not q)),
    ("(p → q) ∧ (q → p)", lambda p, q: ((not p) or q) and ((not q) or p)), # equivalence
    ("(p → q) ∨ (q → p)", lambda p, q: ((not p) or q) or ((not q) or p)),
    ("(p ∧ q) → (p ∨ q)", lambda p, q: (not (p and q)) or (p or q)),
    ("(p ∨ q) → (p ∧ q)", lambda p, q: (not (p or q)) or (p and q)),
]
formulas = [
    ("p", lambda p, q: p),
    ("q", lambda p, q: q),
    ("¬p", lambda p, q: not p),
    ("¬q", lambda p, q: not q),
    ("p ∧ q", lambda p, q: p and q),
    ("p ∨ q", lambda p, q: p or q),
    ("p → q", lambda p, q: (not p) or q),
    ("q → p", lambda p, q: (not q) or p),
    ("p ↔ q", lambda p, q: p == q),
    ("p ⊕ q (XOR)", lambda p, q: p ^ q),
    ("¬(p ∧ q)", lambda p, q: not (p and q)),
    ("¬(p ∨ q)", lambda p, q: not (p or q)),
    ("(¬p) ∧ q", lambda p, q: (not p) and q),
    ("p ∧ (¬q)", lambda p, q: p and (not q)),
    ("(¬p) ∨ q", lambda p, q: (not p) or q),
    ("p ∨ (¬q)", lambda p, q: p or (not q)),
    ("(p → q) ∧ (q → p)", lambda p, q: ((not p) or q) and ((not q) or p)), # equivalence
    ("(p → q) ∨ (q → p)", lambda p, q: ((not p) or q) or ((not q) or p)),
    ("(p ∧ q) → (p ∨ q)", lambda p, q: (not (p and q)) or (p or q)),
    ("(p ∨ q) → (p ∧ q)", lambda p, q: (not (p or q)) or (p and q)),
]

for name, formula in formulas:
    print(f"\nFormula: {name}")
    print("p\tq\tResult")
    for vals in truth_values:
        result = formula(*vals)
        print(f"{vals[0]}\t{vals[1]}\t{result}")