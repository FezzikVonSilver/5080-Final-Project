import math
import heapdict
import random as r

"""
Prim's Algoritm to find a MST
"""
def find_mst(g):
	cost = []
	prev = []
	
	for i in range(len(g)): #initialize cost and prev arrays
		cost.append(math.inf)
		prev.append(None)
	
	cost[0] = 0 #tree will always start from node 0
	
	q = heapdict.heapdict() #priority queue
	
	for i in range(len(g)): #initialize priority queue based on cost values
		q[i] = cost[i]
	

	
	while len(q) is not 0: #update cost and prev
		v,c = q.popitem()
		not_added = list(q.keys())
		for i in not_added:
			if g[v][i] is not 0:
				if cost[i] > g[v][i]:
					cost[i] = g[v][i]
					prev[i] = v
					q[i] = cost[i]
	return prev,cost

"""
Helper to construct tree
"""
def construct_mst(prev,cost):
	mst = [[0 for _ in range(len(prev))] for _ in range(len(prev))]
	for i in range(len(prev)):
		for j in range(len(prev)):
			if prev[j] == i:
				mst[i][j] = cost[j]
			if prev[i] == j:
				mst[i][j] = cost[i]
	
	return mst

"""
Return's MST
"""
def mst(g):
	prev, cost = find_mst(g)

	return construct_mst(prev,cost)
				

"""
Helper function to check that random edge obeys the triangle inequality/is metric space
"""
def obeysMetric(g, i, j):
    for k in range(len(g)):
        # triangle inequality: edge weight w(i->j) should be less than or equal to w(i->k)+w(k->j)
        if g[i][k] == 0 or g[j][k] == 0: 
            continue
        if g[i][k]+g[k][j] < g[i][j]:
            return False
    return True
"""
n: number of vertices in the complete graph
w_rnge: default edge weight range is 1 to 10
return: adjacency matrix representing complete metric graph
"""
def randCompleteMetricGraph(n, w_rnge = (1,10)):
    g = [[0 for _ in range(n)] for _ in range(n)] # initialize adjacency matrix
    for i in range(n):
        for j in range(n):
            if g[j][i] != 0: # matrix is symmetric b/c graph's undirected
                g[i][j] = g[j][i]
            elif i != j: #if vertex is not itself, create random edge
                g[i][j] = r.randint(w_rnge[0], w_rnge[1])
                while not obeysMetric(g, i, j):
                    g[i][j] = r.randint(w_rnge[0], w_rnge[1])
    return g


# def main():
# 	g = randCompleteMetricGraph(3)
# 	for row in g:
# 		print(*row,sep="\t")
# 	min_tree = mst(g)
# 	print("----")
# 	for row in min_tree:
# 		print(*row,sep="\t")
# 	q = heapdict.heapdict()
# 	
# if __name__ == "__main__":
# 	main()
		
	