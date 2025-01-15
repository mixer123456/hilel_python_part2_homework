import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from peewee import *
from config import db

from cli.menu import MainMenu, PortfolioMenu
from models.portfolio import Portfolio
from models.transaction import Transaction

class PortfolioCLI:
    selected_portfolio = None

    def __init__(self):
        self.main_menu = MainMenu(self)
        self.portfolio_menu = PortfolioMenu(self)

    def display_menu(self):
        if self.selected_portfolio:
            self.portfolio_menu.display()
            choice = self.portfolio_menu.get_choice()
            self.portfolio_menu.handle_choice(choice)
        else:
            self.main_menu.display()
            choice = self.main_menu.get_choice()
            self.main_menu.handle_choice(choice)

    def create_portfolio(self):
        name = input("Enter portfolio name: ")
        base_ticker = input("Enter base ticker (e.g., 'USD', 'BTC'): ")
        try:
            portfolio = Portfolio.create(Name=name, BaseTicker=base_ticker)
            print(f"Portfolio '{portfolio.Name}' created successfully!")

        except Exception as e:
            print(f"Error creating portfolio: {e}")

    def show_portfolios(self):
        portfolios = Portfolio.get_list()
        print(portfolios)
        print("Portfolios:")
        for portfolio in portfolios:
            print(f"{portfolio.IdPortfolio} - {portfolio.Name} - {portfolio.BaseTicker}")
        id = input('Select portfolio by id or key "e" for exit: ')

        if id == 'e':
            print("Exiting... Show menu!")
            return
        
        self.select_portfolio(id)

    def select_portfolio(self, id: str):
        selected = self.find_portfolio(id)
        if selected:
            self.selected_portfolio = selected
            print(f"Selected portfolio: '{self.selected_portfolio.Name}'")
        else:
            print("Portfolio not found. Please try again.")

    def deselect_portfolio(self):
        self.selected_portfolio = None
        print("Portfolio deselected.")

    def find_portfolio(self, id: str):
        return Portfolio.get_by_id(id)
    
    def menu_exit(self):
        print("Exiting the program. Goodbye!")
        sys.exit()

    def view_balance(self):
        if self.selected_portfolio:
            balance = self.selected_portfolio.get_balance()
            print(f"Portfolio '{self.selected_portfolio.Name}' balance:")
            for item in balance:
                print(f"{item['token'].upper()} - {item['balance']}")
        else:
            print("No portfolio selected.")

    def add_transaction(self):
        transaction_type = input("Enter transaction type (deposit, withdraw, buy, sell): ")
        if transaction_type not in ['deposit', 'withdraw', 'buy', 'sell']:
            print("Invalid operation type. Please try again.")
            return

        token = input("Enter token: ")
        amount = float(input("Enter amount: "))

        if transaction_type in ['buy', 'sell']:
            price = float(input("Enter price (for buy/sell transactions): "))
        else:
            price = None

        if transaction_type == 'deposit':
            self.selected_portfolio.deposit(token, amount)
        elif transaction_type == 'withdraw':
            self.selected_portfolio.withdraw(token, amount)
        elif transaction_type == 'buy':
            self.selected_portfolio.buy(token, amount, price)
        elif transaction_type == 'sell':
            self.selected_portfolio.sell(token, amount, price)

    def show_transactions(self):
        if self.selected_portfolio:
            transactions = self.selected_portfolio.get_last_transactions(5)
            print(f"Last 5 transactions for portfolio '{self.selected_portfolio.Name}':")
            for transaction in transactions:
                comments = ''

                if transaction.IdParentTransaction:
                    parent = Transaction.get_by_id(transaction.IdParentTransaction)
                    comments = f" (Due to: {parent.TransactionType} {parent.Amount} {parent.Token.upper()})"

                print(f"ID: {transaction.IdTransaction}, "
                      f"Date: {transaction.Date}, "
                      f"Token: {transaction.Token.upper()}, "
                      f"Type: {transaction.TransactionType}, "
                      f"Amount: {transaction.Amount}, "
                      f"Price: {transaction.Price}, "
                      f"Balance: {transaction.Balance} "
                      f"{comments}")
        else:
            print("No portfolio selected.")  


    def run(self):
        while True:
            self.display_menu()

if __name__ == "__main__":
    cli = PortfolioCLI()
    cli.run()