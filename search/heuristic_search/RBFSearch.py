# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:10:53 2016

@author: jsevillamol
"""

from search_node import Node

def RBFSearch(problem):
    """
    Recursive Best-First Search
    """
    def ReBFSearch(problem, node, f_limit, n_nodes):
        Node.check(n_nodes)
        if problem.goal_test(node.state):
            return node.solution(), 0
        
        successors = [node.child(problem, action) for action in problem.actions(node.state)]
        
        n_nodes += len(successors)
        
        if not successors: return None, float("inf")    
        
        for s in successors:
            s.f_value = max(node.f_value, s.f_value)
        
        while True:
            best, second_best = two_bests(successors)
            if best.f_value > f_limit:
                return None, best.f_value
            result, best.f_value = ReBFSearch(problem, best, min(second_best.f_value, f_limit), n_nodes)
            if result is not None: return result, best.f_value    
    
    Node.reset()
    result = ReBFSearch(problem, Node(problem), float("inf"), 1)[0]
    return result
    
        
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
    
"""
def recursive_best_first_search(problem):

    def RBFS(problem, node, flimit):
        if problem.goal_test(node.state):
            return node.solution(), 0   # (The second value is immaterial)
        successors = [node.child(problem, action) for action in problem.actions(node.state)]
        if len(successors) == 0:
            return None, float("inf")
        for s in successors:
            s.f_value = max(s.path_cost + problem.h(s.state), node.f_value)
        while True:                    
            successors.sort(key=lambda x: x.f_value) # Order by lowest f value
            best = successors[0]
            if best.f_value > flimit:
                return None, best.f_value
            if len(successors) > 1:
                alternative = successors[1].f_value
            else:
                alternative = float("inf")
            result, best.f_value = RBFS(problem, best, min(flimit, alternative))
            if result is not None:
                return result, best.f_value

    node = Node(problem)
    node.f_value = problem.h(node.state)
    result, bestf = RBFS(problem, node, float("inf"))
    return result
"""