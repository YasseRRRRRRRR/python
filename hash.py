# Given keys
keys = [50, 27, 59, 1, 43, 52, 40, 63]

# Initialize the hash table as a list of None values
hash_table = [None] * 8

# Hash function
def hash_function(key):
    return (5 * key + 3) % 8

# Insert keys into the hash table using linear addressing
for key in keys:
    hash_value = hash_function(key)
    # Linear probing until an empty slot is found
    while hash_table[hash_value] is not None:
        hash_value = (hash_value + 1) % 8
    hash_table[hash_value] = key

# Print the resulting hash table
print(hash_table)

"""
You are considering traveling to a certain country for your holidays. You already have a list of cities you want to visit and your plan is to stay in one of the cities and visit the rest of them one city a day.

As you want your trip to be as cheap as possible and you don't have any city preference to stay in, you plan to write a function that given a graph with the cities, the connection between them and the cost associated to travel between them, gives you what is the best city to stay in. That is, the city that has a minimum cost to travel to the rest of the cities.

Given the graph object and the dijkstra algorithm you studied in the course, write a modified dijkstra function and main function that gives you the answer. Your function should accept the graph as a parameter and call your modified dijkstra function on each of the vertices (cities). The modified dijkstra function should return the table with the costs, so you can collect the costs for all cities and calculate which one of them has a smaller value for for traveling to the rest of cities (the minimum sum of all costs for each city). Your function should return a tuple containing the name of the city (the value of the vertex) and the total cost of traveling to the rest of the cities from that one.

Par exemple:

Test	Résultat
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')

AB = Edge(A, B, 93)
AC = Edge(A, C, 21)
BE = Edge(B, E, 81)
CD = Edge(C, D, 11)
CE = Edge(C, E, 18)
DE = Edge(D, E, 33)

am = {
    A: {B: AB, C: AC},
    B: {A: AB, E: BE},
    C: {A: AC, D: CD, E: CE},
    D: {C: CD, E: DE},
    E: {B: BE, C: CE, D: DE},
}

g = Graph(am)
print(get_best_city(g))
('C', 149)
here is the code
import heapq

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

class Graph:
    def __init__(self, adjacency_matrix):
        self.vertices = list(adjacency_matrix.keys())
        self.adjacency_matrix = adjacency_matrix

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for edge in current_vertex.edges:
            neighbor = edge.end
            weight = edge.cost
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def get_best_city(graph):
    best_city = None
    min_total_cost = float('infinity')

    for city in graph.vertices:
        distances = dijkstra(graph, city)
        total_cost = sum(distances.values()) - distances[city]
        
        if total_cost < min_total_cost:
            min_total_cost = total_cost
            best_city = city

    return best_city.name, min_total_cost

def get_best_city(graph):
    pass
"""