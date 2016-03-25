# -*- coding: utf-8 -*-

from collections import deque

from search_node import Node

#Breadth-First Tree Search
def BFTSearch(problem):
    initial_node = Node(problem)
    if problem.goal_test(initial_node.state): 
        return initial_node.solution()
    frontier = deque()
    frontier.append(initial_node)
    while frontier:
        node = frontier.popleft()
        for action in problem.actions(node.state):
            child = node.child(problem, action) 
            if problem.goal_test(child.state): 
                return child.solution()
            frontier.append(child)
    return None
    
if True:#__name__ == "__Main__":
    from problems.fifteen_problem import Fifteen_problem
    import logging
    logging.basicConfig(filename='BFTSearch.log',level=logging.DEBUG)
    ins = ((0, 3, 5), (2, 1, 6), (4, 7, 8))    
    p = Fifteen_problem(ins)
    logging.info("about to start instance {}. Solvable: {}".format(p.initial_state, p.solvable()))
    solution = BFTSearch(p)
    logging.info("The solution is {}".format(solution))
    p.initial_state = ((3, 0, 5), (2, 1, 6), (4, 7, 8))  
    logging.info("about to start instance {}. Solvable: {}".format(p.initial_state, p.solvable()))
    solution = BFTSearch(p)
    logging.info("The solution is {}".format(solution))
    for i in range(10):
        p = Fifteen_problem()
        ins = p.initial_state
        logging.info("about to start instance {}. Solvable: {}".format(p.initial_state, p.solvable()))
        solution = BFTSearch(p)
        logging.info("The solution is {}".format(solution))