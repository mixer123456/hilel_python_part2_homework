class NegativeBalanceError(Exception):
    '''Error if balance smaller than 0'''

    def __init__(self, username: str, balance: int):
        '''
        Methof initilization of error
        :param username: username
        :param balance: balance
        '''
        self.message = f'Money cant be negative. {username} current balance: {balance}.'

    def __str__(self):
        '''
        error message
        :return: message
        '''
        return self.message


class FalseValidAccountError(Exception):
    '''Error if account is not valid'''

    def __init__(self, username: str):
        '''
        Methof initilization of error
        :param username: username
        '''
        self.message = f'{username} account is currently invalid.'

    def __str__(self):
        '''
        error message
        :return: message
        '''
        return self.message


class NotEnoughMoneyError(Exception):
    '''Error if not enoug money for withdraw or make a transaction'''

    def __init__(self, username: str, balance: int, withdraw_or_transaction_money: int):
        '''
        Methof initilization of error
        :param username: username
        :param balance: balance
        :param withdraw_or_transaction_money: withdraw or transaction money
        '''
        self.message = f'{username} dont have enough money to withdraw or make a transaction. {username} current balance: {balance}. The money {username} wanted to withdraw or make a transaction: {withdraw_or_transaction_money}'

    def __str__(self):
        '''
        error message
        :return: message
        '''
        return self.message
