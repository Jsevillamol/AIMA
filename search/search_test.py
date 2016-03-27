# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:20:44 2016

@author: jsevillamol
"""
import logging, itertools
from search_node import Node
from heuristic_search.RBFSearch import RBFSearch
from problems.fifteen_problem import Fifteen_problem
from blind_search.biBFGSearch import biBFGSearch
from heuristic_search.AstarGSearch import AstarGSearch

if True:
    logging.basicConfig(filename='RBFSearch.log',level=logging.DEBUG)
    for i in range(10):
        p = Fifteen_problem(size=4, difficulty=10)
        ins = p.initial_state
        logging.info("about to start instance\n {}.\nSolvable: {}".format(p.initial_state, p.solvable()))
        logging.debug("Tuple representation: {}".format(p.initial_state.state))      
        logging.info("RBFSearch")
        nodes_explored = itertools.count()
        solution = RBFSearch(p)
        logging.info("Nodes explored: {}".format(Node.node_count))
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
#        logging.info("biBFGSearch")
#        solution = biBFGSearch(p)
#        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
        
if False:
    logging.basicConfig(filename='RBFSearch.log',level=logging.DEBUG)
    ins = ((0, 8, 2, 3), (1, 7, 5, 4), (9, 6, 10, 11), (15, 14, 13, 12))
    p = Fifteen_problem(ins)
    logging.info("about to start instance\n {}.\nSolvable: {}".format(p.initial_state, p.solvable()))
    logging.debug("Tuple representation: {}".format(p.initial_state.state))   
    logging.info("AstarGSearch")
    solution = AstarGSearch(p)
    logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
    logging.info("RBFSearch")
    solution = RBFSearch(p)
    logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))