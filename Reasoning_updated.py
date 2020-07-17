
class Proposition:
    def __init__(self, quantifier, subject, predicate):
        self.quantifier = quantifier
        self.subject = subject
        self.predicate = predicate


def implies_only_alls(premises, query):
    # Assumption: quantifiers of the propositions are ALL
    list = [query.subject]

    changed = True
    while changed:
        changed = False
        for premise in premises:
            if premise.subject in list:
                if premise.predicate not in list:
                    list.append(premise.predicate)
                    changed = True

    if query.predicate in list:
        return True
    else:
        return False

def implies_only_nos(premises, query):
    # Assumption: quantifiers of the propositions are NO
    for premise in premises:
        p_sub = premise.subject
        p_pre = premise.predicate
        q_sub = query.subject
        q_pre = query.predicate
        if p_sub == q_sub and p_pre == q_pre:
            return True
        elif p_sub == q_pre and p_pre == q_sub:
            return True
    return False

#def implies(premises, query):
#    ?

p_1 = Proposition("No", "X", "Y")

p1 = Proposition("All","X","Y") #("All", "X", "Y") # "All X are Y"
p2 = Proposition("All","Z","W") #("All", "Z", "W") # "All Z are W"
p3 = Proposition("All","Y","W") #("All", "Y", "W") # "All Y are W"
p4 = Proposition("All","W","A") #("All", "W", "A") # "All W are A"
p5 = Proposition("All","W","B") #("All", "W", "B") # "All W are B"
p6 = Proposition("All","D","A") #("All", "D", "A") # "All D are A"
p7 = Proposition("All","B","C") # ("All", "B", "C") # "All B are C"

premises = [p1, p2, p3, p4, p5, p6, p7]

query1 = Proposition("All","X","C") # ("All", "X", "C") # "All X are C"
query2 = Proposition("All","A","X") #("All", "C", "X")
query3 = Proposition("All","X","A") #("All", "X", "A")
query4 = Proposition("All","X","D") #("All", "X", "D")

print(implies_only_alls(premises, query1))
print(implies_only_alls(premises, query2))
print(implies_only_alls(premises, query3))
print(implies_only_alls(premises, query4))

# TODO:
# 1) Find all possible conclusions (only input is the premises)
# 2) Implement "implies" when we can have both All and No
# 3) Implement knowledge representation and automated reasoning for relatives:
# premise1 = Proposition("brother","X","Y") # X is brother of Y
# premise2 = Proposition("father","Z","X")
# premises = [premise1, premise2]
# query = Proposition("father","Z","Y")
# print(implies(premises,query))
# brother, sister, sibling, father, mother, parent, grandfather, grandmother,
# grandparent, son, daughter, child, grandchild, uncle, aunt, etc.
# There will be assumptions: there is no step father etc.