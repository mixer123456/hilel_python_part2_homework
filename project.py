from peewee import *
from datetime import date
from tabulate import tabulate

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
    Balance = IntegerField(null=False, default=0)
    IdParentTransaction = IntegerField()





with db:
    db.create_tables([Transaction])


# customer = {'TransactionType': 'deposit', 'Amount': 1, 'Token': 'bread'.lower(), 'Balance': 3}
# Transaction.add_transaction('deposit', 100, 'euro')
# Transaction.show_balance_by_token('euro')


class Portfolio:
    def __init__(self, name: str, money: int):
        self.name = name
        self.money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        if money <= 0:
            raise Exception('You dont have money?')
        self.__money = money


    def add_money(self, amount: int):
        if amount <= 0:
            raise Exception('You cant add nothing')

        self.__money += amount

    def show_last_transaction(self):
        try:
            last_transaction = Transaction.select().order_by(Transaction.IdTransaction.desc()).first()
            if last_transaction:
                transaction_data = [
                    ["ID", last_transaction.IdTransaction],
                    ["Date", last_transaction.Date],
                    ["Type", last_transaction.TransactionType],
                    ["Amount", last_transaction.Amount],
                    ["Token", last_transaction.Token],
                    ["Price", last_transaction.Price],
                    ["Balance", last_transaction.Balance],
                    ["Parent ID", last_transaction.IdParentTransaction]
                ]
                print(tabulate(transaction_data, headers=["Field", "Value"], tablefmt="pretty"))
                return last_transaction
            else:
                print("No transactions found.")
                return None
        except Exception as e:
            print(f"Error fetching the last transaction: {e}")
            return None

    def add_transaction(self, transaction_type: str, amount: float, token: str, price: float = 0.0,parent_transaction: int = None):
        try:
            # Get the latest balance for the token, if it exists
            last_transaction = (Transaction
                                .select()
                                .where(Transaction.Token == token.lower())
                                .order_by(Transaction.IdTransaction.desc())
                                .first())

            # Calculate new balance
            new_balance = (last_transaction.Balance if last_transaction else 0) + (
                amount if transaction_type in ['deposit', 'buy'] else -amount)

            new_price = amount * price

            # Insert the new transaction
            new_transaction = Transaction.create(
                TransactionType=transaction_type,
                Amount=amount,
                Token=token.lower(),
                Balance=new_balance,
                Price=new_price,
                IdParentTransaction=parent_transaction
            )
            print(f"Transaction added successfully: {new_transaction.IdTransaction}")
            return new_transaction
        except Exception as e:
            print(f"Error adding transaction: {e}")
            return None

    def show_balance_by_token(self, token_name: str):
        try:
            # Get the latest transaction for the given token
            last_transaction = (Transaction
                                .select()
                                .where(Transaction.Token == token_name.lower())
                                .order_by(Transaction.IdTransaction.desc())
                                .first())

            if last_transaction:
                # Display and return the balance
                print(f"Balance for token '{token_name}': {last_transaction.Balance}")
                return last_transaction.Balance
            else:
                print(f"Token '{token_name}' not found in the database.")
                return None
        except Exception as e:
            print(f"Error fetching balance: {e}")
            return None

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

    def deposit(self, amount: float, token: str):
        if amount <= 0:
            raise Exception('You want to deposit nothing?')

        self.add_transaction('deposit', amount, token)

    def withdraw(self, amount: float, token: str):
        if amount <= 0:
            raise Exception('You want to withdraw nothing?')

        self.add_transaction('withdraw', amount, token)

    def buy(self, token: str, price: int, amount: float, parent_transaction: int = None):
        if amount <= 0:
            raise Exception('You want to buy nothing?')

        if price <= 0:
            raise Exception('Token cant be free or less than 0')

        if price >= self.money:
            raise Exception('You dont have enough money')

        new_price = amount * price
        self.add_transaction('buy', amount, token, new_price, parent_transaction)
        self.__money -= new_price

    def sell(self, token: str, price: int, amount: float, parent_transaction: int = None):
        if amount <= 0:
            raise Exception('You want to sell nothing?')

        if price <= 0:
            raise Exception('Token cant be free or less than 0')

        new_price = int(amount * price)
        self.add_transaction('sell', amount, token, new_price)
        self.__money += new_price

port = Portfolio('mixer', 100)
