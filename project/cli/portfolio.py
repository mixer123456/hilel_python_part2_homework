import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cli.menu import PortfolioMenu
from models.portfolio import Portfolio
from models.transaction import Transaction

from colorama import init, Fore
from tabulate import tabulate

class PortfolioCLI:
    portfolio = None

    def __init__(self, portfolio=Portfolio, app_cli=None):
        self.menu = PortfolioMenu(self)
        self.portfolio = portfolio
        self.app_cli = app_cli

    def display_menu(self):
        self.menu.display()
        choice = self.menu.get_choice()
        self.menu.handle_choice(choice)

    def print_balance(self, data ):
        headers = [
            "Token",
            "Amount",
            "Price (USD)", 
            "Invested",
            f"Total ({self.portfolio.BaseTicker})",
            "Avg Price",
            "Profit",
            "ROI"
            ]
        headers = [Fore.YELLOW + header + Fore.RESET for header in headers]
        
        colored_data = [
            (
             Fore.CYAN + row['token'], 
             Fore.MAGENTA + str(row['amount']),
             Fore.GREEN + str(row['current_price']),
             Fore.CYAN + str(row['invested']),
             Fore.CYAN + str(row['current_balance']),
             (Fore.GREEN if row['avg_price'] >= row['current_price'] else Fore.RED) + str(row['avg_price']),
            (Fore.GREEN if row['profit'] >= 0 else Fore.RED) + str(row['profit']),
            (Fore.GREEN if row['roi'] >= 0 else Fore.RED) + str(row['roi'])+ Fore.RESET
             )
            for row in data
        ]
        
        print(tabulate(colored_data, headers, tablefmt="grid"))
        
    def view_balance(self):    
        balance = self.portfolio.get_balance()
        self.print_balance(balance)

        


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
            self.portfolio.deposit(token, amount)
        elif transaction_type == 'withdraw':
            self.portfolio.withdraw(token, amount)
        elif transaction_type == 'buy':
            self.portfolio.buy(token, amount, price)
        elif transaction_type == 'sell':
            self.portfolio.sell(token, amount, price)

    def show_transactions(self):
        transactions = self.portfolio.get_last_transactions(5)
        print(f"Last 5 transactions for portfolio '{self.portfolio.Name}':")
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

    def back_to_main_menu(self):
        self.app_cli.deselect_portfolio()

    def exit(self):
        self.app_cli.exit()