# -*- coding: utf-8 -*-
from collections import deque

from search_node import Node

#Breadth-First Graph Search
def BFGSearch(problem):
    initial_node = Node(problem)
    if problem.goal_test(initial_node.state): 
        return initial_node.solution()
    frontier = deque()
    frontier.append(initial_node)
    explored = set()
    #pdb.set_trace()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if not child.state in explored: 
                if problem.goal_test(child.state): 
                    return child.solution()
                frontier.append(child)
    return None
    
if False:#__name__ == "__Main__":
    from problems.fifteen_problem import Fifteen_problem, Fifteen_puzzle_state
    import logging
    logging.basicConfig(filename='BFGSearch.log',level=logging.DEBUG)
    p = Fifteen_problem()
    p.initial_state = Fifteen_puzzle_state(((0, 3, 5), (2, 1, 6), (4, 7, 8))) 
    logging.info("about to start instance {}. Solvable: {}".format(p.initial_state, p.solvable()))
    solution = BFGSearch(p)
    logging.info("The solution is {}".format(solution))
    p.initial_state = Fifteen_puzzle_state(((3, 0, 5), (2, 1, 6), (4, 7, 8)))  
    logging.info("about to start instance {}. Solvable: {}".format(p.initial_state, p.solvable()))
    solution = BFGSearch(p)
    logging.info("The solution is {}".format(solution))
    for i in range(10):
        p = Fifteen_problem(size=3)
        ins = p.initial_state
        logging.info("about to start instance\n {}.\nSolvable: {}".format(p.initial_state, p.solvable()))
        solution = BFGSearch(p)
        logging.info("The solution is {}".format(solution))