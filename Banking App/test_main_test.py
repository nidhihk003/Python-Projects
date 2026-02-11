def test_car_initial_position():
    assert Car().x == 460

def test_car_initial_y_position():
    assert Car().y == 530

def test_car_move_left_boundary():
    assert car = Car(); car.move_left(); car.update_position(); car.x == 455

def test_car_move_right_boundary():
    assert car = Car(); car.move_right(); car.update_position(); car.x == 465

def test_car_move_forward():
    assert car = Car(); car.move_forward(); car.update_position(); car.y == 525

def test_car_move_backward():
    assert car = Car(); car.move_backward(); car.update_position(); car.y == 535

def test_car_stop_x_movement():
    assert car = Car(); car.move_left(); car.stop_x(); car.update_position(); car.x == 460

def test_car_stop_y_movement():
    assert car = Car(); car.move_forward(); car.stop_y(); car.update_position(); car.y == 530

def test_road_initial_position():
    assert Road().y == 0

def test_road_move():
    assert road = Road(); road.move(); road.y == 5
