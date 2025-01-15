from typing import Optional


from peewee import *
from datetime import date
from .base_model import BaseModel
from .transaction import Transaction

class Portfolio(BaseModel):
    IdPortfolio = AutoField(primary_key=True)
    Name = TextField(null=False, unique=True)
    BaseTicker = TextField(null=False)

    # @classmethod
    # def create_portfolio(cls, name: str, base_ticker: str):
    #     return cls.create(Name=name, BaseTicker=base_ticker)

    @classmethod
    def get_list(cls) -> list['Portfolio']:
        portfolios = cls.select()
        return list(portfolios) 
        
    @classmethod
    def get_by_name(cls, name: str) -> Optional['Portfolio']:
        try:
            portfolio = cls.get(cls.Name == name)
            return portfolio
        except DoesNotExist:
            print(f"Portfolio with name '{name}' does not exist.")
            return None

    @classmethod
    def get_by_id(cls, id: str) -> Optional['Portfolio']:
        try:
            portfolio = cls.get(cls.IdPortfolio == id)
            return portfolio
        except DoesNotExist:
            print(f"Portfolio with name '{id}' does not exist.")
            return None

    def get_balance(self):
        rs = []
        # 1. get tokens list
        tokens = Transaction.get_tokens_list(self.IdPortfolio)

        # 2. get balance for each token
        for token in tokens:
            balance = self.get_token_balance(token)
            rs.append({'token': token, 'balance': balance})
        return rs

    def show_token_balance(self, token: str):
        balance = self.get_token_balance(token)
        print(f"Balance for token '{token}': {balance}")

    def get_token_balance(self, token: str) -> float:
        balance = Transaction.get_balance_by_token(self.IdPortfolio, token)
        return balance

    def get_base_ticker_balance(self) -> float:
        balance = self.get_token_balance(self.BaseTicker)
        return balance

    def deposit_base_ticker(self, amount: float) -> float:
        transaction = Transaction.transaction_add(self.IdPortfolio, 'deposit', amount, self.BaseTicker)
        return transaction.Balance


    def withdraw_base_ticker(self, amount: float) -> float:
        transaction = Transaction.transaction_add(self.IdPortfolio, 'withdraw', amount, self.BaseTicker)
        return transaction.Balance

    def deposit(self, token: str, amount: float) -> float:
        transaction = Transaction.transaction_add(self.IdPortfolio, 'deposit', amount, token)
        return transaction.Balance

    def withdraw(self, token: str, amount:float) -> float:
        transaction = Transaction.transaction_add(self.IdPortfolio, 'withdraw', amount, token)
        return transaction.Balance

    def buy(self, token: str, amount: float, price:float) -> dict:
        base_ticker_balance = self.get_base_ticker_balance()
        total_price = amount * price

        if amount <= 0 or price <= 0:
            raise Exception('Amount or price cant be negative or zero')

        if base_ticker_balance < total_price:
            raise Exception('You dont have enough balance')

        transaction1 = Transaction.transaction_add(self.IdPortfolio, 'buy', amount, token, price)
        transaction2 = Transaction.transaction_add(self.IdPortfolio, 'sell', total_price, self.BaseTicker, parent_transaction=transaction1.IdTransaction)
        return {'buy': transaction1, 'sell': transaction2}

    def sell(self, token: str, amount: float, price:float) -> dict:
        token_balance = self.get_token_balance(token)
        total_price = amount * price

        if amount <= 0 or price <= 0:
            raise Exception('Amount or price cant be negative or zero')

        if token_balance < amount:
            raise Exception(f'You dont have enough {token} balance')

        transaction1 = Transaction.transaction_add(self.IdPortfolio, 'sell', amount, token, price)
        transaction2 = Transaction.transaction_add(self.IdPortfolio, 'buy', total_price, self.BaseTicker, parent_transaction=transaction1.IdTransaction)
        return {'sell': transaction1, 'buy': transaction2}

    def get_last_transactions(self, limit: int) -> list['Transaction']:
        transactions = Transaction.get_last_transactions(self.IdPortfolio, limit)
        return list(transactions)

    # def delete_transaction_by_id(self, transaction_id: int):
    #     Transaction.delete_by_id(transaction_id)
    #
    #
    # def delete_multiple_transactions(self, criteria):
    #     try:
    #         query = Transaction.delete().where(criteria)
    #         rows_deleted = query.execute()
    #         print(f"Deleted {rows_deleted} transaction(s) successfully.")
    #         return rows_deleted
    #     except Exception as e:
    #         print(f"Error deleting transactions: {e}")
    #         return None
    #
    #
    # def deposit(self, token: str, amount: float):
    #     if amount <= 0:
    #         raise Exception('You want to deposit nothing?')
    #
    #     Transaction.transaction_add('deposit', amount, token)
    #
    #
    # def withdraw(self, token: str, amount: float):
    #     token_balance = self.get_balance_by_token(token)
    #
    #     if amount <= 0:
    #         raise Exception('You want to withdraw nothing?')
    #
    #     if token_balance <= amount:
    #         raise Exception('You dont have enough this token(s) to withdraw')
    #
    #     Transaction.transaction_add('withdraw', amount, token)
    #
    #
    # def buy(self, token: str, price: float, amount: float, parent_transaction: int = None):
    #     total = amount * price
    #     base_ticker_balance = self.get_base_ticker_balance()
    #
    #     if amount <= 0:
    #         raise Exception('You want to buy nothing?')
    #
    #     if price <= 0:
    #         raise Exception('Token cant be free or less than 0')
    #
    #     if base_ticker_balance < total:
    #         raise Exception('You dont have enough your base token(s)')
    #
    #     Transaction.transaction_add('buy', amount, token, price)
    #     self.withdraw_base_ticker(total)
    #
    #
    # def sell(self, token: str, price: float, amount: float, parent_transaction: int = None):
    #     token_balance = self.get_balance_by_token(token)
    #
    #     if amount <= 0:
    #         raise Exception('You want to sell nothing?')
    #
    #     if price <= 0:
    #         raise Exception('Token cant be free or less than 0')
    #
    #     if token_balance <= amount:
    #         raise Exception('You dont have this token(s) to sell')
    #
    #     total = int(amount * price)
    #     Transaction.transaction_add('sell', amount, token, price)
    #     self.deposit_base_ticker(total)
    #