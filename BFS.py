"""
Implement a DFS traversal function for a graph
With the information you have received from the course,
implement a Depth-First traversal recursive function for a graph.

The function accepts as parameters the graph object, the vertex from where
to start and a visited dictionary (that defaults to None, so the final
user don't need to provide it)

The function should return a dictionary with the vertices as the keys and the vertices from where those keys where visited as the values.
"""
def DFS(graph, u, visited=None, parent =None):
    """
    Perform Depth-First Search of the undiscovered portion of Graph starting at Vertex u.
    
    :param graph: Instance of Graph
    :param u: Current Vertex to start DFS
    :param visited: Dictionary to keep track of visited vertices and their parents
    :param parent: Parent Vertex of the current Vertex
    :return: Dictionary of visited vertices
    """
    # Initialize the visited dictionary on the first call
    if visited is None:
        visited = {}

    # Mark the current vertex u as visited; set its parent
    visited[u] = parent

    # Visit all adjacent vertices that haven't been visited
    for neighbour in graph._adj_map[u]:
        if neighbour not in visited:
            DFS(graph, neighbour, visited, u)
    
    return visited
