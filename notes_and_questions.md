
## Christofides Algorithm (approximation algorithm for solving the metric TSP) 

### General TSP problem: Find the minimum-weight Hamiltonian cycle in a complete, undirected graph. 

For Chrisofides algorithm to work, distances between nodes in the graph must form a “metric space” 

   - The graph G must obey the triangle inequality (dist(u, w) <= dist(u, v) + dist(v, w)) 

   - Also, dist(u,v) = dist(v,u), and dist(u,v) > 0 

From final project specification on canvas: (input: an integer n denoting the number of vertices in the graphs; 
graphs are to be generated randomly, with edge weights between 1-20; initial graphs 
have to be output in the visualization)

### 0. Generate random graph given number of nodes n (w/ edge weights b/t 1-20)

### 1. Find a minimum spanning tree (T) 

- Find the MST of the graph (by definition, this is the set of edges that span the graph with the minimum total edge weight sum) 



### 2. Find Vertices in T with odd degree (O) 

- We want to be able to be able to find an Eulerian circuit on the graph. 
- We can only do this if every node has an even degree (because a graph has an Eulerian circuit if and only if every edge has an even degree). 
- There must be an even number of odd vertices (by the handshaking lemma). 

 

### 3. Find minimum weight matching (W) edges to T 

- We have an MST, but what we are really looking for is a minimum weight cycle that touches every node exactly once. 
- We need to somehow “turn” the MST into a cycle, while keeping it has “minimum” as possible and touch every node (except the starting and ending node) exactly once. 
- The step that will get us closer to this is to get the minimum weight matching of the edges in O (the MST that we found). 
- There are an even number of these edges, so they will all be matched. Doing this turns the MST into a cycle, where every node necessarily has an even number of edges. 

 

### 4. Build an Eulerian circuit using the edges of W and T 
- A Eulerian cycle is an Eulerian trail that starts and ends on the same vertex
- We combine the edges of W and T into a multigraph (this means that there could be more than one edge between any two vertices u and v) 

 

### 5. Remove the repeated edges in the Eulerian circuit 
- ...Since an Euler tour visits every edge once but can of course visit multiple vertices. 
- Doing this turns the tour into a Hamiltonian tour, of minimum cost, which is what we want.

	 

Questions and proofs to give/explain: 

1. Why does this algorithm work? 

2. What is the approximation ratio of this algorithm? Time complexity analysis?  

3. Why must the input graph form a metric space (obey triangle inequality, etc)? 

4. Step 3, why must every node have an even degree (proof for this)? 

5. What are some other approximation algorithms for metric TSP? Why is this one better (or worse)? 

6. Why do we combine the MST with the minimum perfect matching (steps 3, 4) 

7. How do we convert the Eulerian circuit into a Hamiltonian circuit? 

8. Why do we start by finding the MST of G? 

9. Why must there always be an odd number of edges with even degree and vice versa (handshaking lemma)? 

10. What is the polynomial time algorithm for computing the minimum weight perfect matching? 

11. How should we implement this algorithm in Python? 

12. How should we create a visualization of this algorithm? 
	- Should we show all steps for each larger step (e.g. find MST), or just show the resulting graph of each larger step?
