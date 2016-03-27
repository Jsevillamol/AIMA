# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:20:44 2016

@author: jsevillamol
"""
import logging
from search_node import Node
from heuristic_search.RBFSearch import RBFSearch, recursive_best_first_search
from problems.fifteen_problem import Fifteen_problem, Fifteen_puzzle_state
from blind_search.biBFGSearch import biBFGSearch
from heuristic_search.AstarGSearch import AstarGSearch

if False:
    logging.basicConfig(filename='rbfs.log',level=logging.DEBUG)
    #to_test = [biBFGSearch, RBFSearch, AstarGSearch]
    to_test = [RBFSearch, recursive_best_first_search]
    n_instances = 10
    for i in range(n_instances):
        percent = i*int(100/n_instances)
        print("|{:100}|".format("="*percent +"{}%".format(percent)))
        p = Fifteen_problem(size=3, difficulty=10)
        ins = p.initial_state
        logging.info("about to start instance\n {}.\nSolvable: {}\n".format(p.initial_state, p.solvable()))
        for f in to_test:         
            logging.debug("Tuple representation: {}".format(p.initial_state.state))      
            logging.info(f)
            solution = f(p)
            logging.info("Nodes explored: {}".format(Node.node_count))
            logging.info("The solution is:\n{}.".format(solution))
            logging.info("Depth: {}\n".format(len(solution)+1))
    print("Test completed")
        
if True:
    logging.basicConfig(filename='RBFSearch.log',level=logging.DEBUG)
    ins = ((7, 3, 1, 4), (9, 6, 11, 10), (15, 14, 5, 12), (8, 0, 2, 13))
    p = Fifteen_problem(size=4)
    p.initial_state = Fifteen_puzzle_state(ins)
    logging.info("about to start instance\n {}.\nSolvable: {}".format(p.initial_state, p.solvable()))
    logging.debug("Tuple representation: {}".format(p.initial_state))   
    logging.info("my A* Search")
    solution = AstarGSearch(p)
    logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
    logging.info("Recursive BF Search from AIMA")
    solution = recursive_best_first_search(p)
    logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
    logging.info("My RBFSearch")
    solution = RBFSearch(p)
    logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))