# -*- coding: utf-8 -*-


#Solves problems by searching
#Only useful for deterministic, known, fully observable environments

from collections import deque

class Node():
    def __init__(self, problem = None):
        self.state = problem and problem.initial_state
        self.parent = None
        self.action = None
        self.path_cost = 0
    
    def child(self, problem, action):
        """Creates a child node of self applying specified action"""
        node = Node()
        node.state = problem.result(self.state, action)
        node.parent = self
        node.action = action
        node.path_cost = self.path_cost + problem.cost(self.state, action)
        return node
        
    def solution(self):
        """Returns the chain of actions which leads to this node"""
        node = self
        solution = deque()
        while node.parent != None:
            solution.appendleft(node.action)
            node = node.parent
        return solution
        
    def reverse_path(self):
        """generates the reverse path that leads to this node"""
        node = self
        yield self
        while node.parent != None:
            yield node.parent
            node = node.parent
    
    def copy(self):
        new = Node()
        new.state = self.state
        new.action = self.action
        new.parent = self.parent
        new.path_cost = self.path_cost
        return new
        
    def __iter__(self):#does not work
        node = Node()
        node.parent = self
        return node
    
    def __next__(self):#does not work
        if self.parent != None:     
            self.state = self.parent.state
            self.action = self.parent.action
            self.path_cost = self.parent.path_cost  
            self.parent = self.parent.parent
             
        return self
    
    def __repr__(self):
        return "state:{}, path_cost:{}, path:{}".format(
            self.state, self.path_cost, self.solution())

class Reverse_node():
    """
    Nodes which store a path to a goal_state
    """
    def __init__(self, problem = None):
        self.state = problem and problem.goal_state
        self.child = None
        self.action = None
        self.path_cost = 0
    
    def parent(self, problem, parent_state, action):
        """Creates a parent for backward search."""
        node = Reverse_node()
        node.state = parent_state
        node.child = self
        node.action = action
        node.path_cost = self.path_cost + problem.cost(parent_state, action)
        return node
    
    def solution(self):
        """
        Returns the path of actions from current node to goal.
        """
        solution = []
        node = self
        while node.child != None:
            solution.append(node.action)
            node = node.child
        return solution
        
    def __repr__(self):
        return "state:{}, path_cost:{}, path:{}".format(
            self.state, self.path_cost, self.solution())

def compose_solution(forward_node, backward_node):
        """Combines a forward path and a backward path sharing the same last node."""
        solution = forward_node.solution()
        solution.extend(backward_node.solution())
        return solution

import logging
        
def log_evolution(problem, solution):
    logging.basicConfig(filename='problemEvo.log',level=logging.DEBUG)
    logging.info(problem)
    logging.info(problem.initial_state)
    state = problem.initial_state
    for act in solution:
        state = problem.result(state,act)
        logging.info("Action= {}".format(act))
        logging.info(state)

