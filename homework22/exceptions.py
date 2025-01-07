class  NotFullOrFullColorListError(Exception):
    '''not full or full color list error'''
    def __init__(self):
        '''intilazation method of error'''
        self.message = 'Color must be a list of three integers in range 0-255.'

    def __str__(self) -> str:
        '''error str method'''
        return self.message

class NegativeVolumeError(Exception):
    '''Negative volume error'''
    def __init__(self):
        '''intilazation method of error'''
        self.message = 'Volume must be a non-negative integer.'

    def __str__(self) -> str:
        '''error str method'''
        return self.message