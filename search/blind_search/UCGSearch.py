# -*- coding: utf-8 -*-

def UCGSearch(problem):
    initial_node = Node(problem.initial_state)
    if goal(initial_state): return initial_node
    frontier = [initial_node] #Maybe use a set
    while(not frontier.empty()):
        node = frontier.pop_max()
        if goal(node.state): return node
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = child_node(node,action)
            if not child.state in explored: 
                if not child in frontier: #not bad
                    frontier.add(child)
                elif frontier child cost > child.cost:
                    frontier child = child
        
    return None