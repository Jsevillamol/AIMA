# -*- coding: utf-8 -*-

def UCGSearch(problem):
    initial_node = Node(problem)
    if goal(initial_state): return initial_node.solution()
    
    frontier = Priority_Queue()
    frontier.push(initial_node)
    
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

