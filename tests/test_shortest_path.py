from app.shortest_path import build_adjacency_list, find_shortest_path

def test_build_adjacency_list(large_sample_edges):
    """
   Test the build_adjacency_list function.

   This test verifies that the `build_adjacency_list` function correctly constructs
   an adjacency list representation of a graph from a list of edges.

   Args:
       large_sample_edges (list[dict]): A fixture providing a list of edges, where each
                                        edge is represented as a dictionary with "user"
                                        and "friend" keys.

   Asserts:
       - The adjacency list for specific nodes is correctly constructed.
   """
    # Act
    adjacency_list = build_adjacency_list(large_sample_edges)

    # Assert: Check that the adjacency list for a few users is built correctly
    assert adjacency_list["1"] == [("2", 1), ("3", 1), ("4", 1), ("5", 1), ("6", 1), ("10", 1)]
    assert adjacency_list["2"] == [("1", 1), ("3", 1), ("8", 1), ("5", 1), ("10", 1)]

def test_find_shortest_path(large_sample_edges):
    """
    Test the find_shortest_path function.

    This test verifies that the `find_shortest_path` function correctly identifies the
    shortest path between two nodes in a graph represented as an adjacency list.

    Args:
        large_sample_edges (list[dict]): A fixture providing a list of edges to construct
                                         the graph's adjacency list.

    Asserts:
        - The shortest path between specific nodes is as expected.
        - If no path exists, the function returns None.
    """
    # Arrange: Build adjacency list from sample edges
    adjacency_list = build_adjacency_list(large_sample_edges)

    # Act: Find the shortest path from user 1 to user 6
    path = find_shortest_path(adjacency_list, "1", "6")
    path2 = find_shortest_path(adjacency_list, "1", "9")
    path3 = find_shortest_path(adjacency_list, "1", "7")

    # Assert: Ensure that the path is correct
    assert path == ["1", "6"]
    assert path2 == ["1", "3", "9"]
    assert path3 == None


