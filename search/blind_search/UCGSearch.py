# -*- coding: utf-8 -*-

from search_node import Node, Priority_Queue

def UCGSearch(problem):
    """Uniform Cost Graph Search Algorithm
    """
    initial_node = Node(problem)
    if problem.goal_test(problem.initial_state): 
        return initial_node.solution()
    
    frontier = Priority_Queue()
    frontier.push(initial_node, 0)
    explored = set()
    
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state): return node.solution()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem,action)
            if not child.state in explored: 
                frontier.push(child, child.path_cost)
        
    return None

if False:
    import logging
    from problems.fifteen_problem import Fifteen_problem
    from BFGSearch import BFGSearch
    logging.basicConfig(filename='UCGSearch.log',level=logging.DEBUG)
    for i in range(10):
        p = Fifteen_problem(size=3, difficulty=10)
        ins = p.initial_state
        logging.info("about to start instance\n {}.\nSolvable: {}".format(p.initial_state, p.solvable()))
        logging.debug("Tuple representation: {}".format(p.initial_state.state))   
        logging.info("BFGSearch")
        solution = BFGSearch(p)
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
        logging.info("UCGSearch")
        solution = UCGSearch(p)
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))