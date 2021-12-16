# importing networkx tools
import networkx as nx
from networkx.convert_matrix import from_numpy_array
from networkx.algorithms.approximation.traveling_salesman import christofides
# importing matplotlib.pyplot
from matplotlib import pyplot as plt, animation
# project file imports
import random_metric_graph as rmg
from min_span_tree import mst
import combine as com
from create_tour import create_tour


"""
Function to create graph from the tsp_tour returned

n: number of vertices in the complete tour
TSP: the tour object

return: a networkx graph object
"""
def translate_TSP_Tour(n, TSP):
    g2 = nx.Graph()

    for i in range (n):
        g2.add_node(i)

    #Adds edges along with their weights to the graph 
        for i in range(n-1) :
                # dummy weight of one for the edges, not sure if needed?
                g2.add_edge(TSP[i], TSP[i+1], weight = 1) 
        return g2



#main function
if __name__ == "__main__":
    # create the starting random graph
    g = rmg.randCompleteMetricGraph(10)

    # set position using spring layout (this will result in the nodes displaying at the same position each time the same graph object is drawn if used in call)
    pos = nx.spring_layout(g, seed=1)

    # get MST of g
    T = mst(g)
    # even degree vertices
    E = com.even_degree_vertices(T)
    # odd degree vertices subgraph
    S = com.induced_subgraph(E,g)
    # min weight perfect matching
    M = nx.MultiGraph(com.perfect_match(S))
    # MST and Min-Weight combined
    M2 = com.combine(T, g)
    # get tour
    tsp_tour = create_tour(M2, g)
    # translate tour to draw easier
    g_tsp = translate_TSP_Tour(11, tsp_tour)

    # create fig object for animation
    fig = plt.figure()

    # Function to animate steps in the Christofides TSP algorithm
    # writes each image in the animation to file and saves, overwrites prior each run
    def animate(frame):
        fig.clear()

        # for i in range (6):
        if frame == 0:
            # draw the full graph 
            nx.draw_networkx(g, pos)
            plt.title("Starting Graph", loc='center')
            plt.show()
            plt.savefig("figure1.png")
            # print("0 - Starting Graph")

        if frame == 1:
            # draw the MST of the graph 
            nx.draw_networkx(T, pos)
            plt.title("Minimum Spanning Tree", loc='center')
            plt.show()
            plt.savefig("figure2.png")
            # print("1 - MST")

        # Vertices with odd degree
        if frame == 2:
            # nx.draw_networkx(path_edges, pos)
            # nx.draw_networkx_nodes(g, pos, nodelist=(s.nodes)-set(path_edges)
            nx.draw_networkx_nodes(g, pos)
            nx.draw_networkx_nodes(g, pos, nodelist=(S), node_color='r')
            plt.title("Odd Degree Vertices in MST", loc='center')
            plt.show()
            plt.savefig("figure3.png")
            # print("2 - Odd Degree Vertices in MST")

        # Subgraph of odd degree vertices
        if frame == 3:
            nx.draw_networkx_nodes(g, pos)
            nx.draw_networkx(S, pos, node_color='r')
            plt.title("Subgraph of Odd Degree Vertices", loc='center')
            plt.show()
            plt.savefig("figure4.png")
            # print("3 - Odd Degree Vertices Subgraph")

        # minimum weight matching
        if frame == 4:
            nx.draw_networkx_nodes(g, pos)
            nx.draw_networkx(M, pos, node_color='r')
            plt.title("Min-Weight Matching", loc='center')
            plt.show()
            plt.savefig("figure5.png")
            # print("4 - Min-Weight Matching of Odd-Degree Subgraph")

        # draw combined min-weight matching and MST
        if frame == 5:
            nx.draw_networkx(M2, pos)
            plt.title("Minimum Spanning Tree & Min-Weight Matching", loc='center')
            plt.show()
            plt.savefig("figure6.png")
            # print("5 - Min-Weight Matching & MST Combined")

        # Determine Euler Tour?  Don't think we can easily show this

        # draw our TSP tour
        if frame >= 6:
            nx.draw_networkx(g_tsp, pos, edge_color='r')
            plt.title("TSP Tour", loc='center')
            plt.show()
            plt.savefig("figure7.png")
            # print(tsp_tour)
            # print(g_tsp)
            # print("6 - TSP Tour")

        return

    # create the animation object, interval is the time each frame (image) is displayed in milliseconds
    ani = animation.FuncAnimation(fig, animate, frames=7, interval=2000, repeat=False)

    # display the animation on screen in a popup window
    plt.show()