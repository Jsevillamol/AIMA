# -*- coding: utf-8 -*-

class Problem():
    """
    Problem class
    """
    def __init__(self):
        """must define goal and initial_state"""
        self.goal = None
        self.initial_state = None
        
    def goal_test(self, state)->bool:
        """
        Returns True if state is a goal state
        """
        raise NotImplemented
    
    def actions(self, state):
        """
        Returns the available actions in state
        """
        raise NotImplemented  
    
    def result(self, state, action):
        """
        Returns the result of applying action to state
        """
        raise NotImplemented   
    
    def valid(self, state, action)->bool:
        """
        Returns true if action is applicable to state
        """
        return True
        
    def cost(self, state, action):
        """
        Returns the cost of applying action to state
        """
        return 1