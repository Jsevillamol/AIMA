# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:33:50 2016

@author: jsevillamol
"""

from search_node import Node

def LFRBFSearch(problem):
    """
    Recursive Best-First Search
    """
    def ReBFSearch(problem, node, f_limit, n_nodes):
        Node.check(n_nodes)
        if problem.goal_test(node.state):
            return node.solution(), 0
        
        successors = [node.child(problem, action) for action in problem.actions(node.state)]
        path = [n.state for n in node.reverse_path()]
        successors = [s for s in successors if not s.state in path]#Filter loopy paths
        
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
    
    Node.reset()
    result = ReBFSearch(problem, Node(problem), float("inf"), 1)[0]
    return result