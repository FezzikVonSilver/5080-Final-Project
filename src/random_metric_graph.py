
import random as r

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

#g = randCompleteMetricGraph(10)