from core.box import Box
from core.error.task import UnableToDoTaskError
from core.task import Task


class Meeseeks(Box):
    ''' A Mr. Meeseeks. '''

    def __init__(self, id: str):
        super().with_id(id)

    def perform(self, task_id: str, data: any, config: any = None) -> any:
        '''
        Performs a specific task.

        Parameters:
            task_id: the identity of the task
            data: the data for the task
            config: the configuration for process (default: None)

        Returns:
            The result of the task.
        '''
        task: Task = None
        for ability in self.abilities:
            if ability.id == task_id:
                task = ability
                break
        if task == None:
            raise UnableToDoTaskError(task_id)
        return task.algorithm.run(data=data, config=config)

    def learn(self, task_id: str, data: any, config: any = None) -> any:
        '''
        Learns how to do a specific task.

        Parameters:
            task: the task
            data: the data for learning process
            config: the configuration for learning process (default: None)

        Returns:
            The result of the learning process.
        '''
        task: Task = None
        for ability in self.abilities:
            if ability.id == task_id:
                task = ability
                break
        if task == None:
            raise UnableToDoTaskError(task_id)
        return task.algorithm.fit(data=data, config=config)