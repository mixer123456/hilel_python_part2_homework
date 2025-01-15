from peewee import *
import sys

import config
from cli_menu import MainMenu, PortfolioMenu

class Transaction():
    def __init__(self):
        pass

class Portfolio():
    def __init__(self):
        pass


db = SqliteDatabase(config.DB_NAME)

# def init_db():
#     with db:
#         db.create_tables([Transaction, Portfolio])

# init_db()

class PortfolioCLI:
    selected_portfolio = None

    def __init__(self):
        self.portfolios = [
            {
                'id': 1,
                'name': 'Portfolio 1',
                'base_ticker': 'USD'
            },
            {
                'id': 2,
                'name': 'Portfolio 2',
                'base_ticker': 'BTC'
            }
        ]

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
            # portfolio = Portfolio.create(Name=name, BaseTicker=base_ticker)

            ### ONLY FOR DEV TESTING
            self.portfolios.push({
                'id': len(self.portfolios) + 1,
                'name': name,
                'base_ticker': base_ticker
            })
            ###  / ONLY FOR DEV TESTING

            print(f"Portfolio '{name}' created successfully!")
        except Exception as e:
            print(f"Error creating portfolio: {e}")

    def show_portfolios(self):
        #portfolios = Portfolio.get_portfolios()
        portfolios = self.portfolios

        print("Portfolios:")
        for portfolio in portfolios:
            print(f"{portfolio['id']} - {portfolio['name']}")
        id = input('Select portfolio by id or key "e" for exit: ')

        if id == 'e':
            print("Exiting... Show menu!")
            return
        
        self.select_portfolio(id)

    def select_portfolio(self, id: str):
        selected = self.find_portfolio(id)
        if selected:
            self.selected_portfolio = selected
            print(f"Selected portfolio: '{self.selected_portfolio['name']}'")
        else:
            print("Portfolio not found. Please try again.")

    def deselect_portfolio(self):
        self.selected_portfolio = None
        print("Portfolio deselected.")

    def find_portfolio(self, id: str):
        #return Portfolio.get_by_id(id) PRODUCTION METHOD
        try:
            query_id = int(id)
            for portfolio in self.portfolios:
                if portfolio['id'] == query_id:
                    return portfolio
        except ValueError:
            print("Invalid ID. Please try again.")
        return None
    
    def menu_exit(self):
        print("Exiting the program. Goodbye!")
        sys.exit()

    # def view_balance(self):
    #     name = input("Enter portfolio name: ")
    #     if name in self.portfolios:
    #         token = input("Enter token to view balance: ")
    #         balance = self.portfolios[name].get_balance_by_token(token)
    #         print(f"Balance for {token} in portfolio '{name}': {balance}")
    #     else:
    #         print(f"Portfolio '{name}' does not exist.")

    # def add_transaction(self):
    #     name = input("Enter portfolio name: ")
    #     if name in self.portfolios:
    #         token = input("Enter token: ")
    #         transaction_type = input("Enter transaction type (deposit, withdraw, buy, sell): ")
    #         amount = float(input("Enter amount: "))
    #         price = float(input("Enter price (for buy/sell transactions): ")) if transaction_type in ['buy', 'sell'] else 0.0
    #         self.portfolios[name].add_transaction(token, transaction_type, amount, price)
    #     else:
    #         print(f"Portfolio '{name}' does not exist.")

    def run(self):
        while True:
            self.display_menu()

if __name__ == "__main__":
    cli = PortfolioCLI()
    cli.run()