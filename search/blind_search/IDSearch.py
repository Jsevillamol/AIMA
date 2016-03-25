ID# -*- coding: utf-8 -*-

#from search_node import Node

def IDSearch(problem):
    """Iterative Deepening Search"""
    l = 0    
    while True:
        l+=1
        print("Depth: "+str(l))
        solution = LDFSearch(problem, l)
        if solution: return solution
            
def LDFSearch(problem, l):
    return recursiveLDFSearch(problem, l, Node(problem))
    
def recursiveLDFSearch(problem, l, node):
    if l == 0: return False
    else: 
        if problem.goal_test(node.state): return node.solution()
        successors = problem.actions(node.state)
        cutoff = False
        while successors:
            child = node.child(problem, successors.pop())
            solution = recursiveLDFSearch(problem, l-1, child)
            if solution: return solution
            elif solution == False: cutoff = True
        return False if cutoff else None