"""
def dijkstra_shortest_path(source_vertex, destination_vertex, graph):
    # Get all vertices
    unvisited_vertices = graph.get_vertices()
    # Create a dict table with the discovered shortest distances and paths
    shortest_path_table = {vertex: {'shortest': float('inf'), 'previous': None} for vertex in unvisited_vertices}
    # Initialize the source vertex path distance as 0.
    shortest_path_table[source_vertex]['shortest'] = 0
    # Loop while there are untested vertices
    while unvisited_vertices:
        # Get the vertex with the minimum path distance until now
        current_vertex = min(unvisited_vertices, key=lambda vertex: shortest_path_table[vertex]['shortest'])
        # Get its distance
        distance_from_source = shortest_path_table[current_vertex]['shortest']
        # Iterate over the adjacent vertices of this vertex that are still unvisited
        unvisited_adjacent_vertices = (v for v in graph.get_adjacent_vertices(current_vertex) if v in unvisited_vertices)
        for adjacent_vertex in unvisited_adjacent_vertices:
            # Get incident edge between the vertices (current and adjacent)
            edge = graph.get_edge(current_vertex, adjacent_vertex)
            # Calculate what would be the distance to adjacent vertex through this current vertex:
            # Distance to current vertex + distance between these two vertices (edge's value)
            tentative_distance = distance_from_source + edge.value()
            # If the tentative distance is shorter than the already calculated, update the table
            if tentative_distance < shortest_path_table[adjacent_vertex]['shortest']:
                shortest_path_table[adjacent_vertex]['shortest'] = tentative_distance
                shortest_path_table[adjacent_vertex]['previous'] = current_vertex
        # Remove the current vertex from the list of available vertices (as it is now visited)
        unvisited_vertices.remove(current_vertex)
    # Retrieve the path (in reverse order)
    path = []
    current = destination_vertex
    while current:
        path.append(current)
        current = shortest_path_table[current]['previous']
    # Return shortest distance and minimum distance path from source vertex to destination vertex
    return shortest_path_table[destination_vertex]['shortest'], path[::-1]
"""
import heapq

class Vertex:
    def __init__(self, name):
        self.name = name

    def __lt__(self, other):
        # Customize comparison for heapq
        return id(self) < id(other)

class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

class Graph:
    def __init__(self, adjacency_map):
        self.adjacency_map = adjacency_map

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph.adjacency_map}
    distances[start_vertex] = 0

    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, edge in graph.adjacency_map[current_vertex].items():
            weight = edge.cost
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def get_best_city(graph):
    min_total_cost = float('infinity')
    best_city = None

    for city in graph.adjacency_map:
        distances = dijkstra(graph, city)
        total_cost = sum(distances.values()) - distances[city]

        if total_cost < min_total_cost:
            min_total_cost = total_cost
            best_city = city

    if best_city:
        return best_city.name, min_total_cost
    else:
        return None, 0



# Example usage with the provided adjacency map
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')
G = Vertex('G')
H = Vertex('H')
J = Vertex('J')

AB = Edge(A, B, 25)
AD = Edge(A, D, 3)
AG = Edge(A, G, 17)
BC = Edge(B, C, 2)
BD = Edge(B, D, 73)
BE = Edge(B, E, 84)
CF = Edge(C, F, 79)
DE = Edge(D, E, 47)
DH = Edge(D, H, 10)
EF = Edge(E, F, 73)
EH = Edge(E, H, 15)
FJ = Edge(F, J, 48)
GH = Edge(G, H, 38)
HJ = Edge(H, J, 72)

am = {
    A: {B: AB, D: AD, G: AG},
    B: {A: AB, C: BC, D: BD, E: BE},
    C: {B: BC, F: CF},
    D: {A: AD, B: BD, E: DE, H: DH},
    E: {B: BE, D: DE, F: EF, H: EH},
    F: {C: CF, E: EF, J: FJ},
    G: {A: AG, H: GH},
    H: {D: DH, E: EH, G: GH, J: HJ},
    J: {F: FJ, H: HJ}
}

g = Graph(am)
print(get_best_city(g))
