from math import factorial
import csv


class Calculator:
    '''Calculator'''

    def __init__(self):
        '''calculator initialization method'''
        self.action_dict = {}

    def get_action_dict(self) -> dict:
        '''
        get actions dict
        :return: actions history(saved) dict
        '''
        return self.action_dict

    def save_result(self, file_name):
        '''
        save results in file
        :param file_name: file name
        '''
        with open(file_name, mode='w', encoding='UTF-8') as file:
            csv.DictWriter(file, fieldnames=['action', 'result']).writeheader()
            csv.DictWriter(file, fieldnames=['action', 'result']).writerows(
                [{'action': action, 'result': result} for action, result in self.action_dict.items()])

    def read_results(self, file_name):
        '''
        read data csv
        :return: read data from csv file
        '''
        rs = []
        with open(file_name, mode='r', encoding='utf-8') as file:
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
        sum = first_num + second_num
        sum_dict = {f'{first_num}+{second_num}': sum}
        self.action_dict.update(sum_dict)

    def action_minus(self, first_num: int, second_num: int):
        '''
        subtracts numbers
        :param first_num:first num
        :param second_num:second num
        '''
        minus = first_num - second_num
        minus_dict = {f'{first_num}-{second_num}': minus}
        self.action_dict.update(minus_dict)

    def action_multiplication(self, first_num: int, second_num: int):
        '''
        multiplicat numbers
        :param first_num:first num
        :param second_num:second num
        '''
        multiplication = first_num * second_num
        multiplication_dict = {f'{first_num}*{second_num}': multiplication}
        self.action_dict.update(multiplication_dict)

    def action_division(self, first_num: int, second_num: int):
        '''
        division numbers
        :param first_num:first num
        :param second_num:second num
        '''
        division = round(first_num / second_num, 2)
        division_dict = {f'{first_num}/{second_num}': division}
        self.action_dict.update(division_dict)

    def action_degree(self, first_num: int, second_num: int):
        '''
        degree number
        :param first_num:number raised to a degree
        :param second_num:degree
        '''
        degree = first_num ** second_num
        degree_dict = {f'{first_num}^{second_num}': degree}
        self.action_dict.update(degree_dict)

    def action_root(self, first_num: int, second_num: int):
        '''
        root number
        :param first_num:the number we take the root of
        :param second_num:degree of the root
        '''
        if first_num < 0 and second_num % 2 == 0:
            raise ValueError("It is impossible to extract an even root from a negative number")
        if second_num == 0:
            raise ValueError("The degree of a root cannot be equal to zero")

        root = round(first_num ** (1 / second_num))
        root_dict = {f'{second_num}√{first_num}': root}
        self.action_dict.update(root_dict)

    def action_factorial(self, num: int):
        '''
        factorial num
        :param num: the number over which we do the factorial
        '''
        factorial_num = factorial(num)
        factorial_dict = {f'{num}!': factorial_num}
        self.action_dict.update(factorial_dict)

    def sum_five_results(self):
        results = calculator.read_results('results')
        list_num = [int(el['result']) for el in results[:5]]
        return sum(list_num[:5])


calculator = Calculator()
# print(calculator.get_action_dict())
# calculator.sum_numbers(5, 5)
# print(calculator.get_action_dict())
# calculator.sum_numbers(5, 4)
# print(calculator.get_action_dict())
#
# calculator.minus_numbers(6, 5)
# print(calculator.get_action_dict())
# calculator.minus_numbers(6, 4)
# print(calculator.get_action_dict())
#
# calculator.multiplication_numbers(5, 5)
# print(calculator.get_action_dict())
# calculator.multiplication_numbers(5, 4)
# print(calculator.get_action_dict())
#
# calculator.division_numbers(6, 4)
# print(calculator.get_action_dict())
# calculator.division_numbers(6, 2)
# print(calculator.get_action_dict())
#
# calculator.degree_number(100, -10)
# print(calculator.get_action_dict())
# calculator.degree_number(5, 0)
# print(calculator.get_action_dict())
#
# calculator.root_number(6, 5)
# print(calculator.get_action_dict())
# calculator.root_number(6, 1)
# print(calculator.get_action_dict())
#
# calculator.factorial_number(5)
# print(calculator.get_action_dict())
# calculator.factorial_number(4)
# print(calculator.get_action_dict())
print(calculator.sum_five_results())
print(calculator.save_result('results'))
