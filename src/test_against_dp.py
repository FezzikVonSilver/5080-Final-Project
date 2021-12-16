from itertools import combinations
from random import paretovariate
import random_metric_graph as rmg
import networkx as nx
import numpy as np
from networkx.algorithms.approximation.traveling_salesman import christofides
from christofides import our_christofides

# total_count = 0

def get_cost(G, tour):
    cost = 0
    for i in range(0, len(tour)-1):
        u = tour[i]
        v = tour[i+1] 
        weight = G[u][v]['weight']
        cost += weight
    return cost

def TSP(G):
	n = len(G)
	C = [[np.inf for _ in range(n)] for __ in range(1 << n)]
	C[1][0] = 0 # {0} <-> 1
	for size in range(1, n):
		for S in combinations(range(1, n), size):
			S = (0,) + S
			k = sum([1 << i for i in S])
			for i in S:
				if i == 0: 
					continue
				for j in S:
					if j == i: 
						continue
					cur_index = k ^ (1 << i)
					C[k][i] = min(C[k][i], C[cur_index][j]+ G[j][i])     
                                               #C[S−{i}][j]
	all_index = (1 << n) - 1
	return min([(C[all_index][i] + G[0][i], i) for i in range(n)])


def test_against_DP(V):
    # global total_count
    count = 0
    iter = 0
    for i in np.arange(2,V+1):
        for j in range(10):
            # print("COUNT: " + str(total_count)) 
            # total_count += 1
            g = rmg.randCompleteMetricGraph(i)
            test_0 = TSP(nx.convert_matrix.to_numpy_array(g).tolist())
            test_nx = christofides(g)
            test_nx_cost = get_cost(g,test_nx)
            test_us = our_christofides(g)
            test_us_cost =  get_cost(g,test_us)

            # print(test_us)
            print(test_nx_cost, test_us_cost)
            if test_us_cost/test_0[0] > 1.5:
                print("--------------")
                print("Number of vertices:" + str(i))
                print("NX algorithm cost:" + str(test_nx_cost))
                print("Our algorithm cost:" + str(test_us_cost))
                print("Optimal cost:" + str(test_0[0]))
                print("Our tour:"+str(test_us))
                print("Their tour:"+str(test_nx))
            # print("Number of odd vertices:" + str(i - len(even_degree_vertices(mst(g)))))
                print(nx.convert_matrix.to_numpy_array(g))
                print(nx.convert_matrix.to_numpy_array(mst(g)))
                count += 1
            iter += 1
    return(count/iter)


# # for i in range(5, 10):
# for _ in range(1000000):
#     p = test_against_DP(5)
#     print(p)
# # print(p)