# -*- coding: utf-8 -*-
from collections import deque
import pdb

#from search_node import Node

#Breadth-First Graph Search
def BFGSearch(problem):
    initial_node = Node(problem)
    if problem.goal_test(initial_node.state): 
        return initial_node.solution()
    frontier = deque()
    frontier.append(initial_node)
    explored = set()
    pdb.set_trace()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if not child.state in explored: 
                if problem.goal_test(child.state): return child.solution()
                frontier.append(child)
    return None