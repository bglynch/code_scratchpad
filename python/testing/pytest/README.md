# Pytest

[Blog](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)

Install

```bash
pip install pytest
pipenv install pytest --dev
```

Naming

```bash
test_something.py    # test file must be prefixed with 'test'
```

Running a test

```bash
cd test_folder/

# Run all tests in a folder
pytest

# Run a specific test
pytest -q test_file.py
```

See fixtures

```bash
pytest --fixtures
```

Other flags: [Link](https://docs.pytest.org/en/6.2.x/reference.html?highlight=q#command-line-flags)

```bash
pytest -x           # stop after first failure
pytest --maxfail=2  # stop after two failures

pytest -q           # decrease verbosity.
```



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

