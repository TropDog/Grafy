import networkx as nx
import matplotlib.pyplot as plt
from data_loader import DataLoader


# Function to display friends of a given user
def display_user_friends(G, user):
    """
    Displays the number of friends and all friends of the given user.
    Additionally, visualizes the user and their friends as a graph.
    """
    if user not in G:
        print(f"User {user} not found in the network.")
        return

    friends = list(G.neighbors(user))
    if friends:
        print(f"User {user} has {len(friends)} friends: {', '.join(map(str, friends))}")

        # Visualize the graph
        visualize_friends_graph(G, user, friends)
    else:
        print(f"User {user} has no friends.")


# Function to visualize the user and their friends as a graph
def visualize_friends_graph(G, user, friends):
    """
    Visualizes the user and their friends as a subgraph.
    """
    subgraph = nx.Graph()
    subgraph.add_node(user, color='blue')  # Add the main user with a distinct color
    for friend in friends:
        subgraph.add_node(friend, color='green')  # Add friends
        subgraph.add_edge(user, friend)  # Add edges

    # Set up colors
    colors = [data['color'] for _, data in subgraph.nodes(data=True)]

    # Draw the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(subgraph)  # Position nodes for visualization
    nx.draw(subgraph, pos, with_labels=True, node_color=colors, node_size=500, font_size=10, font_color="white")
    plt.title(f"User {user} and their friends", fontsize=14)
    plt.show()


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
        user = input("Enter the user ID to display friends (or type 'exit' to quit): ")
        if user.lower() == 'exit':
            break

        display_user_friends(G, user)
