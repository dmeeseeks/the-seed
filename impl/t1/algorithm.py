import tensorflow as tf
from core.algorithm import Algorithm


class ClothingClassificationAlgorithm(Algorithm):
    ''' A basic algorithm for classifying clothing images. '''

    __model: tf.keras.Model

    def __init__(self, model: tf.keras.Model):
        super().__init__('ClothingClassification')
        self.__model = model

    def fit(self, data: any, config: any = None) -> any:
        batch_size = None if config == None else config['batch_size']
        epochs = None if config == None else config['epochs']
        return self.__model.fit(
            x=data['x'],
            y=data['y'],
            batch_size=batch_size,
            epochs=epochs
        )

    def run(self, data: any, config: any = None) -> any:
        batch_size = None if config == None else config['batch_size']
        return self.__model.predict(
            x=data['x'],
            batch_size=batch_size
        )

    @property
    def model(self):
        return self.__model