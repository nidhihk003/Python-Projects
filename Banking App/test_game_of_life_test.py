def test_update_all_dead_cells():
    assert update(pygame.Surface((10, 10)), np.zeros((3, 3)), 1) == np.zeros((3, 3))

def test_update_single_alive_cell():
    assert update(pygame.Surface((10, 10)), np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 1) == np.zeros((3, 3))

def test_update_block_pattern_stable():
    assert update(pygame.Surface((10, 10)), np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]]), 1) == np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])

def test_update_blinker_pattern_oscillation():
    assert update(pygame.Surface((10, 10)), np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), 1) == np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])

def test_update_with_progress_false():
    assert update(pygame.Surface((10, 10)), np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), 1, with_progress=False) == np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])

def test_update_all_alive_cells_stay_alive():
    assert update(pygame.Surface((10, 10)), np.ones((3, 3)), 1) == np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1]])

def test_update_edge_case_top_left_corner():
    assert update(pygame.Surface((10, 10)), np.array([[1, 1, 0], [1, 0, 0], [0, 0, 0]]), 1) == np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])

def test_update_edge_case_bottom_right_corner():
    assert update(pygame.Surface((10, 10)), np.array([[0, 0, 0], [0, 0, 0], [0, 1, 1]]), 1) == np.array([[0, 0, 0], [0, 0, 0], [0, 1, 1]])

def test_update_invalid_input_non_integer_size():
    assert update(pygame.Surface((10, 10)), np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), 'invalid') == TypeError

def test_update_invalid_input_non_array_cells():
    assert update(pygame.Surface((10, 10)), 'invalid', 1) == TypeError
