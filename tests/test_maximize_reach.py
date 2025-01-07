from app.maximize_reach import calculate_total_reach_bfs, find_best_tag_bfs

def test_calculate_total_reach_bfs(large_sample_graph):
    """
    Test the calculate_total_reach_bfs function.

    This test verifies that the `calculate_total_reach_bfs` function correctly calculates
    the total number of reachable nodes and the set of reachable nodes in a graph using
    Breadth-First Search (BFS).

    Args:
        large_sample_graph (networkx.Graph): A fixture providing a test graph.

    Asserts:
        - The total reach count is as expected.
        - The set of reachable nodes matches the expected set.
    """
    # Act
    reach_count, reach_set = calculate_total_reach_bfs(large_sample_graph, 1, 2)

    # Assert
    assert reach_count == 7
    assert reach_set == {2, 3, 4, 5, 6, 8, 10}

def test_find_best_tag_bfs(large_sample_graph):
    """
    Test the find_best_tag_bfs function.

    This test verifies that the `find_best_tag_bfs` function correctly identifies the
    best starting node for maximizing reach using BFS, as well as the corresponding reach
    count and set of reachable nodes.

    Args:
        large_sample_graph (networkx.Graph): A fixture providing a test graph.

    Asserts:
        - The best starting node (tag) is correctly identified.
        - The maximum reach count is as expected.
    """
    # Act
    best_tagged, max_reach, reach_set = find_best_tag_bfs(large_sample_graph, 2)

    # Assert
    assert best_tagged == 1
    assert max_reach == 7
