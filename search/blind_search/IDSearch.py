# -*- coding: utf-8 -*-

from search_node import Node

def IDSearch(problem, l=1):
    """Iterative Deepening Search"""
    while True:
        Node.reset()
        #print("Depth: "+str(l))
        solution = LDFSearch(problem, l)
        if solution != False: return solution
        l+=1
            
def LDFSearch(problem, l):
    """
    Limited Depth-First Search.
    """
    def recursiveLDFSearch(problem, l, node):
        if l == 0: return False
        else: 
            Node.count()
            if problem.goal_test(node.state): return node.solution()
            cutoff = False
            for action in problem.actions(node.state):
                child = node.child(problem, action)
                solution = recursiveLDFSearch(problem, l-1, child)
                if solution: return solution
                elif solution == False: cutoff = True
            return False if cutoff else None
            
    return recursiveLDFSearch(problem, l, Node(problem))
    

        
