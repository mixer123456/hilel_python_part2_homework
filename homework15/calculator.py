from math import factorial
import csv

from exeption import DegreeRoot


class Calculator:
    '''Calculator'''

    def __init__(self, file_name):
        '''calculator initialization method'''
        self.file_name = file_name
        self.action_history = []

    def get_action_history(self) -> list:
        '''
        get actions dict
        :return: actions history(saved) dict
        '''
        return self.action_history

    def add_action_to_history(self, action: str, result):
        self.action_history.append({
            'action': action,
            'result': result
        })

    def save_result(self):
        '''
        save results in file
        '''
        with open(self.file_name, mode='w', encoding='UTF-8') as file:
            csv.DictWriter(file, fieldnames=['action', 'result']).writeheader()
            csv.DictWriter(file, fieldnames=['action', 'result']).writerows(
                [{'action': item['action'], 'result': item['result']} for item in self.action_history])

    def read_results(self):
        '''
        read data csv
        :return: read data from csv file
        '''
        rs = []
        with open(self.file_name, mode='r', encoding='utf-8') as file:
            dict_data = csv.DictReader(file)

            for row in dict_data:
                rs.append(row)
        return rs

    def action_sum(self, first_num: int, second_num: int):
        '''
        sum first num and second num
        :param first_num: first num
        :param second_num: second num
        '''
        result = first_num + second_num
        action = f'{first_num}+{second_num}'
        self.add_action_to_history(action, result)

    def action_minus(self, first_num: int, second_num: int):
        '''
        subtracts numbers
        :param first_num:first num
        :param second_num:second num
        '''
        result = first_num - second_num
        action = f'{first_num}-{second_num}'
        self.add_action_to_history(action, result)

    def action_multiplication(self, first_num: int, second_num: int):
        '''
        multiplicat numbers
        :param first_num:first num
        :param second_num:second num
        '''
        result = first_num * second_num
        action = f'{first_num}*{second_num}'
        self.add_action_to_history(action, result)

    def action_division(self, first_num: int, second_num: int):
        '''
        division numbers
        :param first_num:first num
        :param second_num:second num
        '''
        if second_num == 0:
            raise ZeroDivisionError('cant be divided by 0')
        result = round(first_num / second_num, 2)
        action = f'{first_num}/{second_num}'
        self.add_action_to_history(action, result)

    def action_degree(self, first_num: int, second_num: int):
        '''
        degree number
        :param first_num:number raised to a degree
        :param second_num:degree
        '''
        result = first_num ** second_num
        action = f'{first_num}^{second_num}'
        self.add_action_to_history(action, result)

    def action_root(self, first_num: int, second_num: int):
        '''
        root number
        :param first_num:the number we take the root of
        :param second_num:degree of the root
        '''
        if first_num < 0 and second_num % 2 == 0:
            raise DegreeRoot('It is impossible to extract an even root from a negative number')
        if second_num == 0:
            raise DegreeRoot('The degree of a root cannot be equal to zero')

        result = round(first_num ** (1 / second_num))
        action = f'{second_num}√{first_num}'
        self.add_action_to_history(action, result)

    def action_factorial(self, num: int):
        '''
        factorial num
        :param num: the number over which we do the factorial
        '''
        result = factorial(num)
        action = f'{num}!'
        self.add_action_to_history(action, result)

    def get_sum_first_five_results(self):
        results = calculator.read_results()
        list_num = [int(el['result']) for el in results[:5]]
        return sum(list_num[:5])


calculator = Calculator('results')
calculator.action_sum(5, 5)
calculator.action_sum(5, 4)

calculator.action_minus(6, 5)
calculator.action_minus(6, 4)

calculator.action_multiplication(5, 5)
calculator.action_multiplication(5, 4)

calculator.action_division(6, 4)
calculator.action_division(6, 2)

calculator.action_degree(100, -10)
calculator.action_degree(5, 0)

calculator.action_root(6, 5)
calculator.action_root(6, 1)

calculator.action_factorial(5)
calculator.action_factorial(4)
print(calculator.get_action_history())

calculator.action_minus(4,5)
calculator.action_minus(4,5)
calculator.action_sum(4,5)
calculator.action_sum(3,4)
calculator.action_sum(2,3)
calculator.action_sum(1,2)
calculator.action_sum(0,1)
calculator.action_minus(4,5)
print(calculator.action_history)

calculator.save_result()
print(calculator.get_sum_first_five_results())