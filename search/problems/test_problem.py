# -*- coding: utf-8 -*-

from problems.problem import Problem

class Test_problem(Problem):
    """
    Problem for testing.
    The initial state is 0. Actions are sum 1, sum 2 or sum 3.
    The goal is reaching a certain number, 
    """
    def __init__(self, goal = 21):
        self.goal_state = goal
        self.initial_state = 0
        
    def goal_test(self, state)->bool:
        """
        Returns True if state is a goal state
        """
        return state == self.goal_state
    
    def actions(self, state):
        """
        Returns a generator over the available actions in state
        """
        return [1,2,3]
    
    def result(self, state, action):
        """
        Returns the result of applying action to state
        """
        return state + action    
    
    def predecessors(self, state):
        return [(state-1, 1), (state-2, 2), (state-3, 3)]
    
    def __repr__(self):
         return "Test problem: Init={} Goal={}".format(self.initial_state, self.goal_state)
    
    