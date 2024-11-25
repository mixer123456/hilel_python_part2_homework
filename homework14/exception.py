class TrainNumZeroError(Exception):
    '''Error class if train num smaller than 0'''
    def __init__(self):
        '''TrainNumZeroError initalization method'''
        self.message = 'Train num cant be smaller than 0'

    def __str__(self):
        '''
        string representation of the Error class
        :return: string representation of the Error class
        '''
        return self.message


class TrainPastTimeError(Exception):
    '''Error class if departure time in the past'''
    def __init__(self):
        '''TrainPastTimeError initalization method'''
        self.message = 'Departure time cant be in the past'

    def __str__(self):
        '''
        string representation of the Error class
        :return: string representation of the Error class
        '''
        return self.message