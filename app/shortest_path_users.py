import networkx as nx
from data_loader import DataLoader

# Function to find the shortest path and intermediate connections
def find_shortest_path(G, user1, user2):
    """
    Finds the shortest path from user1 to user2 and determines
    intermediate connections if a direct connection is not available.
    """
    if user2 in G.neighbors(user1):
        # Direct connection exists
        print(f"User {user2} is directly connected to User {user1}.")
        print(f"Shortest path: {user1} -> {user2}")
        return [user1, user2]

    try:
        # Find the shortest path
        path = nx.shortest_path(G, source=user1, target=user2)
        print(f"Shortest path from {user1} to {user2}: {' -> '.join(path)}")
        return path
    except nx.NetworkXNoPath:
        # No path exists
        print(f"No path exists between User {user1} and User {user2}.")
        return None

# Function to find intermediate users who can connect user1 to user2
def find_intermediate_connections(G, user1, user2):
    """
    Finds all friends of user1 who can connect to user2 through their own connections.
    """
    intermediate_users = []
    for friend in G.neighbors(user1):
        try:
            # Check if there's a path from the friend to user2
            nx.shortest_path(G, source=friend, target=user2)
            intermediate_users.append(friend)
        except nx.NetworkXNoPath:
            continue
    return intermediate_users

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
    G = nx.Graph()
    for edge in transformed_data["edges"]:
        G.add_edge(edge["user"], edge["friend"])

    # Interactive part
    while True:
        user1 = input("Enter the ID of User 1 (or type 'exit' to quit): ")
        if user1.lower() == 'exit':
            break

        user2 = input("Enter the ID of User 2: ")

        if user1 not in G or user2 not in G:
            print("One or both users do not exist in the network.")
            continue
        # Find the shortest path
        path = find_shortest_path(G, user1, user2)

        if path is None or len(path) > 2:
            # Find intermediate users
            intermediate_users = find_intermediate_connections(G, user1, user2)
            if intermediate_users:
                print(f"Friends of User {user1} who can connect to User {user2}: {', '.join(intermediate_users)}")
                if path:
                    print(f"User {path[1]} should be tagged to reach User {user2} via the shortest path.")
            else:
                print(f"No friends of User {user1} can connect to User {user2}.")
