"""
Module for finding the shortest path and intermediate connections in a social graph.

This module includes functions to:
1. Find the shortest path between two users using Dijkstra's algorithm.
2. Build an adjacency list representation of the graph.
3. Identify intermediate connections between two users.
"""

import heapq

def dijkstra_shortest_path(graph, start, target):
    """
    Finds the shortest path using Dijkstra's algorithm.

    :param graph: Graph represented as an adjacency list {node: [(neighbor, weight), ...]}.
    :param start: Starting node.
    :param target: Target node.
    :return: Shortest path as a list of nodes and the total number of connections.
    """
    queue = [(0, start, [])]  # Priority queue: (cost, node, path)
    visited = set()

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

    :param edges: List of edges, each represented as a dictionary {"user": x, "friend": y}.
    :return: Adjacency list representation of the graph.
    """
    adjacency_list = {}
    for edge in edges:
        user = edge["user"]
        friend = edge["friend"]
        adjacency_list.setdefault(user, []).append((friend, 1))
        adjacency_list.setdefault(friend, []).append((user, 1))
    return adjacency_list

def find_intermediate_connections(adjacency_list, user1, user2):
    """
    Finds all friends of user1 who can connect to user2 through their own connections.

    :param adjacency_list: Graph as an adjacency list.
    :param user1: Starting node.
    :param user2: Target node.
    :return: List of intermediate users.
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

    :param adjacency_list: Graph as an adjacency list.
    :param user1: Starting node.
    :param user2: Target node.
    :return: Shortest path as a list of nodes.
    """
    if user2 in dict(adjacency_list.get(user1, [])):
        print(f"User {user2} is directly connected to User {user1}.")
        print(f"Shortest path: {user1} -> {user2}")
        return [user1, user2]

    path, cost = dijkstra_shortest_path(adjacency_list, user1, user2)
    if path:
        print(f"Shortest path from {user1} to {user2} with {cost} connections: {' -> '.join(map(str, path))}")
        return path

    print(f"No path exists between User {user1} and User {user2}.")
    return None
