def test_update_empty_grid_no_progress():
    assert update(pygame.Surface((800, 600)), np.zeros((5, 5)), 10) == np.zeros((5, 5))

def test_update_single_alive_cell_no_progress():
    assert update(pygame.Surface((800, 600)), np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 10) == np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def test_update_block_pattern_no_progress():
    assert update(pygame.Surface((800, 600)), np.array([[0, 1, 1], [0, 1, 1], [0, 0, 0]]), 10) == np.array([[0, 1, 1], [0, 1, 1], [0, 0, 0]])

def test_update_blinker_pattern_no_progress():
    assert update(pygame.Surface((800, 600)), np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), 10) == np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])

def test_update_alive_cell_with_three_neighbors_no_progress():
    assert update(pygame.Surface((800, 600)), np.array([[1, 1, 0], [1, 0, 0], [1, 0, 0]]), 10) == np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])

def test_update_all_cells_alive_no_progress():
    assert update(pygame.Surface((800, 600)), np.ones((3, 3)), 10) == np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1]])

def test_update_empty_grid_with_progress():
    assert update(pygame.Surface((800, 600)), np.zeros((5, 5)), 10, with_progress=True) == np.zeros((5, 5))

def test_update_single_alive_cell_with_progress():
    assert update(pygame.Surface((800, 600)), np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 10, with_progress=True) == np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def test_update_block_pattern_with_progress():
    assert update(pygame.Surface((800, 600)), np.array([[0, 1, 1], [0, 1, 1], [0, 0, 0]]), 10, with_progress=True) == np.array([[0, 1, 1], [0, 1, 1], [0, 0, 0]])

def test_update_blinker_pattern_with_progress():
    assert update(pygame.Surface((800, 600)), np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), 10, with_progress=True) == np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
