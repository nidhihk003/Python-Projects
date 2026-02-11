def test_update_empty_grid():
    assert update(pygame.Surface((800, 600)), np.zeros((5, 5)), 10) == np.zeros((5, 5))

def test_update_single_cell():
    assert update(pygame.Surface((800, 600)), np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 10) == np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def test_update_underpopulation():
    assert update(pygame.Surface((800, 600)), np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]]), 10) == np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def test_update_overpopulation():
    assert update(pygame.Surface((800, 600)), np.array([[1, 1, 1], [1, 1, 0], [0, 0, 0]]), 10) == np.array([[1, 0, 1], [1, 0, 0], [0, 0, 0]])

def test_update_survival():
    assert update(pygame.Surface((800, 600)), np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]]), 10) == np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])

def test_update_reproduction():
    assert update(pygame.Surface((800, 600)), np.array([[0, 1, 0], [1, 1, 0], [0, 0, 0]]), 10) == np.array([[1, 1, 0], [1, 1, 0], [0, 0, 0]])

def test_update_with_progress():
    assert update(pygame.Surface((800, 600)), np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 10, with_progress=True) == np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def test_update_still_life():
    assert update(pygame.Surface((800, 600)), np.array([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]), 10) == np.array([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])

def test_update_oscillator():
    assert update(pygame.Surface((800, 600)), np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), 10) == np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])

def test_update_empty_grid_with_progress():
    assert update(pygame.Surface((800, 600)), np.zeros((5, 5)), 10, with_progress=True) == np.zeros((5, 5))
