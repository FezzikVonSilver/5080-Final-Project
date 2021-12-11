
""" @author Dylan Wu; Last worked on: Sat. 12.11.2021 """

import random_metric_graph as rmg
G = rmg.randCompleteMetricGraph(5)

"""
Performs an euler tour/hamilton tour in one go, shortcuts vertices if necessary 

Takes in a graph G as adj matrix and returns an adj matrix of the TSP tour
"""

def create_tour(G): #Every vertex in G must have even degree

    # adj matrix to return
    tspTour = [[0 for _ in range(len(G))] for _ in range(len(G))]

    # keep track of all vertices that have been visited
    visited = set() 

    # vertex j is valid if there is edge to it from i and if it's not visited
    isValid = lambda i,j: i != j and G[i][j] != 0 and not j in visited  

    """ Helper functions; called in get_tsp_tour function """
    def get_next_vertex(curr):
        for next in range(len(G[curr])):
            if isValid(curr, next):
                return next
        return None

    def get_next_next_vertex(curr):
        for next in range(len(G[curr])):
            for next_next in range(len(G[next])):
                if isValid(next, next_next):
                    return next_next
        return None

    def add_edge(i, j):
        tspTour[i][j] = G[i][j]
        tspTour[j][i] = G[i][j]

    """ End of helper functions """

    def get_tsp_tour():
        curr_vertex = 0 #starting vertex

        while len(visited) < len(G):
            visited.add(curr_vertex) #mark vertex as visited

            next_vertex = get_next_vertex(curr_vertex)

            if next_vertex != None: # if there's an unvisited neighbor, add that to the tour
                add_edge(curr_vertex, next_vertex)

            else: 
                #if all neighbors have been visited, skip one that has unvisited neighbor, and visit that vertex
                next_vertex = get_next_next_vertex(curr_vertex)
                if next_vertex == None and len(visited) == len(G):
                    add_edge(curr_vertex, 0) # end of tour--creates the tour, terminate loop
                    break
            curr_vertex = next_vertex # visit next valid vertex
                
        return tspTour

    return get_tsp_tour()

print("Complete graph: " + str(G))
res = create_tour(G)
print("TSP tour" + str(res))