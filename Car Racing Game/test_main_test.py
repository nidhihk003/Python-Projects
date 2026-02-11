def test_car_initial_position():
    assert Car().x, Car().y == [460, 530]

def test_car_move_left_within_bounds():
    assert car = Car(); car.move_left(); car.update_position(); car.x == 455

def test_car_move_right_within_bounds():
    assert car = Car(); car.move_right(); car.update_position(); car.x == 465

def test_car_move_forward():
    assert car = Car(); car.move_forward(); car.update_position(); car.y == 525

def test_car_move_backward():
    assert car = Car(); car.move_backward(); car.update_position(); car.y == 535

def test_car_stop_x():
    assert car = Car(); car.stop_x(); car.speed_x == 0

def test_car_stop_y():
    assert car = Car(); car.stop_y(); car.speed_y == 0

def test_road_initial_position():
    assert Road().y == 0

def test_road_move_within_bounds():
    assert road = Road(); road.move(); road.y == 5

def test_create_hurdle():
    assert manager = HurdleManager(); manager.create_hurdle(); len(manager.hurdles) == 1
