class Menu:
    def __init__(self, title: str, options: dict):
        """
        :param title: The title of the menu.
        :param options: A dictionary of options: {"key": "description"}.
                        Example: {"1": "Create Portfolio", "e": "Exit"}
        """
        self.title = title
        self.options = options

    def display(self):
        """Displays the menu on the screen."""
        print(f"\n{self.title}")
        for key, desc in self.options.items():
            print(f"{key}. {desc}")

    def get_choice(self):
        """Gets the user's choice."""
        return input("Enter your choice: ").strip()
    

class AppMenu(Menu):
    def __init__(self, cli):
        super().__init__(
            title="Portfolio Management CLI",
            options={
                "1": "Create Portfolio",
                "2": "Select Portfolio",
                "e": "Exit"
            }
        )
        self.cli = cli

    def handle_choice(self, choice):
        if choice == "1":
            self.cli.create_portfolio()
        elif choice == "2":
            self.cli.show_portfolios()
        elif choice == "e":
            self.cli.exit()
        else:
            print("Invalid choice. Please try again.")

class PortfolioMenu(Menu):
    def __init__(self, cli):
        super().__init__(
            title="Portfolio Menu",
            options={
                "1": "Show Balance",
                "2": "Show Transactions",
                "3": "Add Transaction",
                "b": "Back to Main Menu",
                "e": "Exit"
            }
        )
        self.cli = cli

    def handle_choice(self, choice):
        if choice == "1":
            self.cli.view_balance()
        elif choice == "2":
            self.cli.show_transactions()
        elif choice == "3":
            self.cli.add_transaction()
        elif choice == "b":
            self.cli.back_to_main_menu()
        elif choice == "e":
            self.cli.exit()
        else:
            print("Invalid choice. Please try again.")

