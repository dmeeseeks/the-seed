class Algorithm:
    ''' Represents the algorithm of the learning process. '''

    name: str
    ''' The name of the algorithm. '''

    def __init__(self, name: str):
        self.name = name

    def with_name(self, name: str):
        ''' Modifies the name of the algorithm. '''
        self.name = name
        return self

    def fit(self, data: any, config: any = None) -> any:
        '''
        Starts the learning process.

        Paramaters:
            data: the learning data
            config: the learning configuration

        Returns:
            The result of learning process.
        '''
        pass

    def run(self, data: any, config: any = None) -> any:
        '''
        Performs the algorithm with specific data.

        Paramaters:
            data: the input data
            config: the configuration

        Returns:
            The result of process.
        '''
        pass

    @property
    def model(self) -> any:
        ''' Returns the model associated with the algorithm. '''
        pass