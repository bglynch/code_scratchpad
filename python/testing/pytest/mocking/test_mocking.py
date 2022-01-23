from unittest.mock import patch, MagicMock
from utils import foo

def test_mock_db_write():
  assert foo() == 2

# NOTE: path in patch is where the function is used....NOT where it is defined
#       PATCH WHERE OBJECT IS USED
# Can see that write_db and read_db parent are utils even though read_db is defined in database.py

@patch('utils.write_db', MagicMock(return_value=10))
def test_mock_db_write_with_patch_1():
  assert foo() == 11

@patch('utils.read_db', MagicMock(return_value=10))
def test_mock_db_write_with_patch_2():
  assert foo() == 11


@patch('utils.read_db', MagicMock(return_value=10))
@patch('utils.write_db', MagicMock(return_value=10))
def test_mock_db_write_with_patch_3():
  assert foo() == 20

