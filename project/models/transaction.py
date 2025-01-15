from peewee import *
from datetime import date
from .base_model import BaseModel
 
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
            transactions = (Transaction
                            .select()
                            .where(Transaction.IdPortfolio == id_portfolio)
                            .order_by(Transaction.IdTransaction.desc())
                            .limit(limit))
            return transactions

        except Exception as e:
            print(f"Error fetching transactions: {e}")
            return []

    @classmethod
    def get_tokens_list(cls, id_portfolio: int) -> list:
        tokens = (Transaction
                  .select(Transaction.Token)
                  .where(Transaction.IdPortfolio == id_portfolio)
                  .distinct())
        return [token.Token for token in tokens]
