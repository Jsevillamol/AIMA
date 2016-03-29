# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:20:44 2016

@author: jsevillamol
"""
import logging, json, time, types, gc
from search_node import Node
from blind_search.BFGSearch import BFGSearch
from blind_search.BFTSearch import BFTSearch
from blind_search.LFIDSearch import LFIDSearch
from heuristic_search.RBFSearch import RBFSearch
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
        
if False:
    logging.basicConfig(filename='RBFSearch.log',level=logging.DEBUG)
    ins = ((7, 3, 1, 4), (9, 6, 11, 10), (15, 14, 5, 12), (8, 0, 2, 13))
    p = Fifteen_problem(size=4)
    p.initial_state = Fifteen_puzzle_state(ins)
    logging.info("about to start instance\n {}.\nSolvable: {}".format(p.initial_state, p.solvable()))
    logging.debug("Tuple representation: {}".format(p.initial_state))   
    logging.info("my A* Search")
    solution = AstarGSearch(p)
    logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))
    logging.info("My RBFSearch")
    solution = RBFSearch(p)
    logging.info("The solution is {}. Depth:{}".format(solution, len(solution)))

class Percent_bar:
    def __init__(self, size):
        self.size = int(size)
        self.i = 0
        print("start test")
    def advance(self):
        self.i+=1
        percent = int(self.i*100/self.size)
        print("|{:100}|{}/{}".format("="*percent, self.i, self.size))
 
blind_algos = [BFTSearch, BFGSearch, LFIDSearch, biBFGSearch]#
h_algos = [AstarGSearch, RBFSearch]
heuristics = Fifteen_problem.heuristics + [Fifteen_problem.max_heuristic]#Fifteen_problem.heuristics

difficulties = [10]
n_instances = 20    

null_h = lambda x,y:0
to_test = [(f, null_h) for f in blind_algos]+[(f, h) for f in h_algos for h in heuristics]
     
 
if True:
    logging.basicConfig(filename='results.log',level=logging.DEBUG)
    with open("results.data", "a") as file:
        bar = Percent_bar(n_instances*len(difficulties)*len(to_test))
        for difficulty in difficulties:
            logging.debug("Level up! Difficulty:{}".format(difficulty))
            for i in range(n_instances): 
                problem = Fifteen_problem(size = 4, difficulty=difficulty)
                logging.debug("Next instance:\n{}".format(problem.initial_state))
                for algorithm, h in to_test:
                    logging.debug("Turn for {}{}".format(str(algorithm).split()[1], ",h:"+str(h).split()[1] if h is not null_h else ""))
                    problem.h = types.MethodType(h, problem)
                    gc.collect()
                    before = time.clock()
                    solution = algorithm(problem)
                    after = time.clock()
                    d_time = after - before
                    
                    data_point = {
                        "instance:": problem.initial_state.state, 
                        "algorithm": str(algorithm).split()[1],
                        "heuristic": str(h).split()[1],
                        "solution": list(solution),
                        "depth": len(solution)+1,
                        "time":d_time,
                        "memory":Node.memory_used,
                        "nodes": Node.node_count,
                        "max_nodes": Node.max_nodes
                        }
                    json.dump(data_point, file)
                    print("", file = file)
                    bar.advance()
            
        print("test completed")

import numpy as np
import matplotlib.pyplot as plt



def plot_time_space(data, algorithm, h):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lns1=ax.plot([x["depth"] for x in data], [x["time"] for x in data], 'bo', label = 'Time(s)')
    #ax.plot(time, Rn, '-', label = 'Rn')
    ax2 = ax.twinx()
    lns2=ax2.plot([x["depth"] for x in data], [x["memory"]/1024 for x in data], 'ro', label = 'Memory(mB)')
    
    lns = lns1+lns2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)      
    
    ax.grid()
    ax.set_xlabel("Depth of optimal solution")
    ax.set_ylabel(r"Time(s)")
    ax2.set_ylabel(r"Memory(kB)")
    #ax2.set_ylim(0, 35)
    #ax.set_ylim(-20,100)
    plt.title(algorithm)
    plt.savefig("plots/time_space/{}{}_time_space.png".format(algorithm,h))
    plt.close(fig)

def plot_node_data(data, algorithm, h):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lns1= ax.plot([x["depth"] for x in data], [x["nodes"] for x in data], 'bo', label = 'Nodes explored')
    #ax.plot(time, Rn, '-', label = 'Rn')
    ax2 = ax.twinx()
    lns2= ax2.plot([x["depth"] for x in data], [x["max_nodes"] for x in data], 'ro', label = 'Maximum number of nodes in memory')
    
    lns = lns1+lns2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0) 
    
    ax.grid()
    ax.set_xlabel("Depth of optimal solution")
    ax.set_ylabel(r"Total nodes explored")
    ax2.set_ylabel(r"Max nodes in memory")
    #ax2.set_ylim(0, 35)
    #ax.set_ylim(-20,100)
    plt.title(algorithm)
    plt.savefig("plots/nodes/{}{}_node_data.png".format(algorithm,h))
    plt.close(fig)

if True:
    with open("results.data", "r") as file:
        data = [json.loads(data_string) for data_string in file if data_string != "\n"]
        #plt.plot([x["depth"] for x in BFTS_data], [x["time"] for x in BFTS_data], 'ro')
        for algo,h in to_test:
            algo_data = [x for x in data if x["algorithm"] == str(algo).split()[1] and x["heuristic"]==str(h).split()[1]]
            name = str(algo).split()[1] 
            h_name = ("_h:"+str(h).split()[1] if h is not null_h else "")
            plot_time_space(algo_data, name, h_name)
            plot_node_data(algo_data, name, h_name)
        