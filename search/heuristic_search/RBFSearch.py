# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:10:53 2016

@author: jsevillamol
"""

from search_node import Node

def RBFSearch(problem):
    Node.reset()
    result = ReBFSearch(problem, Node(problem), float("inf"))[0]
    return result if result != False else None
    
def ReBFSearch(problem, node, f_limit):
    Node.count()
    if problem.goal_test(node.state):
        return node.solution(), 0
    
    successors = [node.child(problem, action) for action in problem.actions(node.state)]
    
    if not successors: return False, float("inf")    
    
    
    """
    for s in successors:
        if node.f_value > s.f_value: print("You were wrong!")
        s.f_value = max(node.f_value, s.f_value)
    """
    
    while True:
        best, second_best = two_bests(successors)
        if best.f_value > f_limit:
            return False, best.f_value
        result, best.f_value = ReBFSearch(problem, best, min(second_best.f_value, f_limit))
        if result != False: return result, 0
        
def two_bests(nodes):
    m1 = m2 = Node()
    m1.f_value = m2.f_value = float("inf")
    for n in nodes:
        if n.f_value < m2.f_value:
            if n.f_value <= m1.f_value:
                m1, m2 = n, m1 
            else:
                m2 = n
    return m1, m2
        