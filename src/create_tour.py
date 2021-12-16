import networkx as nx
from matplotlib import pyplot as plt
"""
Performs an hamilton tour on eulerian graph, shortcuts vertices if necessary 

Takes in a graph G as adj matrix and returns an adj matrix of the TSP tour
"""

def create_tour(M, G):

    if not nx.is_eulerian(M):
        raise ValueError("Multigraph M must be eulerian!")

    def can_skip_to(u, v):
        for w in M.nodes:
            if M.has_edge(u, w) and M.has_edge(w, v):
                return True
        return False

    def is_valid(node, path):
        finishes_tour = node == 0 and (len(path) == len(M.nodes))
        return finishes_tour or node not in path

    for i in range(0, len(G)):
        # stack = [([0],0)]
        stack = [([i],i)]

        # found_tour = []

        while stack:
            # print(stack)
            path,u = stack.pop()

            no_open_neighbors = True
            for v in M.neighbors(u):
                # print("neighbor: " + str(v))
                if is_valid(v, path):
                    stack.append((path.copy() + [v], v))
                    if len(path+[v]) == len(M.nodes)+1:
                        # found_tour = path + [v]
                        # break
                        return path + [v]
                    no_open_neighbors = False

            if no_open_neighbors:
                for g_v in G.neighbors(u):
                    if is_valid(g_v, path) and can_skip_to(u, g_v):
                        stack.append((path.copy() + [g_v], g_v))
                        if len(path + [g_v]) == len(M.nodes)+1:
                            return path + [g_v]
                            # break
    
    # print(M.edges)
    # nx.draw(M, with_labels=True)
    # plt.draw()
    # plt.show()
    # raise ValueError("STOP HERE: " + str(len(G)))
   
    return []
    

