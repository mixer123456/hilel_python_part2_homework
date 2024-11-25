from exception import NegativeBalanceError, FalseValidAccountError, NotEnoughMoneyError


class Client:
    '''Client class bank'''
    def __init__(self, username: str, balance: int, valid_account: bool):
        '''method initilization clien class'''
        self.username = username
        self.balance = balance
        self.valid_account = valid_account

    @property
    def balance(self):
        '''
        getter method of balance
        :return: balance
        '''
        return self.__balance

    @balance.setter
    def balance(self, balance: int):
        '''
        seter method of balance
        :param balance: balance
        '''
        if balance < 0:
            raise NegativeBalanceError(self.username, balance)
        self.__balance = balance

    @property
    def valid_account(self):
        '''
        getter method of valid_account
        :return: valid_account
        '''
        return self.__valid_account

    @valid_account.setter
    def valid_account(self, valid_account: bool):
        '''
        seter method of valid_account
        :param valid_account: valid_account
        '''
        if valid_account == False:
            raise FalseValidAccountError(self.username)
        self.__valid_account = valid_account

    def withdraw_money_from_balance(self, withdraw_money: int):
        '''
        withdraw your money from balance
        :param withdraw_money: count of money
        :return: text that says about successful withdrawal of money
        '''
        if withdraw_money > self.__balance:
            raise NotEnoughMoneyError(self.username, self.__balance, withdraw_money)
        self.__balance -= withdraw_money
        return f'{self.username} succeful withdraw money. His balance: {self.__balance}'

    def transaction_money_to_other(self, transaction_money: int, other_client: 'Client'):
        '''
        transaction money from your balance to other balance
        :param transaction_money: count of money
        :param other_client: other client of bank
        :return: text that indicates a successful transfer of money to another account
        '''
        if self.__balance < transaction_money:
            raise NotEnoughMoneyError(self.username, self.__balance, transaction_money)
        self.__balance -= transaction_money
        other_client.__balance += transaction_money
        return f'User {self.username} make transactin to {other_client.username}. {self.username} current balance: {self.__balance}. {other_client.username} current balance: {other_client.__balance}'

    def add_money_to_balance(self, add_money: int):
        '''
        addd money  to your balance
        :param add_money: count of money
        :return: text that talks about adding money to your account
        '''
        if add_money <= 0:
            raise NegativeBalanceError(self.username, self.__balance)
        self.__balance += add_money
        return f'{self.username} add money to his balance. His current balance: {self.__balance}'

    def __str__(self):
        '''
        str methhod if client
        :return: data for client
        '''
        return f'''
Username: {self.username}
Balance: {self.__balance}
Valid account: {self.__valid_account}'''


Taras = Client('taraskiller228', 100, True)
Nikita = Client('nikitakiller228', 150, True)
Taras.withdraw_money_from_balance(10)
print(Taras.balance)
print(Taras.transaction_money_to_other(50, Nikita))
print(Taras.balance)
print(Nikita.balance)
print(Taras.add_money_to_balance(100))
print(Taras)
print(Nikita)
