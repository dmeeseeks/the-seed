from typing import List
from core.task import Task


class Box:
    ''' A Mr. Meeseeks box, that can summon several Mr. Meeseeks with specific abilities. '''

    id: str
    ''' The identity of the box. '''

    created_at: any
    ''' The time when the box was created. '''

    abilities: List[Task]
    ''' All abilities that a Mr. Meeseeks summoned from the box haves. '''

    def __init__(self, id: str):
        self.id = id
        self.abilities = []

    def with_id(self, id: str):
        ''' Modifies the identity of the box. '''
        self.id = id
        return self

    def with_created_at(self, created_at: any):
        ''' Modifies the time the box was created. '''
        self.created_at = created_at
        return self

    def with_abilities(self, abilities: List[Task]):
        ''' Modifies the abilities that a Mr. Meeseeks summoned from the box haves. '''
        self.abilities = abilities
        return self

    def save(self, file_name: str):
        '''
        Save the box to a file.

        Parameters:
            file_name: the file name
        '''
        pass
