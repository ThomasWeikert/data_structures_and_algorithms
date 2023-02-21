# Shortest Path Algorithm

This is an implementation of the A* shortest path algorithm that uses Euclidean distance as a heuristic function. The algorithm finds the shortest path between two points on a map, represented by a collection of intersections and roads.

## Usage
The function `shortest_path` takes three arguments:

- `M`: a Map object that represents the map of the area
- `start`: the index of the intersection where the path should start
- `goal`: the index of the intersection where the path should end

The function returns a list of indices that represent the shortest path from the start intersection to the goal intersection.

## Implementation
The algorithm uses a priority queue to keep track of the next intersection to explore. The priority of each intersection is determined by the sum of its tentative g score (the length of the path from the start intersection to the intersection) and its heuristic function value (the Euclidean distance from the intersection to the goal intersection).

The algorithm starts by initializing the closed set, the open set, and the g score dictionary. The closed set keeps track of the intersections that have been explored. The open set is a priority queue that keeps track of the next intersection to explore. The g score dictionary keeps track of the tentative g score for each intersection.

The algorithm then adds the start intersection to the open set and sets its tentative g score to 0. The algorithm continues to explore the intersections in the open set until the goal intersection is reached or the open set is empty.

At each iteration, the algorithm removes the intersection with the lowest f score from the open set and adds it to the closed set. The algorithm then explores the neighboring intersections and updates their tentative g score if a shorter path is found. If a neighboring intersection is not in the open set, the algorithm adds it to the open set. If a neighboring intersection is already in the open set but the new tentative g score is lower than its current g score, the algorithm updates the tentative g score and adds the intersection to the open set again.

Once the goal intersection is reached, the algorithm reconstructs the path by following the links from the goal intersection back to the start intersection.

If there is no path from the start intersection to the goal intersection, the function returns None.

## Functions

### `distance(point1, point2)`

This function calculates the Euclidean distance between two points represented by tuples of x and y coordinates.

### `shortest_path(M, start, goal)`

This function takes a Map object `M`, the index of the start intersection, and the index of the goal intersection, and returns the shortest path between them as a list of indices. The function uses the A* shortest path algorithm with Euclidean distance as a heuristic function.
