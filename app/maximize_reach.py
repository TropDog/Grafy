import networkx as nx
from data_loader import DataLoader
import matplotlib.pyplot as plt


# Function to calculate total reach of a post
def calculate_total_reach(G, author, tagged):
    """
    Calculates the number of unique people who will see the post
    when the author tags a specific person. Mutual friends are counted only once.
    """
    author_friends = set(G.neighbors(author))
    tagged_friends = set(G.neighbors(tagged))

    # Combine all unique friends and mutual friends
    total_reach = author_friends | tagged_friends | {author, tagged}

    return len(total_reach), total_reach


# Function to find the best person to tag
def find_best_tag(G, user):
    """
    Finds the person whose tag maximizes the reach of the post,
    counting mutual friends only once.
    """
    max_reach = 0
    best_tagged = None
    best_reach_set = set()

    for friend in G.neighbors(user):
        reach, reach_set = calculate_total_reach(G, user, friend)
        if reach > max_reach:
            max_reach = reach
            best_tagged = friend
            best_reach_set = reach_set

    return best_tagged, max_reach, best_reach_set


# Function to visualize the reach of the post
def visualize_reach(G, user, tagged, reach_set):
    """
    Visualizes the subgraph containing the author, the tagged person,
    and the entire reach of the post.
    """
    subgraph = G.subgraph(reach_set)
    pos = nx.spring_layout(subgraph)

    plt.figure(figsize=(8, 8))
    nx.draw(subgraph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
    nx.draw_networkx_nodes(subgraph, pos, nodelist=[user], node_color='green', label="Author")
    nx.draw_networkx_nodes(subgraph, pos, nodelist=[tagged], node_color='red', label="Tagged")
    plt.legend()
    plt.title(f"Reach of post by {user} tagging {tagged}")
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
        user = input("Enter the user ID (or type 'exit' to quit): ")
        if user.lower() == 'exit':
            break

        if user not in G:
            print(f"User {user} not found in the network.")
            continue

        best_tagged, max_reach, reach_set = find_best_tag(G, user)
        if best_tagged:
            print(f"Best person to tag: {best_tagged}")
            print(f"Maximum total reach: {max_reach}")
            print(f"People who see the post: {', '.join(reach_set)}")

            # Optional visualization
            visualize_reach(G, user, best_tagged, reach_set)
        else:
            print(f"User {user} has no friends to tag.")
