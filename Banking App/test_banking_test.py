def test_create_account_generates_valid_card_number():
    assert Card().create_account() == None

def test_log_in_with_valid_credentials():
    assert Card().log_in() == None

def test_log_in_with_invalid_credentials():
    assert Card().log_in() == None

def test_success_view_balance():
    assert Card().success() == None

def test_success_add_income():
    assert Card().success() == None

def test_success_do_transfer():
    assert Card().success() == None

def test_success_do_transfer_insufficient_funds():
    assert Card().success() == None

def test_success_close_account():
    assert Card().success() == None

def test_luhn_valid_card_number():
    assert Card().luhn_2('4000001234567890') == True

def test_luhn_invalid_card_number():
    assert Card().luhn_2('1234567890123456') == False
