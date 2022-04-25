from core.agent import Meeseeks
from core.algorithm import Algorithm
from core.task import Task


agent = Meeseeks('A69').with_abilities([
    Task('T1').with_algorithm(Algorithm('U2-Net'))
])

try:
    agent.learn(task_id='T1', data=[])
    agent.save(file_name='A69.json')
except Exception as ex:
    print(ex)