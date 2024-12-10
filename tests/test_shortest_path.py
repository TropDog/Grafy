from app.shortest_path import build_adjacency_list, find_shortest_path

def test_build_adjacency_list(large_sample_edges):
    # Act
    adjacency_list = build_adjacency_list(large_sample_edges)

    # Assert: Check that the adjacency list for a few users is built correctly
    assert adjacency_list["1"] == [("2", 1), ("3", 1), ("4", 1), ("5", 1), ("6", 1), ("10", 1)]
    assert adjacency_list["2"] == [("1", 1), ("7", 1), ("8", 1), ("5", 1), ("10", 1)]

def test_find_shortest_path(large_sample_edges):
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


