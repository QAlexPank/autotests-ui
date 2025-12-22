def test_user_login():
    print('Hello')

class TestUser:
    def test_user(self):
        print('Hi')

    def test_admin(self):
        print('Greetings!')

def test_assert_positive_case():
    assert (2 + 2) == 4
    assert (3 + 3) == 6
    assert (4 + 4) == 8

def test_assert_negative_case():
    assert (2 + 2) == 5, "2 + 2 != 5"
