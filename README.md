# 5080-Final-Project
The Christofides Algorithm

Basic steps of algorithm:

Graph = (Vertices, W nonnegative real weights of edges)

1) Find a minimum spanning tree (T)
2) Find Vertices in T with odd degree (O)
3) Find minimum weight matching (W) edges to T
4) Build an Eulerian circuit using the edges of W and T 
   (A Eulerian cycle is an Eulerian trail that starts and ends on the same vertex)
6) Make a Hamiltonian circuit by skipping repeated vertexes
   (A Hamiltonian circuit is a path in an undirected or directed graph that visits each vertex exactly once) 
