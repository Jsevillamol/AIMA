# -*- coding: utf-8 -*-
import numpy as np

class Fifteen_problem():
    def __init__(self, state = None, size = 3):
        self.size = size
        if state == None: self.generate_solvable_state()
        else:
            self.initial_state = state
            self.size = len(state)
            if not self.solvable(): 
                raise "UnsolvablePuzzle"
                
        self.goal = tuple([tuple(range(i*self.size,i*self.size+self.size)) 
                     for i in range(self.size)])

    def solvable(self):
        perm = sum(self.initial_state, ())
        #This could be very wrong
        return (parity(perm) + index_2d(self.initial_state, 0)[0] + self.size)%2 == 0
            
        return True
        
    def generate_solvable_state(self):
        while True:
            permutation = tuple(np.random.permutation(self.size*self.size))
            self.initial_state = tuple([permutation[i*self.size:i*self.size+self.size] for i in range(self.size)])
            if(self.solvable()): break
    
    def goal_test(self, state)->bool:
        return state == self.goal      
    
    def actions(self, state):
        (x,y) = index_2d(state, 0)
        actions = []
        for direction, (d1,d2) in directions.items():
            if 0<=x+d1<self.size and 0<=y+d2<self.size:
                actions.append(direction)
        return actions
        
    def cost(self, state, action):
        return 1
    
    def result(self, state, action):
        new_state = [list(row) for row in state]
        x,y = index_2d(new_state,0)
        d1,d2 = directions[action]
        new_state[x][y], new_state[x+d1][y+d2] = new_state[x+d1][y+d2], new_state[x][y]
        return tuple([tuple(row) for row in new_state])

directions = {
        "up":    ( 1, 0),
        "down":  (-1, 0),
        "right": ( 0,-1),
        "left":  ( 0, 1)
    }

def parity(permutation):
    to_visit = list(range(len(permutation)))
    parity = 0
    while to_visit:
        aux = to_visit.pop()
        while(permutation[aux] in to_visit):
            parity += 1
            aux = permutation[aux]
            to_visit.remove(aux)
    return parity%2
    
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))