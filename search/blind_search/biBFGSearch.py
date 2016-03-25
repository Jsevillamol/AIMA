# -*- coding: utf-8 -*-

from collections import deque
from search_node import Node

def biBFGSearch(problem):
    """Bidirectional BFGS Search for revertible problems"""
    initial_node = Node(problem)
    if problem.test_goal(problem.initial_state):
        return initial_node.solution()
    goal_node = Node()
    goal_node.initial_state = problem.goal
    
    init_frontier = deque()
    init_frontier.add(initial_node)
    goal_frontier = deque()
    goal_frontier.add(goal_node)
    explored = set()
    
    while init_frontier or goal_frontier:
        node = init_frontier.popleft()
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if child.state in goal_frontier.states??:
                return compose_solution(child, goal_frontier.pop("one which matches this"))
            if not child in explored
    