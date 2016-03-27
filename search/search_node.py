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
        self.f_value = problem.h(self.state) if problem else None
    
    def child(self, problem, action):
        """Creates a child node of self applying specified action"""
        node = Node()
        node.state = problem.result(self.state, action)
        node.parent = self
        node.action = action
        node.path_cost = self.path_cost + problem.cost(self.state, action)
        node.f_value = node.path_cost + problem.h(node.state)
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
        return "state:{}, path_cost:{}, f_value:{}, path:{}".format(
            self.state, self.path_cost, self.f_value, self.solution())
    
    node_count = None
    def count():
        Node.node_count+=1
        
    def reset():
        Node.node_count = 0

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

import heapq
import itertools
class Priority_Queue:
    """
    Priority Queue for Search_nodes with efficient membership test.
    Returns node with lower f-cost on pop.
    If a repeated node is inserted, only the one with lower f-cost is retained.
    Keeps track of # of nodes processed through index.
    """
    REMOVED = '<removed-node>'
    def __init__(self):
        """
        Constructs a new queue.
        Cost: constant
        """
        self._queue = []
        self._node_finder = {}
        self._index = itertools.count()
        self._n = 0
    
    def push(self, node, f_cost):
        """
        Adds node to queue. 
        If there is another node with the same state but higher f-cost, it is
        replaced.
        """
        if node in self:
            old_f_cost, index, old_node = self._node_finder[node.state]
            if old_f_cost > f_cost:
                self.remove(node)
                entry = [f_cost, next(self._index), node]
                self._node_finder[node.state] = entry
                heapq.heappush(self._queue, entry)
                self._n += 1
            
        else:
            entry = [f_cost, next(self._index), node]
            self._node_finder[node.state] = entry
            heapq.heappush(self._queue, entry)
            self._n+=1
    
    def remove(self, node):
        """
        Removes node with same state as arg
        """
        entry = self._node_finder.pop(node.state)
        entry[-1] = Priority_Queue.REMOVED
        self._n -= 1
    
    def pop(self):
        while self._queue:
            entry = heapq.heappop(self._queue)
            if entry[-1] is not Priority_Queue.REMOVED:
                node = entry[-1]
                self.remove(node)
                return node
        raise KeyError("Empty queue!")
            
    def __len__(self):
        return self._n
    
    def __contains__(self, node):
        return node.state in self._node_finder
    """
    def __nonzero__(self):
        while self._queue and self._queue[0][-1] is Priority_Queue.REMOVED:
            heapq.heappop(self._queue)
        return bool(self._queue)"""
    
    def __repr__(self):
        return repr(self._queue)
    
    