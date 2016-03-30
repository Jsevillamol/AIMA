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

def test():
    logging.basicConfig(filename='rbfs.log',level=logging.DEBUG)
    #to_test = [biBFGSearch, RBFSearch, AstarGSearch]
    to_test = [RBFSearch]
    n_instances = 10
    for i in range(n_instances):
        percent = i*int(100/n_instances)
        print("|{:100}|".format("="*percent +"{}%".format(percent)))
        p = Fifteen_problem(size=3, difficulty=10)
        ins = p.initial_state
        logging.info("about to start instance\n {}.\nSolvable: {}\n".format(ins, p.solvable()))
        for f in to_test:         
            logging.debug("Tuple representation: {}".format(ins.state))   
            logging.info(f)
            solution = f(p)
            logging.info("Nodes explored: {}".format(Node.node_count))
            logging.info("The solution is:\n{}.".format(solution))
            logging.info("Depth: {}\n".format(len(solution)+1))
    print("Test completed")
        
def specific_test():
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
        print("start sampling")
    def advance(self):
        self.i+=1
        percent = int(self.i*100/self.size)
        print("|{:100}|{}/{}".format("="*percent, self.i, self.size)) 
 
def sample(to_test, difficulties, n_instances):
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
                        "depth": len(solution),
                        "time":d_time,
                        "memory":Node.memory_used,
                        "nodes": Node.node_count,
                        "max_nodes": Node.max_nodes
                        }
                    json.dump(data_point, file)
                    print("", file = file)
                    bar.advance()
            
        print("sampling completed")

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

def plot_node_data(data, algorithm, h_name):
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
#    ax2.set_ylim(0, 35)
#    ax.set_ylim(-20,100)
    plt.title("{}{}. Sample size:{}".format(algorithm, h_name, len(data)))
    plt.savefig("plots/nodes/{}{}_node_data.png".format(algorithm,h))
    plt.close(fig)
    #-----------------------------------------------

def make_chart(brute_data, interval_data, name, h_name):
    
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10,10)) 
    
    """
    Sample charts
    """
    lns1= axes[0,0].plot([x["depth"] for x in brute_data], [x["time"] for x in brute_data], 'b+', label = 'Nodes explored')
    #ax.plot(time, Rn, '-', label = 'Rn')
    ax2 = axes[0,0].twinx()
    lns2= ax2.plot([x["depth"] for x in brute_data], [x["memory"]/1024 for x in brute_data], 'r+', label = 'Maximum number of nodes in memory')
    
    lns = lns1+lns2
    labs = [l.get_label() for l in lns]
    #axes[0,1].legend(lns, labs, loc=0) 
    axes[0,0].set_title("Memory/time sample chart", fontsize=14)
    axes[0,0].set_xlabel("Depth of optimal solution", style='italic')
    axes[0,0].set_ylabel(r"Time(s)", style='italic', color='b')
    ax2.set_ylabel(r"Memory (KiB)", style='italic', color='r')    
    
    lns1= axes[0,1].plot([x["depth"] for x in brute_data], [x["nodes"] for x in brute_data], 'b+', label = 'Nodes explored')
    #ax.plot(time, Rn, '-', label = 'Rn')
    ax2 = axes[0,1].twinx()
    lns2= ax2.plot([x["depth"] for x in brute_data], [x["max_nodes"] for x in brute_data], 'r+', label = 'Maximum number of nodes in memory')
    
    lns = lns1+lns2
    labs = [l.get_label() for l in lns]
    #axes[0,1].legend(lns, labs, loc=0) 
    axes[0,1].set_title("Nodes sample chart", fontsize=14)
    axes[0,1].set_xlabel("Depth of optimal solution", style='italic')
    axes[0,1].set_ylabel(r"Total nodes explored", style='italic', color='b')
    ax2.set_ylabel(r"Max nodes in memory", style='italic', color='r')
    
    """
    Boxes and whiskers charts
    """        
    labels = [5*i for i in range(len(interval_data))]
    
    time_data = [[x["time"] for x in data] for data in interval_data]
    
    axes[1,0].boxplot(time_data, labels = labels)
    axes[1,0].set_title("Time chart", fontsize=14)
    axes[1,0].set_ylabel("Time (s)", style='italic')
    axes[1,0].set_xlabel("Depth of solution", style='italic')
    
    node_data = [[x["nodes"] for x in data] for data in interval_data]    
    
    axes[1,1].boxplot(node_data, labels = labels)
    axes[1,1].set_title("Explored nodes chart", fontsize=14)
    axes[1,1].set_ylabel("Nodes explored", style='italic')
    axes[1,1].set_xlabel("Depth of solution", style='italic')
    
    mem_data = [[x["memory"]/1024 for x in data] for data in interval_data]    
    
    axes[2,0].boxplot(mem_data, labels = labels)
    axes[2,0].set_title("Memory chart", fontsize = 14)
    axes[2,0].set_ylabel("Memory (KiB)", style='italic')
    axes[2,0].set_xlabel("Depth of solution", style='italic')
    
    max_data = [[x["max_nodes"] for x in data] for data in interval_data]    
    
    axes[2,1].boxplot(max_data, labels = labels)
    axes[2,1].set_title("Max nodes chart", fontsize=14)
    axes[2,1].set_ylabel("Max nodes in memory", style='italic')
    axes[2,1].set_xlabel("Depth of solution", style='italic')
    
    fig.suptitle("{}{}".format(
                            name, 
                            "".join(
                                [s+" " for s in h_name.split("_")])
                                ), 
                            fontsize=20
                            )
    fig.subplots_adjust(hspace=0.4, wspace=0.7)
    plt.show()
    fig.savefig("plots/{}{}.png".format(name, h_name))
        
    
