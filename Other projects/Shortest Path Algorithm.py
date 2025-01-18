my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    """
    Compute the shortest paths and distances from a starting node to all other nodes 
    in an undirected graph using Dijkstra's algorithm.

    Parameters:
        graph (dict): A dictionary representing the graph where keys are node names,
                      and values are lists of tuples (neighbor, weight).
        start (str): The starting node for the path search.
        target (str): A specific target node to display the shortest path. 
                      If empty, all nodes will be displayed.

    Returns:
        tuple: A dictionary of shortest distances and a dictionary of paths for each node.
    """
    # Initialize unvisited nodes and distances
    unvisited = list(graph)  # Nodes that haven't been processed yet
    distances = {
        node: 0 if node == start else float('inf') for node in graph
    }  # Distance from start to each node
    paths = {node: [] for node in graph}  # Stores the shortest path to each node
    paths[start].append(start)  # Start node's path is itself

    # Process nodes until all are visited
    while unvisited:
        # Select the unvisited node with the smallest distance
        current = min(unvisited, key=distances.get)
        
        # Update distances and paths for neighbors of the current node
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]  # Update shortest distance
                
                # Update the path to the current node
                if paths[node] and paths[node][-1] == node:  # Prevent duplicates
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)

        # Mark the current node as visited
        unvisited.remove(current)

    # Determine nodes to display paths for
    targets_to_print = [target] if target else graph  # Display only the target node or all
    for node in targets_to_print:
        if node == start:  # Skip the starting node
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths

# Run the shortest path algorithm starting from node 'A' and targeting node 'F'
shortest_path(my_graph, 'A', 'F')