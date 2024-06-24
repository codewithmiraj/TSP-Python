import numpy as np
import matplotlib.pyplot as plt

'''get a list of cities and distances'''

cities = ['London', 'Birmingham', 'Bristol', 'Sheffield']

'''distance matrix'''

distances = np.array([[0, 10, 15, 20],
                      [10, 0, 35, 25],
                      [15, 35, 0, 30],
                      [20, 25, 30, 0]])
city_coords = {
    'London': (0, 0),
    'Birmingham': (1, 3),
    'Bristol': (4, 1),
    'Sheffield': (3, 4)
}

'''implementing nearest neighbour algorithm'''

def nearest_neighbour(distances):
    n = distances.shape[0]
    current_city = 0  # Starting at London
    route = [current_city]  # Initialize route with the starting city index
    visited = set(route)  # Initialize visited cities with the starting city

    while len(visited) < n:
        nearest_city = min(
            [(i, distances[current_city][i]) for i in range(n) if i not in visited],
            key=lambda x: x[1]
        )[0]
        route.append(nearest_city)
        visited.add(nearest_city)
        current_city = nearest_city

    route.append(0)  # Return back to the initial city (London)
    return route

'''Applying algorithm'''

route_indices = nearest_neighbour(distances)
route_cities = [cities[i] for i in route_indices]
print("Best route:", route_cities)
print("Total Distance:", total_distance)


'''Visualising algorithm'''

plt.figure(figsize=(10, 6))
for city, coord in city_coords.items():
    plt.scatter(coord[0], coord[1], s=100)
    plt.text(coord[0] + 0.1, coord[1] + 0.1, city, fontsize=12)

# Plot the routes
for i in range(len(route_cities) - 1):
    start_city = route_cities[i]
    end_city = route_cities[i + 1]
    start_coord = city_coords[start_city]
    end_coord = city_coords[end_city]
    plt.arrow(start_coord[0], start_coord[1], 
              end_coord[0] - start_coord[0], end_coord[1] - start_coord[1],
              length_includes_head=True, head_width=0.1, color='blue')

plt.title('Nearest Neighbour Route')
plt.xlabel('index')
plt.ylabel('Distance')
plt.grid(True)
plt.show()