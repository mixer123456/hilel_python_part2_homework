from peewee import *
from datetime import date
# from tabulate import tabulate

db = SqliteDatabase('Briefcase.db')


class BaseModel(Model):
    class Meta:
        database = db


class Transaction(BaseModel):
    IdTransaction = AutoField(primary_key=True)
    IdPortfolio = IntegerField(null=False)
    Date = DateField(default=date.today, null=False)
    TransactionType = CharField(null=False)  # withdraw, deposit, buy or sell
    Amount = FloatField(null=False, default=0)
    Token = CharField(null=False)
    Price = FloatField(null=False, default=0)
    Total = FloatField()
    Balance = FloatField(null=False, default=0)
    IdParentTransaction = IntegerField(null=True)

    @classmethod
    def transaction_add(cls, id_portfolio: int, transaction_type: str, amount: float, token: str, price=0.0, parent_transaction=None) -> 'Transaction':
        if amount <= 0:
            raise Exception('You cant make transaction with negative or zero amount')
        if transaction_type.lower() not in ['deposit', 'withdraw', 'sell', 'buy']:
            raise Exception('bla bla')

        total = amount * price
        balance = cls.get_balance_by_token(id_portfolio, token)
        new_balance = balance + (
            amount if transaction_type in ['deposit', 'buy'] else -amount)
        if new_balance < 0:
            raise Exception('rtfgreg')

        return cls.create(
            IdPortfolio = id_portfolio,
            TransactionType=transaction_type,
            Amount=amount,
            Token=token.lower(),
            Price=price,
            Total=total,
            Balance=new_balance,
            IdParentTransaction=parent_transaction
        )

    @classmethod
    def get_balance_by_token(self,id_portfolio: int, token: str):
        # Get the latest transaction for the given token
        last_transaction = (Transaction
                            .select()
                            .where(Transaction.IdPortfolio == id_portfolio, Transaction.Token == token.lower())
                            .order_by(Transaction.IdTransaction.desc())
                            .first())

        if last_transaction:
            return last_transaction.Balance
        else:
            return 0
    @classmethod
    def get_last_transactions(self, id_portfolio: int ,limit: int) -> list:
        try:
            # Получаем последние транзакции, отсортированные по ID в убывающем порядке
            transactions = (Transaction
                            .select()
                            .where(Transaction.IdPortfolio == id_portfolio)
                            .order_by(Transaction.IdTransaction.desc())
                            .limit(limit))
            return transactions
            # Форматируем вывод
            # if transactions:
            #     print(f"Last {limit} transaction(s):")
            #     for transaction in transactions:
            #         print(f"ID: {transaction.IdTransaction}, "
            #               f"Date: {transaction.Date}, "
            #               f"Type: {transaction.TransactionType}, "
            #               f"Amount: {transaction.Amount}, "
            #               f"Token: {transaction.Token}, "
            #               f"Price: {transaction.Price}, "
            #               f"Balance: {transaction.Balance}")
            #     return transactions
        #     else:
        #         print("No transactions found.")
        #         return []
        except Exception as e:
            print(f"Error fetching transactions: {e}")
            return []







class Portfolio(BaseModel):
    IdPortfolio = AutoField(primary_key=True)
    Name = TextField(null=False, unique=True)
    BaseTicker = TextField(null=False)

    @classmethod
    def create_portfolio(cls, name: str, base_ticker: str):
        return cls.create(Name=name, BaseTicker=base_ticker)

    @classmethod
    def get_by_name(cls, name: str) -> 'Portfolio' or None:
        try:
            portfolio = cls.get(cls.Name == name)
            return portfolio
        except DoesNotExist:
            print(f"Portfolio with name '{name}' does not exist.")
            return None


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

with db:
    db.create_tables([Transaction, Portfolio])

id_portfolio = 2
# port = Portfolio.create_portfolio('mixer', 'usdt')
# tr = Transaction.transaction_add(id_portfolio, 'withdraw', 2000, 'USDT')
# tr = Transaction.transaction_add(id_portfolio, 'withdraw', 376576, 'bread', )

# tr2 = Transaction.transaction_add(2, 'deposit', 2000, 'USDT')
# print(Transaction.get_balance_by_token(2, 'usdt'))
#
# port = PortfolioBaseTicker('mixer', 'USDT')
port = Portfolio.get_by_name('mixer')
# print(port.Name)
# # port.show_token_balance('usdt')
# base_ticker_balance = port.get_base_ticker_balance()
# print(base_ticker_balance)
# new_base_ticker_balance = port.withdraw_base_ticker(300)
# print(f'deposited {new_base_ticker_balance}')
# port.deposit_base_ticker(100)
# port.show_token_balance('usdt')
# print(port.buy('bread', 5, 2.5))
print(port.sell('bread', 5, 2.5))

