import heapq
import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def shortest_path(M, start, goal):
    # Get the coordinates of the start and goal nodes
    start_coords = M.intersections[start]
    goal_coords = M.intersections[goal]
    
    # Define the heuristic function as Euclidean distance
    def heuristic(node):
        return math.sqrt((node[0] - goal_coords[0]) ** 2 + (node[1] - goal_coords[1]) ** 2)
    
    # Initialize the closed set, the open set, and the g score dictionary
    closed_set = set()
    open_set = [(heuristic(start_coords), start)]
    g_score = {start: 0}
    
    # Initialize the came_from dictionary and the current node
    came_from = {}
    current = None
    
    while open_set:
        # Get the node with the lowest f score from the open set
        current = heapq.heappop(open_set)[1]
        
        # If the current node is the goal, reconstruct and return the path
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]
        
        # Add the current node to the closed set
        closed_set.add(current)
        
        # Explore the neighbors of the current node
        for neighbor in M.roads[current]:
            # If the neighbor is in the closed set, skip it
            if neighbor in closed_set:
                continue
            
            # Compute the tentative g score for the neighbor
            tentative_g_score = g_score[current] + distance(M.intersections[current], M.intersections[neighbor])
            
            # If the neighbor is not in the open set, add it
            if neighbor not in [n[1] for n in open_set]:
                heapq.heappush(open_set, (tentative_g_score + heuristic(M.intersections[neighbor]), neighbor))
            # If the tentative g score is greater than or equal to the current g score for the neighbor, skip it
            elif tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue
            
            # This path is the best until now. Record it!
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            
    # If we reach here, there is no path from the start to the goal
    return None
