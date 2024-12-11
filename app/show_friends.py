"""
Module for displaying a user's friends and visualizing their social connections.

This module provides functions to:
1. Display the number of friends and their IDs for a given user.
2. Visualize the user's social graph.
"""

import networkx as nx
import matplotlib.pyplot as plt

def display_user_friends(graph, user):
    """
    Displays the number of friends and all friends of the given user.
    Additionally, visualizes the user and their friends as a graph.

    :param graph: NetworkX graph object representing the social network.
    :param user: ID of the user whose friends will be displayed.
    """
    if user not in graph:
        print(f"User {user} not found in the network.")
        return

    friends = list(graph.neighbors(user))
    if friends:
        print(f"User {user} has {len(friends)} friends: {', '.join(map(str, friends))}")
        # Visualize the graph
        visualize_friends_graph(graph, user, friends)
    else:
        print(f"User {user} has no friends.")

def visualize_friends_graph(graph, user, friends):
    """
    Visualizes the user and their friends as a subgraph.

    :param graph: NetworkX graph object representing the social network.
    :param user: ID of the user to visualize.
    :param friends: List of IDs of the user's friends.
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
