import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cli.menu import AppMenu
from models.portfolio import Portfolio
from .portfolio import PortfolioCLI

class AppCLI:
    portfolio_cli = None

    def __init__(self):
        self.menu = AppMenu(self)

    def display_menu(self):
        if self.portfolio_cli:
            self.portfolio_cli.display_menu()
        else:
            self.menu.display()
            choice = self.menu.get_choice()
            self.menu.handle_choice(choice)

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
            self.portfolio_cli = PortfolioCLI(selected, self)
            print(f"Selected portfolio: '{selected.Name}'")
        else:
            print("Portfolio not found. Please try again.")

    def deselect_portfolio(self):
        self.portfolio_cli = None
        print("Portfolio deselected.")

    def find_portfolio(self, id: str):
        return Portfolio.get_by_id(id)
    
    def exit(self):
        print("Exiting the program. Goodbye!")
        sys.exit()


    def run(self):
        while True:
            self.display_menu()