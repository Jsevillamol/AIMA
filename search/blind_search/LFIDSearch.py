# -*- coding: utf-8 -*-

from search_node import Node

def LFIDSearch(problem, l=1):
    """Loop Free Iterative Deepening Search"""
    Node.reset()
    while True:
        #logging.debug("Depth: "+str(l))
        solution = LFLDFSearch(problem, l)
        if solution != False: return solution
        l+=1
            
def LFLDFSearch(problem, l):
    "Loop Free Limited Depth First Search"
    return recursiveLFLDFSearch(problem, l, Node(problem), set(problem.initial_state), 1)
    
def recursiveLFLDFSearch(problem, l, node, current_path, n_nodes):    
    if l == 0: return False
    else: 
        Node.check(n_nodes)
        if problem.goal_test(node.state): return node.solution()
        cutoff = False
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if not child.state in current_path:
                current_path.add(child.state)
                solution = recursiveLFLDFSearch(problem, l-1, child, current_path, n_nodes+1)
                if solution: return solution
                elif solution == False: cutoff = True
                current_path.remove(child.state)
        return False if cutoff else None
        