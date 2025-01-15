from config import db
from models.transaction import Transaction
from models.portfolio import Portfolio

from cli.app import AppCLI

def init_db():
    with db:
        db.create_tables([Transaction, Portfolio])


if __name__ == "__main__":
    init_db()

    cli = AppCLI()
    cli.run()