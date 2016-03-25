# -*- coding: utf-8 -*-

from collections import deque
from search_node import Node, Reverse_node, compose_solution

def biBFGSearch(problem):
    """
    Bidirectional BFGS Search for revertible problems
    
    Returns a list of actions that lead from 
    problem.initial_state to problem.goal
    Or None if no such solution exists
    
    """
    initial_node = Node(problem)
    if problem.goal_test(problem.initial_state):
        return initial_node.solution()
        
    init_frontier = deque()
    init_frontier.append(initial_node)
    init_frontier_set = set()
    init_frontier_set.add(initial_node.state)
    
    goal_node = Reverse_node(problem)
    
    goal_frontier = deque()
    goal_frontier.append(goal_node)
    goal_frontier_set = set()
    goal_frontier_set.add(goal_node.state)
    
    explored = set()
    
    while init_frontier and goal_frontier:
        #Forward search
        other_init_frontier = deque()
        #We explore the next depth and then pass the baton
        while init_frontier:
            node = init_frontier.popleft()
            init_frontier_set.remove(node.state)
            explored.add(node.state)
            for action in problem.actions(node.state):
                child = node.child(problem, action)
                if child.state in goal_frontier_set:
                    return compose_solution(
                        child, pick(goal_frontier, child.state))
                if not child.state in explored and \
                not child.state in init_frontier_set:
                    other_init_frontier.append(child)
                    init_frontier_set.add(child.state)
        init_frontier = other_init_frontier
        
        #Backward search
        other_goal_frontier = deque()
        #We explore the next depth and then pass the baton
        while goal_frontier:
            node = goal_frontier.popleft()
            goal_frontier_set.remove(node.state)
            explored.add(node.state)
            for state, action in problem.predecessors(node.state):
                parent = node.parent(problem, state, action)
                if parent.state in init_frontier_set:
                    return compose_solution(
                        pick(init_frontier, parent.state), parent)
                if not parent.state in explored and \
                not parent.state in goal_frontier_set:
                    other_goal_frontier.append(parent)
                    goal_frontier_set.add(parent.state)
        goal_frontier = other_goal_frontier
        
    return None
    

def pick(deque, state):
    for node in deque:
        if node.state == state: 
            return node
    raise NoSuchElement

class NoSuchElement(Exception):
    pass

if True:
    import logging
    from problems.fifteen_problem import Fifteen_problem
    from BFGSearch import BFGSearch
    logging.basicConfig(filename='biBFGSearch.log',level=logging.DEBUG)
    for i in range(10):
        p = Fifteen_problem(size=3, difficulty=50)
        ins = p.initial_state
        logging.info("about to start instance\n {}.\nSolvable: {}".format(p.initial_state, p.solvable()))
        logging.debug("Tuple representation: {}".format(p.initial_state.state))        
        logging.info("BFGSearch")
        solution = BFGSearch(p)
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
        logging.info("biBFGSearch")
        solution = biBFGSearch(p)
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
        