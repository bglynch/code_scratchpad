# Pytest

[Blog](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)

## Install

```bash
pip install pytest
pipenv install pytest --dev
```

Naming

```bash
test_something.py    # test file must be prefixed with 'test'
```

## CLI

```bash
cd test_folder/

pytest                                              # Run all tests in a folder
pytest -q test_file.py                              # Run a specific test file
pytest test_2_fixtures.py::test_wallet_spend_cash   # Run specific test
pytest -k test_wallet_add_cash                      # Run specific test
pytest test_2_fixtures.py -k test_wallet_spend_cash # Run specific test

```

See fixtures

```bash
pytest --fixtures
```

Other flags: [Link](https://docs.pytest.org/en/6.2.x/reference.html?highlight=q#command-line-flags)

```bash
pytest -x           # stop after first failure
pytest --maxfail=2  # stop after two failures

pytest -v                 # verbose console output
pytest -q                 # decrease verbosity.
pytest -s                 # see print statements in console output
pytest -m webtest         # run tests with the marker 'webtest'
pytest -m "not webtest"   # run tests without the marker 'webtest'
pytest --durations=3      # show the 3 slowest tests
```

## Assertions

Basic

```python
def f():
    return 3

def test_function():
    assert f() == 4
```

Expected Exception

```python
import pytest

# basic
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# with assertion
def some_function() -> None:
  raise ValueError("Special Error")
 
def test_some_function():
  with pytest.raises(ValueError) as e:
    some_function()
  assert "Special Error" == str(e.value)
```

Assert Logs: by default only works for WARNING logs and above

```python
def function_that_logs_something():
	try:
    raise ValueError("Special Error")
  except:
    logger.warning(f"I am logging {str(e)}")

def test_logged_warning_level(caplog):
  function_that_logs_something()
  assert "I am logging Special Error" == caplog.text

# example for INFO level logs
def test_info_level_logs(caplog):
  with caplog.at_level(logging.INFO):
    logger.info("I am logging info level")
    assest "I am logging info level" in caplog.text
```





### Mark

https://docs.pytest.org/en/6.2.x/example/markers.html

Pytest Mark is a way to tag a test with a certain property. Can use pytest builtin markers or can create custom markers. View builtins with `pytest --markers`







### Fixtures

Removes the repetition of initialising classes for each test. Similat to SetUp in unites

Example test file with no fxtures

```python
import pytest
from wallet import Wallet, InsufficientAmount


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
```

Fixtures added. Can see parameters are now passed into the test functions

```python
import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)
```



### Mocking

[Doc on mocking](https://docs.python.org/3/library/unittest.mock.html)

```python
from unittest.mock import MagicMock

>>> mock = MagicMock()
>>> type(mock)
<class 'unittest.mock.MagicMock'>
>>> dir(mock)
['assert_any_call', 'assert_called', 'assert_called_once', 'assert_called_once_with', 'assert_called_with', 'assert_has_calls', 'assert_not_called', 'attach_mock', 'call_args', 'call_args_list', 'call_count', 'called', 'configure_mock', 'method_calls', 'mock_add_spec', 'mock_calls', 'reset_mock', 'return_value', 'side_effect']

# call mock
>>> mock()
<MagicMock name='mock()' id='4498011232'>

>>> mock.foo()
<MagicMock name='mock.foo()' id='4498051760'>

>>> mock.foo(name="brian")
<MagicMock name='mock.foo()' id='4498051760'>

# assert mock is called only once - PASS
>>> mock.assert_called_once()
>>> mock.assert_called_once()

# call mock a second time
>>> mock()
<MagicMock name='mock()' id='4498011232'>

# assert mock is called only once - FAIL
>>> mock.assert_called_once()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/brianlynch/.pyenv/versions/3.8.10/lib/python3.8/unittest/mock.py", line 892, in assert_called_once
    raise AssertionError(msg)
AssertionError: Expected 'mock' to have been called once. Called 2 times.
Calls: [call(), call.foo(), call.foo(name='brian'), call()].

>>> mock.foo.assert_called_once()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/brianlynch/.pyenv/versions/3.8.10/lib/python3.8/unittest/mock.py", line 892, in assert_called_once
    raise AssertionError(msg)
AssertionError: Expected 'foo' to have been called once. Called 2 times.
Calls: [call(), call(name='brian')].

# make a mock return an Error
>>> mock_with_error = MagicMock(side_effect=ValueError("eden"))
>>> mock_with_error()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/brianlynch/.pyenv/versions/3.8.10/lib/python3.8/unittest/mock.py", line 1081, in __call__
    return self._mock_call(*args, **kwargs)
  File "/Users/brianlynch/.pyenv/versions/3.8.10/lib/python3.8/unittest/mock.py", line 1085, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
  File "/Users/brianlynch/.pyenv/versions/3.8.10/lib/python3.8/unittest/mock.py", line 1140, in _execute_mock_call
    raise effect
ValueError: eden
```

