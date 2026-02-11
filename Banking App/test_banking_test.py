def test_create_account_valid_output():
    assert card.create_account() == None

def test_log_in_successful_login():
    assert card.log_in() == None

def test_log_in_invalid_card():
    assert card.log_in() == None

def test_log_in_invalid_pin():
    assert card.log_in() == None

def test_success_balance_display():
    assert card.success() == None

def test_success_add_income():
    assert card.success() == None

def test_success_do_transfer():
    assert card.success() == None

def test_success_close_account():
    assert card.success() == None

def test_success_log_out():
    assert card.success() == None

def test_luhn_valid_card_number():
    assert card.luhn('4000001234567890') == 4000001234567890
