# -*- coding: utf-8 -*-
import numpy as np
from random import choice
from types import MethodType

from problems.problem import Problem

class Fifteen_problem(Problem):
    """
    Classic sliding blocks puzzle.
    The objective is to arrange the tiles to form
    0 1 2 Where 0 is a blank.
    3 4 5
    6 7 8
    """
    def __init__(self, state = None, size = 3, difficulty=10, h=lambda x,y: 0):
        self.size = len(state) if state else size     
        self.difficulty = difficulty     
        self.goal_state = Fifteen_puzzle_state(wiggle(range(self.size**2)))
        self.h = MethodType(h, self)
        
        if state == None: self.generate_solvable_state()
        else:
            self.initial_state = Fifteen_puzzle_state(state)
            if not self.solvable(): 
                raise Unsolvable

    def solvable(self):#Works I think?
        perm = list(sum(self.initial_state, ()))
        #perm = list(sum(wiggle(perm),()))
        perm.remove(0)
        
        return parity(perm) == 0
        #(parity(perm) + index_2d(self.initial_state, 0)[0]*(self.size-1))%2==0
        
    
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
    
    """
    Heuristics
    """
    
        
    def misplaced_tiles(self, state):
        misplaced_tiles = 0
        for x,y in coords(self.size):
            if state[x][y] != 0 and state[x][y]!=self.goal_state[x][y]:
                misplaced_tiles+=1
        return misplaced_tiles
    
    def manhattan_d(self,state):
        manhattan_d = 0
        for x,y in coords(self.size):
            if state[x][y] != 0:
                i,j = index_2d(self.goal_state, state[x][y])
                manhattan_d += abs(x-i) + abs(y-j)
        return manhattan_d
    
    def gaschnig(self, state):
        d = 0
        to_visit = set(sum(state,()))
        to_visit.remove(0)
        state = [list(row) for row in state]
        blank = index_2d(state, 0)
        blank_goal = index_2d(self.goal_state, 0)
        while to_visit:
            if blank != blank_goal:
                n = self.goal_state[blank[0]][blank[1]]
                move_to = index_2d(state, n)
                swap(state, blank, move_to)
                d+=1
                blank = move_to
                to_visit.remove(n)
            else:
                n = to_visit.pop()
                position = index_2d(state, n)
                if  position != index_2d(self.goal_state, n):
                    to_visit.add(n)                    
                    swap(state, blank, position)
                    d+=1
                    blank = position
        return d
    
    def max_heuristic(self,state):
        return max([f(self, state) for f in Fifteen_problem.heuristics])
    
    def __repr__(self):
        return "{}-problem\ninit=\n{}".format(self.size**2-1, self.initial_state)

    heuristics = [
        misplaced_tiles,
        manhattan_d,
        gaschnig
        ]    
    
directions = {
        "up":    ( 1, 0),
        "down":  (-1, 0),
        "right": ( 0,-1),
        "left":  ( 0, 1)
    }

def coords(size):
    return ((x,y) for x in range(size) for y in range(size))

def swap(l, a, b):
    l[a[0]][a[1]], l[b[0]][b[1]] = l[b[0]][b[1]], l[a[0]][a[1]]

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
    return tuple([tuple(l[i*s:(i+1)*s]) if True#i%2==0 
             else tuple(l[(i+1)*s-1:i*s-1:-1])
             for i in range(s)])

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))
    raise KeyError