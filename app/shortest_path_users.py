import heapq
from data_loader import DataLoader

def dijkstra_shortest_path(graph, start, target):
    """
    Finds the shortest path using Dijkstra's algorithm.

    :param graph: Graph represented as an adjacency list {node: [(neighbor, weight), ...]}
    :param start: Starting node
    :param target: Target node
    :return: Shortest path as a list of nodes and the total number of connections.
    """
    queue = [(0, start, [])]  # Priority queue: (cost, node, path)
    visited = set()  # Set of visited nodes

    while queue:
        cost, current_node, path = heapq.heappop(queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        path = path + [current_node]

        if current_node == target:
            return path, cost

        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return None, float('inf')

def build_adjacency_list(edges):
    """
    Builds an adjacency list representation of the graph from the edge list.

    :param edges: List of edges, each represented as a dictionary {"user": x, "friend": y}
    :return: Adjacency list representation of the graph
    """
    adjacency_list = {}
    for edge in edges:
        user = edge["user"]
        friend = edge["friend"]

        # Since this is an unweighted graph, assign weight 1 to all edges
        adjacency_list.setdefault(user, []).append((friend, 1))
        adjacency_list.setdefault(friend, []).append((user, 1))
    return adjacency_list

def find_intermediate_connections(adjacency_list, user1, user2):
    """
    Finds all friends of user1 who can connect to user2 through their own connections.

    :param adjacency_list: Graph as an adjacency list
    :param user1: Starting node
    :param user2: Target node
    :return: List of intermediate users
    """
    intermediate_users = []
    for neighbor, _ in adjacency_list.get(user1, []):
        path, _ = dijkstra_shortest_path(adjacency_list, neighbor, user2)
        if path:
            intermediate_users.append(neighbor)
    return intermediate_users

def find_shortest_path(adjacency_list, user1, user2):
    """
    Finds the shortest path from user1 to user2 using Dijkstra's algorithm.

    :param adjacency_list: Graph as an adjacency list
    :param user1: Starting node
    :param user2: Target node
    :return: Shortest path as a list of nodes
    """
    if user2 in dict(adjacency_list.get(user1, [])):
        print(f"User {user2} is directly connected to User {user1}.")
        print(f"Shortest path: {user1} -> {user2}")
        return [user1, user2]

    path, cost = dijkstra_shortest_path(adjacency_list, user1, user2)
    if path:
        print(f"Shortest path from {user1} to {user2} with {cost} connections: {' -> '.join(map(str, path))}")
        return path
    else:
        print(f"No path exists between User {user1} and User {user2}.")
        return None

# Main part of the program
if __name__ == "__main__":
    # Load data using DataLoader
    file_path = "../data/facebook_combined.txt"
    loader = DataLoader(file_path)

    try:
        data = loader.load_csv()
        print("Data successfully loaded!")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise

    try:
        transformed_data = loader.transform_data(data)
        print("Data transformation completed successfully!")
    except Exception as e:
        print(f"Error during data transformation: {e}")
        raise

    # Build the graph
    print("Building the graph...")
    adjacency_list = build_adjacency_list(transformed_data["edges"])

    # Interactive part
    while True:
        user1 = input("Enter the ID of User 1 (or type 'exit' to quit): ")
        if user1.lower() == 'exit':
            break

        user2 = input("Enter the ID of User 2: ")

        if user1 not in adjacency_list or user2 not in adjacency_list:
            print("One or both users do not exist in the network.")
            continue

        # Find the shortest path
        path = find_shortest_path(adjacency_list, user1, user2)

        if path is None or len(path) > 2:
            # Find intermediate users
            intermediate_users = find_intermediate_connections(adjacency_list, user1, user2)
            if intermediate_users:
                print(f"Friends of User {user1} who can connect to User {user2}: {', '.join(map(str, intermediate_users))}")
                if path:
                    print(f"User {path[1]} should be tagged to reach User {user2} via the shortest path.")
            else:
                print(f"No friends of User {user1} can connect to User {user2}.")
