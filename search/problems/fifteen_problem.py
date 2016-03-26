# -*- coding: utf-8 -*-
import numpy as np
from random import choice

from problems.problem import Problem

class Fifteen_problem(Problem):
    """
    Classic sliding blocks puzzle.
    The objective is to arrange the tiles to form
    0 1 2 Where 0 is a blank.
    5 4 3
    6 7 8
    """
    def __init__(self, state = None, size = 3, difficulty=10):
        self.size = len(state) if state else size     
        self.difficulty = difficulty     
        self.goal_state = Fifteen_puzzle_state(wiggle(range(self.size**2)))
        
        if state == None: self.generate_solvable_state()
        else:
            self.initial_state = Fifteen_puzzle_state(state)
            if not self.solvable(): 
                raise Unsolvable

    def solvable(self):#Does not work
        perm = list(sum(self.initial_state, ()))
        perm = list(sum(wiggle(perm),()))
        perm.remove(0)
        
        return parity(perm)==0
        
        
    def generate_solvable_state(self):
        """while True:
            permutation = tuple(np.random.permutation(self.size*self.size))
            self.initial_state = Fifteen_puzzle_state(wiggle(permutation))
            if(self.solvable()): break"""
        self.initial_state = self.goal_state
        for i in range(self.difficulty):
            self.initial_state = self.result(self.initial_state,choice(list(self.actions(self.initial_state))))
    
    def goal_test(self, state)->bool:
        return state == self.goal_state      
    
    def actions(self, state):
        (x,y) = index_2d(state, 0)
        for direction, (d1,d2) in directions.items():
            if 0<=x+d1<self.size and 0<=y+d2<self.size:
                yield direction
        
    def cost(self, state, action):
        return 1
    
    def result(self, state, action):
        new_state = [list(row) for row in state]
        x,y = index_2d(new_state,0)
        d1,d2 = directions[action]
        new_state[x][y], new_state[x+d1][y+d2] = new_state[x+d1][y+d2], new_state[x][y]
        return Fifteen_puzzle_state(tuple([tuple(row) for row in new_state]))
    
    def predecessors(self, state):
        (x,y) = index_2d(state, 0)
        for direction, (d1,d2) in directions.items():
            if 0<=x+d1<self.size and 0<=y+d2<self.size:
                yield (self.result(state, direction), self.reverse_action(state, direction))
        
    
    def reverse_action(self, state, action):
        """
        returns the action which cancels the effect of action on state
        """
        if action == "up": return "down"
        if action == "down": return "up"
        if action == "left": return "right"
        if action == "right": return "left"
    
    def __repr__(self):
        return "{}-problem\ninit=\n{}".format(self.size**2-1, self.initial_state)
    
directions = {
        "up":    ( 1, 0),
        "down":  (-1, 0),
        "right": ( 0,-1),
        "left":  ( 0, 1)
    }

class Fifteen_puzzle_state:
    def __init__(self, state):
        self.state = state
    
    def __repr__(self):
        s = "---"*len(self.state) +"\n|"
        for i in range(len(self.state)):
            for j in range(len(self.state)):
                s += "{:2d}|".format(self.state[i][j])
            s += "\n"+"---"*len(self.state) +"\n|"
        return s[:-1]
    
    def __getitem__(self, index):
        return self.state[index]
    
    def __eq__(self, other):
        if not isinstance(other, Fifteen_puzzle_state): raise NotImplemented
        return self.state == other.state
    
    def __hash__(self):
        return hash(self.state)

class Unsolvable(Exception):
    pass

def parity(permutation):
    to_visit = set(range(1, len(permutation)+1))
    parity = 0
    while to_visit:
        init = aux = to_visit.pop()
        while permutation[aux-1] != init:
            parity += 1
            aux = permutation[aux-1]
            to_visit.remove(aux)
    return parity%2

import math

def wiggle(l):
    s = int(math.sqrt(len(l)))
    return tuple([tuple(l[i*s:(i+1)*s]) if i%2==0 
             else tuple(l[(i+1)*s-1:i*s-1:-1])
             for i in range(s)])

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))