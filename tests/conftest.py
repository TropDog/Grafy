import pytest
import networkx as nx

@pytest.fixture
def large_sample_edges():
    """
    Provide a large list of sample edges for testing.

    This fixture returns a list of dictionaries, where each dictionary represents
    an edge in a graph with keys "user" and "friend" indicating connected nodes.

    Returns:
        list[dict]: A list of edges represented as dictionaries with "user" and "friend" keys.
    """

    return [
        {"user": "1", "friend": "2"},
        {"user": "1", "friend": "3"},
        {"user": "1", "friend": "4"},
        {"user": "1", "friend": "5"},
        {"user": "1", "friend": "6"},
        {"user": "2", "friend": "3"},
        {"user": "2", "friend": "8"},
        {"user": "3", "friend": "9"},
        {"user": "4", "friend": "10"},
        {"user": "5", "friend": "2"},
        {"user": "6", "friend": "10"},
        {"user": "7", "friend": "11"},
        {"user": "8", "friend": "4"},
        {"user": "9", "friend": "5"},
        {"user": "10", "friend": "2"},
        {"user": "10", "friend": "1"}
    ]

@pytest.fixture
def large_sample_graph(large_sample_edges):
    """
    Provide a large NetworkX graph for testing.

    This fixture uses the `large_sample_edges` fixture to create a NetworkX undirected graph.
    Each edge in the graph is created by connecting the nodes defined in the edge list.

    Args:
        large_sample_edges (list[dict]): A list of edges, where each edge is a dictionary
                                         with "user" and "friend" keys.

    Returns:
        networkx.Graph: A NetworkX graph constructed from the provided edge list.
    """
    graph = nx.Graph()
    for edge in large_sample_edges:
        graph.add_edge(int(edge["user"]), int(edge["friend"]))
    return graph
