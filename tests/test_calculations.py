import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5), 
    (4, 4, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected
    
def test_subtract():
    assert subtract(4, 1) == 3
    
def test_multiply():
    assert multiply(2, 9) == 18
    
def test_divide():
    assert divide(12, 6) == 2
    
def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50
    
def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0
    
def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30
    
def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70
    
def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 5) == 55
  
@pytest.mark.parametrize("deposit, withdraw, expected", [
    (200, 100, 100), 
    (50, 10, 40),
    (1200, 500, 700),
])  
def teste_bank_transaction(zero_bank_account, deposit, withdraw, expected):
    zero_bank_account.deposit(deposit)
    zero_bank_account.withdraw(withdraw)
    
    assert zero_bank_account.balance == expected
    
def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(70)
    
