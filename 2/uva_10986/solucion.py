class Node:
    def __init__(self, index):
        self.index = index
        self.neighbours = []
        self.distances = []
        
    def add_neighbour(self, neighbour, distance):
        self.neighbours.append(neighbour)
        neighbour.neighbours.append(self)
        self.distances.append(distance)
        neighbour.distances.append(distance)
        
    def get_distance(self, other_node):
        if(other_node in self.neighbours):
            return(self.distances[self.neighbours.index(other_node)])
        else:
            return(float("infinity"))

from collections import deque

def solve(graph, start_node, end_node):
    best_distances = [float("infinity")]*len(graph)
    not_checked = graph.copy()
    queue = deque(graph)
    best_distances[start_node.index] = 0
    while(len(not_checked) > 0):
        current_node = queue.popleft()
        not_checked.remove(current_node)
        for other_node in current_node.neighbours:
            best_distances[other_node.index] = min([current_node.get_distance(other_node) + best_distances[current_node.index], best_distances[other_node.index]])
            if(other_node in not_checked):
                queue.append(other_node) 
        print(current_node.index, best_distances)
    return(best_distances[end_node.index])
    
infinite = float('infinity')
N = int(input())
for i in range(N):
    graph = []
    n,m,S,T = map(int,input().split())
    for node in range(n):
        graph.append(Node(node))
    for connection in range(m):
        node1, node2, latency = map(int,input().split())
        graph[node1].add_neighbour(graph[node2], latency)
    distance = solve(graph, graph[S], graph[T])
    if(distance is not infinite):
        print('Case #' + str(i + 1) + ':', distance)
    else:
        print('Case #' + str(i + 1) + ': unreachable')
    