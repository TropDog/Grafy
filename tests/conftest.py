import pytest
import networkx as nx

@pytest.fixture
def large_sample_edges():
    """Provide a large list of sample edges for testing."""
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
    """Provide a large NetworkX graph for testing."""
    graph = nx.Graph()
    for edge in large_sample_edges:
        graph.add_edge(int(edge["user"]), int(edge["friend"]))
    return graph
