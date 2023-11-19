# Library Imports
import keras
from keras.models import Model
from keras.layers import Input, Flatten, Dense


###############################################################################################################################################################
# Artificial Neural Network
###############################################################################################################################################################
class ANN:

    def __init__(self):
        self.model = self.loadANN("CANN")

    # Creates an instance of the neural network model
    def createChessModel(self):
        input_layer = Input(shape=(8, 8))
        x = Flatten()(input_layer)
        x = Dense(512, activation='relu')(x)
        x = Dense(256, activation='relu')(x)
        x = Dense(128, activation='relu')(x)
        x = Dense(64, activation='relu')(x)
        Q_values = Dense(226, name='q_values', activation='linear')(x)
        model = Model(inputs=input_layer, outputs=Q_values)
        model.compile(optimizer="adam", loss='mae', metrics=['accuracy'])

        return model

    # Loads ANN from a .JSON file
    def loadANN(self, filename):
        if filename.endswith('.json'):
            json_filename = filename
            h5_filename = filename[:-5] + '.h5'
        else:  # assume local filename root only
            json_filename = 'ANNCAModels/' + filename + '.json'
            h5_filename = 'ANNCAModels/' + filename + '.h5'
        json_filename = json_filename.replace('\\', '/')
        h5_filename = h5_filename.replace('\\', '/')

        with open(json_filename, 'r') as json_file:
            model_json = json_file.read()

        model = keras.models.model_from_json(model_json)
        model.load_weights(h5_filename)

        # Sets up ANN optimizers and loss on load
        model.compile(optimizer="adam", loss='mae', metrics=['accuracy'])

        return model

    # Saves ANN as .JSON file
    def saveANN(self, filename):
        filename = 'ANNCAModels/' + filename
        self.model.save_weights(filename + '.h5')
        model_json = self.model.to_json()
        with open(filename + '.json', 'w') as json_file:
            json_file.write(model_json)
        
        return True


###############################################################################################################################################################
