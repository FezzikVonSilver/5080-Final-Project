
""" @author Dylan Wu; Last worked on: Sat. 12.11.2021 """

import random_metric_graph as rmg
import networkx as nx

G = rmg.randCompleteMetricGraph(5)

"""
Performs an euler tour/hamilton tour in one go, shortcuts vertices if necessary 

Takes in a graph G as adj matrix and returns an adj matrix of the TSP tour
"""

def create_tour(M, G):

    def can_skip_to(u, v):
        for w in M.nodes:
            if M.has_edge(u, w) and M.has_edge(w, v):
                return True
        return False

    def is_valid(node, path):
        finishes_tour = node == 0 and (len(path) == len(M.nodes))
        return finishes_tour or node not in path

    stack = [([0],0)]

    while stack:
        path,u = stack.pop()

        no_open_neighbors = True
        for v in M.neighbors(u):
            if is_valid(v, path):
                stack.append((path + [v], v))
                if len(path) == len(M.nodes):
                    return path+[v]
                no_open_neighbors = False
            if no_open_neighbors:
                for g_v in G.neighbors(u):
                    if is_valid(g_v, path) and can_skip_to(u, g_v):
                        stack.append((path + [g_v], g_v))
                        if len(path) == len(M.nodes):
                            return path+[g_v]
    

