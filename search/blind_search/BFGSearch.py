# -*- coding: utf-8 -*-
from collections import deque

from search_node import Node

#Breadth-First Graph Search
def BFGSearch(problem):
    Node.reset()
    initial_node = Node(problem)
    if problem.goal_test(initial_node.state): 
        return initial_node.solution()
    frontier = deque()
    frontier.append(initial_node)
    explored = set()#states we have already explored
    #pdb.set_trace()
    while frontier:
        node = frontier.popleft()
        Node.check(len(frontier)+len(explored))
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if not child.state in explored: 
                if problem.goal_test(child.state): 
                    return child.solution()
                frontier.append(child)
    return None
    