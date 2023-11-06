from collections import deque
"""
Implement a BFS traversal function for a graph
With the information you have received from the course, 
implement a Breadth-First traversal iterative function for a graph. 

The function accepts as parameters the graph object and the vertex from 
where to start.

The function should return a dictionary with the vertices as the keys and 
the vertices from where those keys where visited as the values.
"""
def BFS(graph, start):
    """
    Perform Breadth-First Search of the graph starting from Vertex start.
    
    :param graph: Instance of Graph
    :param start: Starting Vertex for BFS
    :return: Dictionary of visited vertices with their parent vertices
    """
    # Queue for the vertices to visit
    queue = deque([start])
    
    # Dictionary to keep track of visited vertices and their parents
    visited = {start: None}
    
    # Loop until there are vertices to be visited
    while queue:
        # Dequeue a vertex from the queue
        current_vertex = queue.popleft()
        
        # Visit all adjacent vertices that haven't been visited
        for neighbour in graph._adj_map[current_vertex]:
            if neighbour not in visited:
                visited[neighbour] = current_vertex  # Mark the neighbour as visited with its parent
                queue.append(neighbour)  # Enqueue the neighbour
    
    return visited
