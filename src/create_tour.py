
""" @author Dylan Wu; Last worked on: Sat. 12.11.2021 """

import random_metric_graph as rmg
import networkx as nx

G = rmg.randCompleteMetricGraph(5)

"""
Performs an euler tour/hamilton tour in one go, shortcuts vertices if necessary 

Takes in a graph G as adj matrix and returns an adj matrix of the TSP tour
"""

def create_tour(M, G): #Every vertex in G must have even degree

    # adj matrix to return
    # tspTour = [[0 for _ in range(len(G))] for _ in range(len(G))]
    tsp_tour = nx.MultiGraph()

    # keep track of all vertices that have been visited
    visited = set() 

    def is_valid(node):
        finishes_tour = (node == 0 and len(visited) == len(G.nodes))
        return finishes_tour or node not in visited

    """ Helper functions; called in get_tsp_tour function """
    def get_next_vertex(curr):
        for next in M.neighbors(curr):
            if is_valid(next):
                return next
        return get_next_next_vertex(curr)

    def get_next_next_vertex(curr): #shortcut vertex
        for next in M.neighbors(curr):
            for next_next in G.neighbors(next):
                if is_valid(next_next):
                    return next_next
        return None

    """ End of helper functions """

    def get_tsp_tour():
        curr_vertex = 0 #starting vertex

        while len(visited) <= len(G.nodes):
            visited.add(curr_vertex) #mark vertex as visited

            next_vertex = get_next_vertex(curr_vertex)
            if next_vertex != None:
                edge_weight = G.get_edge_data(curr_vertex, next_vertex)[0]['weight']
                tsp_tour.add_edge(curr_vertex, next_vertex, edge_weight)
            else:
                raise Exception("Graph is not eulerian; cannot find tour")

            if len(visited) == len(G.nodes): # tour has been completed
                break
            
            curr_vertex = next_vertex # visit next valid vertex
                
        return tsp_tour

    return get_tsp_tour()
