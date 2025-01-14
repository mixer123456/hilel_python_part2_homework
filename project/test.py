from peewee import *
from datetime import date
# from tabulate import tabulate

db = SqliteDatabase('Briefcase.db')


class BaseModel(Model):
    class Meta:
        database = db


class Transaction(BaseModel):
    IdTransaction = AutoField(primary_key=True)
    Date = DateField(default=date.today, null=False)
    TransactionType = CharField(null=False)  # withdraw, deposit, buy or sell
    Amount = IntegerField(null=False, default=0)
    Token = CharField(null=False)
    Price = IntegerField(null=False, default=0)
    Total = IntegerField()
    Balance = IntegerField(null=False, default=0)
    IdParentTransaction = IntegerField(null=False)

    @classmethod
    def transaction_add(cls, transaction_type, amount, token, price=0.0, parent_transaction=None):
        total = amount * price
        last_transaction = (Transaction
                            .select()
                            .where(Transaction.Token == token.lower())
                            .order_by(Transaction.IdTransaction.desc())
                            .first())
        new_balance = (last_transaction.Balance if last_transaction else 0) + (
            amount if transaction_type in ['deposit', 'buy'] else -amount)

        return cls.create(
            TransactionType=transaction_type,
            Amount=amount,
            Token=token.lower(),
            Price=price,
            Total=total,
            Balance=new_balance,
            IdParentTransaction=parent_transaction
        )


class PortfolioBaseTicker(BaseModel):
    IdPortfolio = AutoField(primary_key=True)
    Name = TextField(null=False, unique=True)
    BaseTicker = TextField(null=False)

    @classmethod
    def create_portfolio(cls, name, base_ticker):
        return cls.create(Name=name, BaseTicker=base_ticker)

    def get_last_transactions(self, limit):
        try:
            # Получаем последние транзакции, отсортированные по ID в убывающем порядке
            transactions = (Transaction
                            .select()
                            .order_by(Transaction.IdTransaction.desc())
                            .limit(limit))

            # Форматируем вывод
            if transactions:
                print(f"Last {limit} transaction(s):")
                for transaction in transactions:
                    print(f"ID: {transaction.IdTransaction}, "
                          f"Date: {transaction.Date}, "
                          f"Type: {transaction.TransactionType}, "
                          f"Amount: {transaction.Amount}, "
                          f"Token: {transaction.Token}, "
                          f"Price: {transaction.Price}, "
                          f"Balance: {transaction.Balance}")
                return transactions
            else:
                print("No transactions found.")
                return []
        except Exception as e:
            print(f"Error fetching transactions: {e}")
            return []



    def show_balance_by_token(self, token: str):
        balance = self.get_balance_by_token(token)
        print(f"Balance for token '{token}': {balance}")

    def get_balance_by_token(self, token: str):
        # Get the latest transaction for the given token
        last_transaction = (Transaction
                            .select()
                            .where(Transaction.Token == token.lower())
                            .order_by(Transaction.IdTransaction.desc())
                            .first())

        if last_transaction:
            return last_transaction.Balance
        else:
            return 0

    def get_base_ticker_balance(self):
        last_transaction = (Transaction
                            .select()
                            .where(Transaction.Token == self.__base_ticker)
                            .order_by(Transaction.IdTransaction.desc())
                            .first())

        return last_transaction.Balance

    # def deposit_base_ticker(self, amount: float):
    #     if amount <= 0:
    #         raise Exception('Are you want to deposit nothing?')
    #
    #     query = PortfolioBaseTicker.select(PortfolioBaseTicker.BaseTicker).where(PortfolioBaseTicker.Name == self.name)
    #     self.add_transaction(query, 'deposit', amount)

    def deposit_base_ticker(self, amount: float):

        if amount <= 0:
            raise Exception('Are you want to deposit nothing?')

        self.add_transaction(self.__base_ticker, 'deposit', amount)


    def withdraw_base_ticker(self, amount: float):
        if amount <= 0:
            raise Exception('Are you want to withdraw nothing?')
        self.add_transaction(self.__base_ticker, 'withdraw', amount)


    def delete_transaction_by_id(self, transaction_id: int):
        Transaction.delete_by_id(transaction_id)


    def delete_multiple_transactions(self, criteria):
        try:
            query = Transaction.delete().where(criteria)
            rows_deleted = query.execute()
            print(f"Deleted {rows_deleted} transaction(s) successfully.")
            return rows_deleted
        except Exception as e:
            print(f"Error deleting transactions: {e}")
            return None


    def deposit(self, token: str, amount: float):
        if amount <= 0:
            raise Exception('You want to deposit nothing?')

        self.add_transaction(token, 'deposit', amount)


    def withdraw(self, token: str, amount: float):
        token_balance = self.get_balance_by_token(token)

        if amount <= 0:
            raise Exception('You want to withdraw nothing?')

        if token_balance <= amount:
            raise Exception('You dont have enough this token(s) to withdraw')

        Transaction.transaction_add('withdraw', amount, token)


    def buy(self, token: str, price: float, amount: float, parent_transaction: int = None):
        total = amount * price
        base_ticker_balance = self.get_base_ticker_balance()

        if amount <= 0:
            raise Exception('You want to buy nothing?')

        if price <= 0:
            raise Exception('Token cant be free or less than 0')

        if base_ticker_balance < total:
            raise Exception('You dont have enough your base token(s)')

        Transaction.transaction_add('buy', amount, token, price)
        self.withdraw_base_ticker(total)


    def sell(self, token: str, price: float, amount: float, parent_transaction: int = None):
        token_balance = self.get_balance_by_token(token)

        if amount <= 0:
            raise Exception('You want to sell nothing?')

        if price <= 0:
            raise Exception('Token cant be free or less than 0')

        if token_balance <= amount:
            raise Exception('You dont have this token(s) to sell')

        total = int(amount * price)
        Transaction.transaction_add(token, 'sell', amount, price, parent_transaction)
        self.deposit_base_ticker(total)


with db:
    db.create_tables([Transaction, PortfolioBaseTicker])

port = PortfolioBaseTicker('mixer', 'USDT')

