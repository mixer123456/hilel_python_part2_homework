from datetime import datetime

from exception import TrainNumZeroError, TrainPastTimeError


class TrainCollection:
    '''Class where trains remain'''

    def __init__(self, *trains: 'Train'):
        '''
        TrainCollection initialization method
        :param trains: list of trains
        '''
        self.train_list = list(trains)

    def sort_by_destination(self):
        '''
        sort list by ddestination but if several trains arrive at the same place, they are sorted by departure time
        :return: sorted list
        '''
        self.train_list.sort(key=lambda x: f'{x.destination} {x.departure_time}')
        return self.train_list


class Train:
    '''Train class'''
    def __init__(self, destination: str, train_num: int, departure_time: datetime):
        '''
        Train initialization method
        :param destination: train destination
        :param train_num: train num
        :param departure_time: train departure time
        '''
        self.destination = destination
        self.train_num = train_num
        self.departure_time = departure_time

    @property
    def destination(self):
        '''
        Getter method of ddestination
        :return: destination
        '''
        return self.__destination

    @destination.setter
    def destination(self, destination):
        '''
        Setter method of destination
        :param destination: train ddestination
        '''
        self.__destination = destination

    @property
    def train_num(self):
        '''
        Getter method of train num
        :return: train num
        '''
        return self.__train_num

    @train_num.setter
    def train_num(self, train_num):
        '''
        Setter method of train num
        :param train_num: train num
        '''
        if train_num < 0:
            raise TrainNumZeroError()
        self.__train_num = train_num

    @property
    def departure_time(self):
        '''
        Getter method of ddeparture time
        :return: departure time
        '''
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, time: datetime):
        '''
        Setter method of departure time
        :param time: departure time
        '''
        if time < datetime.now():
            raise TrainPastTimeError()
        self.__departure_time = time

    def __str__(self):
        '''
        string representation of the Train class
        :return: string representation of the Train class
        '''
        return f'''
        Destination: {self.destination}
        Train number: {self.train_num}
        Departure time: {self.departure_time}\n'''

    __repr__ = __str__
