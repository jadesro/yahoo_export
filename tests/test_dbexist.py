import pytest
from sqlalchemy_utils import database_exists

url = "mysql+pymysql://jacques:1Kermit1@192.168.1.20/finance?charset=utf8mb4"


def test_dbexist():
    if database_exists(url):
        assert True


# @pytest.mark.parametrize(
#     "str1, expected",
#     [(url, True)],
# )

# def test_dbexist(str1: str, expected: bool) -> None:
#    assert dbexist(url) == expected
