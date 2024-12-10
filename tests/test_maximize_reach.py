from app.maximize_reach import calculate_total_reach_bfs, find_best_tag_bfs

def test_calculate_total_reach_bfs(large_sample_graph):
    # Act
    reach_count, reach_set = calculate_total_reach_bfs(large_sample_graph, 1, 2)

    # Assert
    assert reach_count == 8
    assert reach_set == {2, 3, 4, 5, 6, 7, 8, 10}

def test_find_best_tag_bfs(large_sample_graph):
    # Act
    best_tagged, max_reach, reach_set = find_best_tag_bfs(large_sample_graph, 2)

    # Assert
    assert best_tagged == 1
    assert max_reach == 8
