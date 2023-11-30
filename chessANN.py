import os
import keras
from keras.models import Model
from keras.layers import Input, Flatten, Dense


###############################################################################################################################################################
# Artificial Neural Network - Version 3.1 (24/11/2023)
###############################################################################################################################################################

class neuralNetwork:
    """
    NeuralNetwork represents a neural network model for a chess AI using Keras.

    Attributes:
        - model (keras.models.Model): The neural network model.

    Methods:
        - __init__(self, model_name: str): Initializes an instance of the NeuralNetwork class, and checks if the model folder and default model exists on device and if not creates them.
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

    def __init__(self, model_directory='Documents/ANNCA/ANNCA_Model', default_model = "ANNCA"):
        """
        Initializes an instance of the NeuralNetwork class, and checks if the model folder and default model exists on device and if not creates them.
        """
        home_directory = os.path.expanduser("~")
        self.model_directory = os.path.join(home_directory, model_directory)

        if not os.path.exists(self.model_directory):
            os.makedirs(self.model_directory)

        filename = os.path.join(self.model_directory, default_model)
        json_filepath = filename + '.json'
        if os.path.exists(json_filepath):   # Checks if the default ANNCA model JSON file exist and creates it if it doesn't
            print(f"Model " + default_model + " JSON Already Exists.")
        else:
            self.create_new_model(default_model)
            print(f"Model " + default_model + " JSON Created.")
        
        self.model = self.load_model(default_model)

        
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
        x = Dense(20512, activation='relu')(x)
        x = Dense(10256, activation='relu')(x)
        x = Dense(5128, activation='relu')(x)
        x = Dense(2564, activation='relu')(x)
        x = Dense(1282, activation='relu')(x)

        q_values = Dense(1282, name='q_values', activation='linear')(x)
        self.model = Model(inputs=input_layer, outputs=q_values)
        self.model.compile(optimizer="adam", loss='mae', metrics=['accuracy'])

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

        model_path = os.path.join(self.model_directory, filename)
        json_filename = model_path if filename.endswith('.json') else model_path + '.json'
        h5_filename = model_path if filename.endswith('.h5') else model_path + '.h5'

        json_filename = os.path.expanduser(json_filename)  # Expanding ~ to user's home directory
        h5_filename = os.path.expanduser(h5_filename)

        if not os.path.exists(json_filename) or not os.path.exists(h5_filename):
            raise FileNotFoundError(f"Model files not found for {filename}")

        with open(json_filename, 'r') as json_file:
            model_json = json_file.read()

        model = keras.models.model_from_json(model_json)
        model.load_weights(h5_filename)

        model.compile(optimizer="adam", loss='mae', metrics=['accuracy'])   # Sets up ANN optimizers and loss on load

        return model


    def save_model(self, model_name: str):
        """
        Saves the neural network model as a JSON file.

        Args:
            - model_name (str): The name to assign to the saved model.

        Usage:
            - chessANN.save_model("saved_model_name")
        """
        filename = os.path.join(self.model_directory, model_name)
        
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
        home_directory = os.path.expanduser("~")
        full_model_directory = os.path.join(home_directory, self.model_directory)
        filename = os.path.join(full_model_directory, model_name)

        json_filepath = filename + '.json'
        if os.path.exists(json_filepath):   # Checks if the model JSON file exists before attempting to delete
            os.remove(json_filepath)
            print(f"Model '{model_name}' JSON file deleted.")
        else:
            print(f"Model '{model_name}' JSON file not found.")

###############################################################################################################################################################