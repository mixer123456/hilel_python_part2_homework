from peewee import *
from datetime import date

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

    def add_transaction(transaction_type: str, amount: float, token: str, parent_transaction: int = None):
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

            # Insert the new transaction
            new_transaction = Transaction.create(
                TransactionType=transaction_type,
                Amount=amount,
                Tocken=token.lower(),
                Balance=new_balance,
                ParentTransaction=parent_transaction
            )
            print(f"Transaction added successfully: {new_transaction.IdTransaction}")
            return new_transaction
        except Exception as e:
            print(f"Error adding transaction: {e}")
            return None

    def show_balance_by_token(token_name: str):
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


with db:
    db.create_tables([Transaction])


# customer = {'TransactionType': 'deposit', 'Amount': 1, 'Token': 'bread'.lower(), 'Balance': 3}
# Transaction.add_transaction('deposit', 100, 'euro')
# Transaction.show_balance_by_token('euro')


class Portfolio:
    def __init__(self, name: str, money: int):
        self.name = name
        self.money = money

    def deposit(self, amount: float, token: str):
        if amount <= 0:
            raise Exception('You want to deposit nothing?')

        Transaction.add_transaction('deposit', amount, token)

    def withdraw(self, amount: float, token: str):
        if amount <= 0:
            raise Exception('You want to withdraw nothing?')

        Transaction.add_transaction('withdraw', amount, token)

    def buy(self, token: str, price: int, amount: float, parent_transaction: int):
        if amount <= 0:
            raise Exception('You want to buy nothing?')

        if price <= 0:
            raise Exception('Token cant be free or less than 0')

        if price >= self.money:
            raise Exception('You dont have enough money')

        Transaction.add_transaction('buy', amount, token, parent_transaction)
        self.money = - price

    def sell(self, token: str, price: int, amount: float, parent_transaction: int):
        if amount <= 0:
            raise Exception('You want to sell nothing?')

        if price <= 0:
            raise Exception('Token cant be free or less than 0')

        Transaction.add_transaction('sell', amount, token, parent_transaction)
        self.money += price
