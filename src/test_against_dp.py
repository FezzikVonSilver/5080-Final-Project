from itertools import combinations
import random_metric_graph as rmg
from min_span_tree import mst
from combine import combine, span_root_example
from create_tour import create_tour
import networkx as nx
import numpy as np
from networkx.algorithms.approximation.traveling_salesman import christofides
from christofides import our_christofides
from christofides import get_cost



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
    count = 0
    iter = 0
    for i in np.arange(2,V+1):
        for j in range(10):
            g = rmg.randCompleteMetricGraph(i)
            test_0 = TSP(nx.convert_matrix.to_numpy_array(g).tolist())
            test_nx = christofides(g)
            test_nx_cost = get_cost(g,test_nx)
            test_us = our_christofides(g)
            test_us_cost =  get_cost(g,test_us)
            if test_us_cost/test_0[0] > 1.5:
                print("--------------")
                print("Number of vertices:" + str(i))
                print("NX algorithm cost:" + str(test_nx_cost))
                print("Our algorithm cost:" + str(test_us_cost))
                print("Optimal cost:" + str(test_0[0]))
            # print("Number of odd vertices:" + str(i - len(even_degree_vertices(mst(g)))))
                print(nx.convert_matrix.to_numpy_array(g))
                print(nx.convert_matrix.to_numpy_array(mst(g)))
                count += 1
            iter += 1
    return(count/iter)


p = test_against_DP(10)
print(p)