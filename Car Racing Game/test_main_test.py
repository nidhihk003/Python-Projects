def test_car_initial_position():
    assert Car().x == 460

def test_car_move_left_within_bounds():
    assert car = Car(); car.move_left(); car.x == 455

def test_car_move_right_within_bounds():
    assert car = Car(); car.move_right(); car.x == 465

def test_car_move_forward():
    assert car = Car(); car.move_forward(); car.speed_y == -5

def test_car_move_backward():
    assert car = Car(); car.move_backward(); car.speed_y == 5

def test_road_initial_position():
    assert Road().y == 0

def test_road_move_down():
    assert road = Road(); road.move(); road.y == 5

def test_hurdle_manager_create_hurdle():
    assert hurdle_manager = HurdleManager(); hurdle_manager.create_hurdle(); len(hurdle_manager.hurdles) == 1

def test_hurdle_manager_move_hurdles():
    assert hurdle_manager = HurdleManager(); hurdle_manager.create_hurdle(); hurdle_manager.move_hurdles(); hurdle_manager.hurdles[0].y == -15

def test_update_score():
    assert game = Game(); game.update_score(); game.score == 1
