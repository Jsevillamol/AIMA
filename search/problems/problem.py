# -*- coding: utf-8 -*-

class Problem():
    """
    Abstract Problem class
    """
    def __init__(self):
        """must define goal_state and initial_state"""
        self.goal_state = None
        self.initial_state = None
        raise NotImplemented
        
    def goal_test(self, state)->bool:
        """
        Returns True if state is a goal state
        """
        raise NotImplemented
    
    def actions(self, state):
        """
        Returns an iterable over actions in state
        """
        raise NotImplemented  
    
    def result(self, state, action):
        """
        Returns the result of applying action to state
        """
        raise NotImplemented   
    
    def valid(self, state, action)->bool:
        """
        Returns true if action is applicable to state.
        By default is True.
        """
        return True
        
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
    
    def __repr__(self)->str:
        """
        Returns the name of the problem, plus additional info
        """
        raise NotImplemented