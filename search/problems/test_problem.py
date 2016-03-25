# -*- coding: utf-8 -*-

class Test_problem():
    def __init__(self, goal = 21):
        self.goal = goal
        self.initial_state = 0
        
    def goal_test(self, state)->bool:
        return state == self.goal
    
    def actions(self, state):
        return [1,2,3]
    
    def cost(self, state, action):
        return 1
    
    def result(self, state, action):
        return state + action