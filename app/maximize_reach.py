"""
Module for calculating and visualizing the reach of a user in a social graph.

This module includes functions to:
1. Calculate the total reach of a post when a specific user is tagged.
2. Find the best person to tag to maximize reach.
3. Visualize the subgraph of users impacted by a post.
"""

import networkx as nx
import matplotlib.pyplot as plt

def calculate_total_reach_bfs(graph, author, tagged):
    """
    Calculates the reach using BFS when the author tags a specific person.
    Combines the reach of the author and tagged person, counting unique nodes only.

    :param graph: NetworkX graph object representing the social network.
    :param author: ID of the author making the post.
    :param tagged: ID of the user tagged in the post.
    :return: A tuple containing the size of the total reach and the set of reached nodes.
    """
    # Get friends of the author and tagged person
    author_friends = set(graph.neighbors(author))
    tagged_friends = set(graph.neighbors(tagged))

    # Include both the author and the tagged person in the reach
    total_reach = (author_friends | tagged_friends) - {author}
    return len(total_reach), total_reach

def find_best_tag_bfs(graph, user):
    """
    Finds the best person to tag to maximize reach using BFS.

    :param graph: NetworkX graph object representing the social network.
    :param user: ID of the user posting.
    :return: A tuple containing the best user to tag, the size of the maximum reach,
             and the set of reached nodes.
    """
    max_reach = 0
    best_tagged = None
    best_reach_set = set()

    # Iterate through all neighbors of the user
    for friend in graph.neighbors(user):
        reach, reach_set = calculate_total_reach_bfs(graph, user, friend)
        if reach > max_reach:
            max_reach = reach
            best_tagged = friend
            best_reach_set = reach_set

    return best_tagged, max_reach, best_reach_set

def visualize_reach(graph, user, tagged, reach_set):
    """
    Visualizes the subgraph containing the author, the tagged person,
    and the entire reach of the post.

    :param graph: NetworkX graph object representing the social network.
    :param user: ID of the user posting.
    :param tagged: ID of the user tagged in the post.
    :param reach_set: Set of IDs of users impacted by the post.
    """
    subgraph = graph.subgraph(reach_set)
    pos = nx.spring_layout(subgraph)

    plt.figure(figsize=(8, 8))
    nx.draw(subgraph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
    nx.draw_networkx_nodes(subgraph, pos, nodelist=[user], node_color='green', label="Author")
    nx.draw_networkx_nodes(subgraph, pos, nodelist=[tagged], node_color='red', label="Tagged")
    plt.legend()
    plt.title(f"Reach of post by {user} tagging {tagged}")
    plt.show()
