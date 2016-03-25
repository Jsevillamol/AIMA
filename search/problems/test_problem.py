# -*- coding: utf-8 -*-

class Test_problem():
    """
    Problem for testing.
    The initial state is 0. Actions are sum 1, sum 2 or sum 3.
    The goal is reaching a certain number, 
    """
    def __init__(self, goal = 21):
        self.goal = goal
        self.initial_state = 0
        
    def goal_test(self, state)->bool:
        """
        Returns True if state is a goal state
        """
        return state == self.goal
    
    def actions(self, state):
        """
        Returns the available actions in state
        """
        return [1,2,3]    
    
    def result(self, state, action):
        """
        Returns the result of applying action to state
        """
        return state + action    
    
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
    
    