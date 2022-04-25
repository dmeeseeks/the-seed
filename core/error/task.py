class UnableToDoTaskError(Exception):
    '''
    An exeption thrown when a Mr. Meeseeks cannot do a specific task.
    '''

    def __init__(self, task_id: str):
        super().__init__(f'Unable to do task {task_id}')