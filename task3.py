import heapq

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    my_heap = [(0, starting_vertex)]
    while len(my_heap) > 0:
        current_distance, current_vertex = heapq.heappop(my_heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(my_heap, (distance, neighbor))

    return distances

# тестовий кейс
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 1},
    'D': {'B': 1, 'C': 1},
}

print("Відстані від A:")
print(calculate_distances(graph, 'A'))  # {'A': 0, 'B': 1, 'C': 3, 'D': 2}