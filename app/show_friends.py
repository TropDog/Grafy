import networkx as nx
from data_loader import DataLoader


# Function to display friends of a given user
def display_user_friends(G, user):
    """
    Displays the number of friends and all friends of the given user.
    """
    if user not in G:
        print(f"User {user} not found in the network.")
        return

    friends = list(G.neighbors(user))
    if friends:
        print(f"User {user} has {len(friends)} friends: {', '.join(friends)}")
    else:
        print(f"User {user} has no friends.")


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
