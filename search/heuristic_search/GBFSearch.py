# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 01:05:40 2016

@author: jsevillamol
"""

from search_node import Node, Priority_Queue

def GBFSearch(problem): #Untested
    """
    Greedy Best-First Search
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
                frontier.push(child, problem.h(child.state))
        
    return None
    