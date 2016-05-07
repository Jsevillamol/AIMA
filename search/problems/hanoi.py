# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 09:33:45 2016

@author: jsevillamol
"""

# -*- coding: utf-8 -*-

class HanoiProblem():
    """
    Hanoi puzzle
    """
    def __init__(self, n=3, init = None):
        """must define goal_state and initial_state"""
        self.size = n
        self.goal_state = ((),(),tuple((range(n-1,-1,-1))))
        if init != None: self.initial_state = init
        else: self.initial_state = (tuple((range(n-1,-1,-1))),(),())
        
    def goal_test(self, state)->bool:
        """
        Returns True if state is a goal state
        """
        return self.goal_state == state
    
    def actions(self, state):
        """
        Returns an iterable over actions in state
        """
        actions = []
        for move in [(i,j) for i in range(3) for j in range(3) if i!=j]:
            if self.valid(state, move): actions.append(move)
        return actions
    
    def result(self, state, action):
        """
        Returns the result of applying action to state
        """
        new_state = list([list(stack) for stack in state])
        disk = new_state[action[0]].pop()
        new_state[action[1]].append(disk)
        return tuple([tuple(stack) for stack in new_state])
    
    def valid(self, state, action)->bool:
        """
        Returns true if action is applicable to state.
        By default is True.
        """
        return state[action[0]] and (not state[action[1]] or state[action[1]] > state[action[0]])
        
    def cost(self, state, action):
        """
        Returns the cost of applying action to state.
        By default is 1.
        """
        return 1
    
    def successors(self, state):
        """
        Returns an iterable of state/actions reachable from this state.
        By default constructs an iterable from actions() and result()
        """
        return ((self.result(state,action), action) for action in self.actions(state))
    
    def predecessors(self, state):
        """
        Returns an iterable of state/actions pairs which lead to this state.
        
        Used for bidirectional search.
        """
        raise NotImplemented
    
    def h(self, state)   :
        """
        Returns a heuristic cost for a state.
        
        By default is 0.
        
        In order to work with Heuristic Tree Search should be admissible:
        the heuristic cost must be a lower bound of an optimal path leading 
        from state to a goal state.
        
        In order to work with Heuristic Graph Searchs h should be consistent:
        h(n) <= c(n,n') + h(n'), where n is a node, c is the step cost function
        and n' a successor of n.
        """
        return 0
    
    def __repr__(self)->str:
        """
        Returns the name of the problem, plus additional info
        """
        return "Hanoi problem, size {}, initial state {}".format(self.size, self.initial_state)