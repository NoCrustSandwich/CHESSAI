import os
import keras
from keras.models import Model
from keras.layers import Input, Flatten, Dense


###############################################################################################################################################################
# Artificial Neural Network - Version 4.1 (18/12/2023)
###############################################################################################################################################################

class neuralNetwork:
    """
    NeuralNetwork represents a neural network model for a chess AI using Keras.

    Attributes:
        - model (keras.models.Model): The neural network model.

    Methods:
        - __init__(self): Initializes an instance of the NeuralNetwork class, , and loads ANNCA's neural network.
        - create_new_model(self, model_name: str): Creates a new instance of the neural network model and saves it.
        - load_model(self, filename: str) -> keras.models.Model: Loads the neural network model from a JSON file.
        - save_model(self, model_name: str): Saves the neural network model as a JSON file.
        - delete_model(self, model_name: str): Deletes the neural network model JSON file.

    Usage Example:
        - chessANN = neuralNetwork()
        - chessANN.create_new_model("ANNCA")
        or
        - chessANN.load_model("ANNCA")
    """

    def __init__(self):
        """
        Initializes an instance of the NeuralNetwork class, and loads ANNCA's neural network.
        """

        self.model = self.load_model("ANNCA")

        
    def create_new_model(self, model_name: str):
        """
        Creates a new instance of the neural network model and saves it.

        Args:
            - model_name (str): The name to assign to the new model.

        Usage:
            - chessANN.create_new_model("new_model_name")
        """
        input_layer = Input(shape=(8, 8))

        x = Flatten()(input_layer)
        x = Dense(10256, activation='relu')(x)
        x = Dense(5128, activation='relu')(x)
        x = Dense(2564, activation='relu')(x)

        q_values = Dense(1282, name='q_values', activation='linear')(x)
        self.model = Model(inputs=input_layer, outputs=q_values)
        self.model.compile(optimizer="adam", loss='mse', metrics=['accuracy'])

        self.save_model(model_name)
        print(f"Model '{model_name}' JSON file created.")



    def load_model(self, filename: str):
        """
        Loads the neural network model from a JSON file.

        Args:
            - filename (str): The filename (with or without extension) or path of the model to be loaded.

        Returns:
            - keras.models.Model: The loaded neural network model.

        Raises:
            - FileNotFoundError: If the specified model file is not found.

        Usage:
            - loaded_model = chessANN.load_model("pretrained_model")
        """

        if filename.endswith('.json'):
            json_filename = filename
            h5_filename = filename[:-5] + '.h5'
        else:
            json_filename = 'models/' + filename + '.json'
            h5_filename = 'models/' + filename + '.h5'
        json_filename = json_filename.replace('\\', '/')
        h5_filename = h5_filename.replace('\\', '/')

        with open(json_filename, 'r') as json_file:
            model_json = json_file.read()

        model = keras.models.model_from_json(model_json)
        model.load_weights(h5_filename)

        model.compile(optimizer="adam", loss='mse', metrics=['accuracy'])   # Sets up ANN optimizers and loss on load

        return model


    def save_model(self, model_name: str):
        """
        Saves the neural network model as a JSON file.

        Args:
            - model_name (str): The name to assign to the saved model.

        Usage:
            - chessANN.save_model("saved_model_name")
        """
        filename = 'models/' + model_name

        self.model.save_weights(filename + '.h5')
        model_json = self.model.to_json()
        with open(filename + '.json', 'w') as json_file:
            json_file.write(model_json)


    def delete_model(self, model_name: str):
        """
        delets the neural network model JSON file.

        Args:
            - model_name (str): The name to assigned to the saved model.

        Usage:
            - chessANN.delete_model("saved_model_name")
        """
        filename = 'models/' + model_name

        json_filepath = filename + '.json'
        if os.path.exists(json_filepath):   # Checks if the model JSON file exists before attempting to delete
            os.remove(json_filepath)
            print(f"Model '{model_name}' JSON file deleted.")
        else:
            print(f"Model '{model_name}' JSON file not found.")

###############################################################################################################################################################