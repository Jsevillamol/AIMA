# -*- coding: utf-8 -*-

def LFIDSearch(problem):
    """Loop Free Iterative Deepening Search"""
    l = 0    
    while True:
        l+=1
        print("Depth: "+str(l))
        solution = LDFSearch(problem, l)
        if solution: return solution
            
def LFLDFSearch(problem, l):
    return recursiveLFLDFSearch(problem, l, Node(problem), set(problem.initial_state))
    
def recursiveLFLDFSearch(problem, l, node, current_path):
    if l == 0: return False
    else: 
        if problem.goal_test(node.state): return node.solution()
        successors = problem.actions(node.state)
        cutoff = False
        while successors:
            child = node.child(problem, successors.pop())
            if not child.state in current_path:
                current_path.add(child.state)
                solution = recursiveLFLDFSearch(problem, l-1, child)
                if solution: return solution
                elif solution == False: cutoff = True
                current_path.remove(child.state)
        return False if cutoff else None