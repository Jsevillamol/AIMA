# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:20:44 2016

@author: jsevillamol
"""
import logging
from heuristic_search.AstarGSearch import AstarGSearch
from problems.fifteen_problem import Fifteen_problem
from blind_search.biBFGSearch import biBFGSearch

if True:
    logging.basicConfig(filename='A*GSearch.log',level=logging.DEBUG)
    for i in range(10):
        p = Fifteen_problem(size=4, difficulty=100)
        ins = p.initial_state
        logging.info("about to start instance\n {}.\nSolvable: {}".format(p.initial_state, p.solvable()))
        logging.debug("Tuple representation: {}".format(p.initial_state.state))      
        logging.info("A*GSearch")
        solution = AstarGSearch(p)
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
        logging.info("biBFGSearch")
        solution = biBFGSearch(p)
        logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))