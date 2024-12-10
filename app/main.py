"""
Main module for interacting with the social graph application.

This module provides an interactive API for users to:
1. Display a user's friends.
2. Find the best friend to tag for maximum reach.
3. Display the shortest path between two users in the network.
"""
import networkx as nx
from data_loader import DataLoader
from show_friends import display_user_friends
from maximize_reach import find_best_tag_bfs, visualize_reach
from shortest_path import build_adjacency_list, find_shortest_path

def main():
    """
    Entry point for the social graph application.
    """
    file_path = "../data/facebook_combined.txt"
    loader = DataLoader(file_path)

    try:
        data = loader.load_csv()
        print("Data successfully loaded!")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    try:
        transformed_data = loader.transform_data(data)
        print("Data transformation completed successfully!")
    except Exception as error:  # Avoid catching broad exceptions
        print(f"Error during data transformation: {error}")
        return

    # Build graph for NetworkX
    graph = nx.Graph()
    for edge in transformed_data["edges"]:
        graph.add_edge(edge["user"], edge["friend"])

    # Build adjacency list for shortest path calculations
    adjacency_list = build_adjacency_list(transformed_data["edges"])

    # Simple API
    while True:
        print("\nChoose an action:")
        print("1. Display friends of a user")
        print("2. Find the best friend to tag for maximum reach")
        print("3. Display the shortest path between two users")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            user = input("Enter the user ID to display friends: ")
            display_user_friends(graph, user)
        elif choice == "2":
            user = input("Enter the user ID to find the best tag: ")
            if user in graph:
                best_tagged, max_reach, reach_set = find_best_tag_bfs(graph, user)
                if best_tagged:
                    print(f"Best person to tag: {best_tagged}")
                    print(f"Maximum total reach: {max_reach}")
                    visualize_reach(graph, user, best_tagged, reach_set)
                else:
                    print(f"User {user} has no friends to tag.")
            else:
                print(f"User {user} not found in the network.")
        elif choice == "3":
            user1 = input("Enter the ID of User 1: ")
            user2 = input("Enter the ID of User 2: ")
            if user1 in adjacency_list and user2 in adjacency_list:
                find_shortest_path(adjacency_list, user1, user2)
            else:
                print("One or both users do not exist in the network.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
