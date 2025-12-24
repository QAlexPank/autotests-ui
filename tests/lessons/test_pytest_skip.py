import pytest


@pytest.mark.skip(reason="Фича в разработке") # Указывается маркировка, которая пропустит автотест
def test_feature_in_development():
    pass

class TestSuiteScip:
    @pytest.mark.skip(reason="Фича в разработке")
    def test_feature_in_development_1(self):
        pass

    def test_feature_in_development_2(self):
        pass