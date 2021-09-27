# Interview Questions: Undirected Graphs (ungraded)
## Question 1
**Nonrecursive depth-first search.** Implement depth-first search in an undirected graph without using recursion.

## Question 2
**Diameter and center of a tree.** Given a connected graph with no cycles

* Diameter: design a linear-time algorithm to find the longest simple path in the graph.
* Center: design a linear-time algorithm to find a vertex such that its maximum distance from any other vertex is minimized.

To find diameter is the same as traversal from one node with a degree of one to all other nodes with a degree of one. The longest path is the result.
Using either BFS or DFS should be fine.

To find center

A side note for simple graph and simple path:

**Simple Graph.** A simple graph is a graph that does not have more than one edge between any two vertices and no edge starts and ends at the same vertex. 
In other words a simple graph is a graph without loops and multiple edges. 

**Simple path** A path that does not repeat vertices is called a simple path. 

## Question 3
**Euler cycle.** An Euler cycle in a graph is a cycle (not necessarily simple) that uses every edge in the graph exactly one.

* Show that a connected graph has an Euler cycle if and only if every vertex has even degree.
* Design a linear-time algorithm to determine whether a graph has an Euler cycle, and if so, find one.

