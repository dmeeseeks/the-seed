from core.algorithm import Algorithm


class Task:
    ''' Represents the ability of a model with specific task. '''

    id: str
    ''' The identity of the ability. '''

    created_at: any
    ''' The time when the ability was created. '''

    algorithm: Algorithm
    ''' The algorithm that the ability follows. '''

    weights: list
    ''' The weights of the model in learning process. '''

    def __init__(self, id: str):
        self.id = id
        self.weights = []

    def with_id(self, id: str):
        ''' Modifies the identity of the ability. '''
        self.id = id
        return self

    def with_created_at(self, created_at: any):
        ''' Modifies the time the ability was created. '''
        self.created_at = created_at
        return self

    def with_algorithm(self, algorithm: Algorithm):
        ''' Modifies the algorithm the ability follows. '''
        self.algorithm = algorithm
        return self

    def with_weights(self, weights: list):
        ''' Modifies the weights of the model in learning process. '''
        self.weights = weights
        return self