blind_algos = [BFTSearch, BFGSearch]#, BFTSearch
h_algos = []#RBFSearch
heuristics = [Fifteen_problem.manhattan_d, Fifteen_problem.max_heuristic]#Fifteen_problem.heuristics
    
null_h = lambda x,y:0
to_test = [(f, null_h) for f in blind_algos]
        
    
if False:
    
    difficulties = [17]
    n_instances = 40   
    
    sample(to_test, difficulties, n_instances)

blind_algos = [BFTSearch, BFGSearch, LFIDSearch, biBFGSearch]#, 
h_algos = [AstarGSearch, RBFSearch]#
heuristics = Fifteen_problem.heuristics + [Fifteen_problem.max_heuristic]#Fifteen_problem.heuristics
    
null_h = lambda x,y:0
to_test = [(f, null_h) for f in blind_algos]+[(f, h) for f in h_algos for h in heuristics]

if True:
    with open("results.data", "r") as file:
        data = [json.loads(data_string) for data_string in file if data_string != "\n"]
        #plt.plot([x["depth"] for x in BFTS_data], [x["time"] for x in BFTS_data], 'ro')
    for algo,h in to_test:
        algo_data = [x for x in data if x["algorithm"] == str(algo).split()[1] and x["heuristic"]==str(h).split()[1]]
        
        name = str(algo).split()[1] 
        h_name = (", "+str(h).split()[1].split(sep=".")[1] if h is not null_h else "")
        
        depth_intervals_data = [[] for i in range(10)]
        for data_point in algo_data:
            depth_intervals_data[int(data_point["depth"]/5)].append(data_point)
        
        for i,s in enumerate(depth_intervals_data):
            print("Algo:{}{}. Depth interval:{}-{}. Sample size:{}".\
                    format(name,h_name,i*5,(i+1)*5,len(s)))
        
        depth_intervals_data =  [interval for interval in depth_intervals_data if len(interval)>0]
        make_chart(algo_data, depth_intervals_data, name, h_name)
        #input()
        