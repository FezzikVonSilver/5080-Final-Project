
import random as r
import numpy as np
import networkx as nx

"""
Helper function to check that random edge obeys the triangle inequality/is metric space
"""
def obeysMetric(G, i, j, candidate_weight):
    for k in range(len(G)):
        # triangle inequality: edge weight w(i->j) should be less than or equal to w(i->k)+w(k->j)
        if G.has_edge(i, k) and G.has_edge(k, j): 
            ik_weight = G[i][k]['weight']
            kj_weight = G[k][j]['weight']
            if ik_weight + kj_weight < candidate_weight:
                return False
    return True

"""
n: number of vertices in the complete graph
w_rnge: default edge weight range is 1 to 10

return: adjacency matrix representing complete metric graph
"""
def randCompleteMetricGraph(n, w_rnge = (1,10)):
    g = nx.Graph()
    for i in range(n):
        g.add_node(i)
        for j in range(n):
            if i != j and not g.has_edge(i, j): # no self loops, no double edges
                candidate_weight = r.randint(w_rnge[0], w_rnge[1])

                while not obeysMetric(g, i, j, candidate_weight):
                    candidate_weight = r.randint(w_rnge[0], w_rnge[1])

                g.add_edge(i, j, weight=candidate_weight)
    return g

#main function
if __name__ == "__main__":
    g = randCompleteMetricGraph(100)
    print(g.adj)