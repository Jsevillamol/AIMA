# -*- coding: utf-8 -*-

from search_node import Node

def IDSearch(problem):
    """Iterative Deepening Search"""
    l = 0    
    while True:
        l+=1
        #print("Depth: "+str(l))
        solution = LDFSearch(problem, l)
        if solution != False: return solution
            
def LDFSearch(problem, l):
    """
    Limited Depth-First Search.
    """
    return recursiveLDFSearch(problem, l, Node(problem))
    
def recursiveLDFSearch(problem, l, node):
    if l == 0: return False
    else: 
        if problem.goal_test(node.state): return node.solution()
        cutoff = False
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            solution = recursiveLDFSearch(problem, l-1, child)
            if solution: return solution
            elif solution == False: cutoff = True
        return False if cutoff else None
        
import logging

if False:#__name__ == "__Main__":
    from problems.fifteen_problem import Fifteen_problem
    from BFGSearch import BFGSearch
    logging.basicConfig(filename='IDSearch.log',level=logging.INFO)
    for i in range(10):
        p = Fifteen_problem(size=3)
        ins = p.initial_state
        logging.info("about to start instance\n {}.\nSolvable: {}".format(p.initial_state, p.solvable()))
        logging.info("BFGSearch")
        solution = BFGSearch(p)
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
        logging.info("LFIDSearch")
        solution = IDSearch(p)
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))

if False:     
    from problems.fifteen_problem import Fifteen_problem
    p = Fifteen_problem(((0,1,2),(5,4,3),(6,7,8)))
    print(IDSearch(p))
    