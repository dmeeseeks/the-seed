from core.algorithm import Algorithm


class Task:
    ''' Represents the ability of a model with specific task. '''

    id: str
    ''' The identity of the ability. '''

    created_at: any
    ''' The time when the ability was created. '''

    algorithm: Algorithm
    ''' The algorithm that the ability follows. '''

    weight: list
    ''' The weight of the model in learning process. '''

    def __init__(self, id: str):
        self.id = id
        self.weight = []

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

    def with_weight(self, weight: list):
        ''' Modifies the weight of the model in learning process. '''
        self.weight = weight
        return self