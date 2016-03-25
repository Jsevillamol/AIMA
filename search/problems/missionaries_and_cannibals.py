# -*- coding: utf-8 -*-


#import pdb
class Missionaries_and_Cannibals:
    left = True
    right = False
    def __init__(self, size = 3, boat_size = 2):
        self.initial_state = MaC_state(((size,size), (0,0)), MaC.left)
        self.goal_state = MaC_state(((0,0), (size,size)), MaC.right)
        self.size = size
        self.boat_size = boat_size
        
    def goal_test(self, state)->bool:
        return state == self.goal_state
    
    def actions(self, state):
        actions = []
        #pdb.set_trace()
        for action in [(i,j) for i in range(self.boat_size+1) for j in range(self.boat_size+1) if 0<i+j<=self.boat_size]:
            res = self.result(state, action)
            if (0 <= res.river[0][1] <= res.river[0][0] or 0 == res.river[0][0]<=res.river[0][1]) \
            and (0 <= res.river[1][1] <= res.river[1][0] or 0 == res.river[1][0]<=res.river[1][1]):
                actions.append(action)
        return actions
        
    
    def cost(self, state, action):
        return 1
    
    def result(self, state, action):
        river = state.river
        if state.boat == MaC.left:
            river = (tuple([river[0][i]-action[i] for i in range(2)]), 
                     tuple([river[1][i]+action[i] for i in range(2)]))
            boat = MaC.right
        elif state.boat == MaC.right:
            river = (tuple([river[0][i]+action[i] for i in range(2)]), 
                     tuple([river[1][i]-action[i] for i in range(2)]))
            boat = MaC.left
        return MaC_state(river, boat)
    
    def __repr__(self):
        return "MaC \ninit = {}".format(self.initial_state)
    
MaC = Missionaries_and_Cannibals
        
class MaC_state:
    def __init__(self, river, boat):
        self.river = river
        self.boat = boat
    
    def __eq__(self, other):
        return self.river == other.river and self.boat == other.boat
    
    def __repr__(self):
        return "{} |{}| {}".format(self.river[0], 
              "B   " if self.boat else "   B", self.river[1])
    def __hash__(self):
        return hash((self.river, self.boat))