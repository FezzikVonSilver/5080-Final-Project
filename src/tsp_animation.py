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
import christofides as ch



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


def christo_animation(n):

    # create the starting random graph
    g = rmg.randCompleteMetricGraph(6)
    # g = com.span_root_example()

    # get the weights of the edges to label in graph
    edge_labels = dict([((n1, n2), d['weight'])
                    for n1, n2, d in g.edges(data=True)])

    # labels = nx.get_edge_attributes(g, 'weight')

    # set position using spring layout (this will result in the nodes displaying at the same position each time the same graph object is drawn if used in call)
    # pos = nx.spring_layout(g, seed=1)
    pos = nx.spring_layout(g)

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
    tour_edges = zip(list(tsp_tour))
    # get tour cost, wrong?
    tour_cost = str(round(ch.get_cost(g, tsp_tour), 2))
    

    # translate tour to draw easier
    g_tsp = translate_TSP_Tour(n+1, tsp_tour)

    # create fig object for animation
    fig = plt.figure()

    # Function to animate steps in the Christofides TSP algorithm
    # writes each image in the animation to file and saves, overwrites prior each run
    def animate(frame):
        fig.clear()

        # for i in range (6):
        if frame == 0:
            # draw the full graph 
            nx.draw_networkx(g, pos, with_labels = True)
            # nx.draw(g, with_labels = True)
            # draw edge weight labels for troubleshooting
            nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
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
            # nx.draw_networkx_edges(g, pos, edgelist=tsp_tour, width=6)
            plt.title("Minimum Spanning Tree & Min-Weight Matching Combined", loc='center')
            plt.show()
            plt.savefig("figure6.png")
            # print("5 - Min-Weight Matching & MST Combined")

        # Determine Euler Tour?  Don't think we can easily show this

        # draw our TSP tour
        if frame >= 6:
            nx.draw_networkx(g_tsp, pos, edge_color='r')
            # nx.draw_networkx_nodes(g, pos)
            # nx.draw_networkx_edges(g, pos, edgelist=set(tour_edges), edge_color='r')
            # add label with tour cost rounded to 3 decimals
            plt.title("Christofides TSP Tour - cost: " + tour_cost, loc='center')
            plt.show()
            plt.savefig("figure7.png")
            # print(tsp_tour)
            # print(g_tsp)
            # print("6 - TSP Tour")

        return

    # create the animation object, interval is the time each frame (image) is displayed in milliseconds
    ani = animation.FuncAnimation(fig, animate, frames=7, interval=1000, repeat=False)

    # display the animation on screen in a popup window
    plt.show()

#main function
if __name__ == "__main__":
    christo_animation(6)