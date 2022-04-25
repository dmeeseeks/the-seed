import tensorflow as tf
from core.agent import Meeseeks
from core.task import Task
from impl.t1.algorithm import ClothingClassificationAlgorithm


class ClothingClassificationMeeseeks(Meeseeks):
    ''' A Mr. Meeseeks can classify clothing images. '''

    __task_id: str
    ''' The identity of the clothing classification task. '''

    def __init__(self, model: tf.keras.Model):
        super().__init__('ClothingClassificationMeeseeks')
        self.__task_id = 'ClothingClassificationTask'
        self.with_abilities([
            Task(self.__task_id).with_algorithm(
                ClothingClassificationAlgorithm(model)
            )
        ])

    def save(self, file_name: str):
        for ability in self.abilities:
            if ability.id == self.__task_id:
                model = ability.algorithm.model # tf.keras.Model
                model.save(filepath=file_name)
                break