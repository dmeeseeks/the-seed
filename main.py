from impl.t1.agent import ClothingClassificationMeeseeks
import tensorflow as tf


def main():
    dataset = tf.keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = dataset.load_data()
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dense(10))
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )
    agent = ClothingClassificationMeeseeks(model=model)
    agent.learn(
        task_id='ClothingClassificationTask',
        data={
            'x': train_images,
            'y': train_labels
        },
        config={
            'batch_size': None,
            'epochs': 10
        }
    )
    agent.perform(
        task_id='ClothingClassificationTask',
        data={
            'x': test_images,
            'y': test_labels
        },
        config={
            'batch_size': None
        }
    )
    agent.save(f'model/{agent.id}.h5')


if __name__ == '__main__':
    main()