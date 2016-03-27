# -*- coding: utf-8 -*-

from search_node import Node, Priority_Queue

def UCGSearch(problem):
    """Uniform Cost Graph Search Algorithm
    """
    Node.reset()
    initial_node = Node(problem)
    if problem.goal_test(problem.initial_state): 
        return initial_node.solution()
    
    frontier = Priority_Queue()
    frontier.push(initial_node, 0)
    explored = set()
    
    while frontier:
        node = frontier.pop()
        Node.count()
        if problem.goal_test(node.state): return node.solution()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem,action)
            if not child.state in explored: 
                frontier.push(child, child.path_cost)
        
    return None
