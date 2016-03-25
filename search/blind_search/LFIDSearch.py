# -*- coding: utf-8 -*-
import logging
from search_node import Node

def LFIDSearch(problem):
    """Loop Free Iterative Deepening Search"""
    l = 0    
    while True:
        l+=1
        logging.debug("Depth: "+str(l))
        solution = LFLDFSearch(problem, l)
        if solution != False: return solution
            
def LFLDFSearch(problem, l):
    "Loop Free Limited Depth First Search"
    return recursiveLFLDFSearch(problem, l, Node(problem), set(problem.initial_state))
    
def recursiveLFLDFSearch(problem, l, node, current_path):
    if l == 0: return False
    else: 
        if problem.goal_test(node.state): return node.solution()
        cutoff = False
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if not child.state in current_path:
                current_path.add(child.state)
                solution = recursiveLFLDFSearch(problem, l-1, child, current_path)
                if solution: return solution
                elif solution == False: cutoff = True
                current_path.remove(child.state)
        return False if cutoff else None
        
if True:#__name__ == "__Main__":
    from problems.fifteen_problem import Fifteen_problem
    from BFGSearch import BFGSearch
    logging.basicConfig(filename='LFIDSearch.log',level=logging.INFO)
    for i in range(10):
        p = Fifteen_problem(size=3)
        ins = p.initial_state
        logging.info("about to start instance\n {}.\nSolvable: {}".format(p.initial_state, p.solvable()))
        logging.info("BFGSearch")
        solution = BFGSearch(p)
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
        logging.info("LFIDSearch")
        solution = LFIDSearch(p)
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))