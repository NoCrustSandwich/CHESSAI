#ANNCA - Artificial Neural Network Chess Algorithmn

import math

import keras
from keras.models import Model
from keras.layers import Input, Conv2D, Flatten, Dense

from keras.optimizers import Adam, SGD, RMSprop, Adagrad, Adadelta, Nadam

import numpy as np


import chess
import chess.pgn




# Unused Translation dictionaries
position_to_coordinates = {
    'a8': [0, 0], 'b8': [0, 1], 'c8': [0, 2], 'd8': [0, 3],'e8': [0, 4], 'f8': [0, 5], 'g8': [0, 6], 'h8': [0, 7],
    'a7': [1, 0], 'b7': [1, 1], 'c7': [1, 2], 'd7': [1, 3],'e7': [1, 4], 'f7': [1, 5], 'g7': [1, 6], 'h7': [1, 7],
    'a6': [2, 0], 'b6': [2, 1], 'c6': [2, 2], 'd6': [2, 3],'e6': [2, 4], 'f6': [2, 5], 'g6': [2, 6], 'h6': [2, 7],
    'a5': [3, 0], 'b5': [3, 1], 'c5': [3, 2], 'd5': [3, 3],'e5': [3, 4], 'f5': [3, 5], 'g5': [3, 6], 'h5': [3, 7],
    'a4': [4, 0], 'b4': [4, 1], 'c4': [4, 2], 'd4': [4, 3],'e4': [4, 4], 'f4': [4, 5], 'g4': [4, 6], 'h4': [4, 7],
    'a3': [5, 0], 'b3': [5, 1], 'c3': [5, 2], 'd3': [5, 3],'e3': [5, 4], 'f3': [5, 5], 'g3': [5, 6], 'h3': [5, 7],
    'a2': [6, 0], 'b2': [6, 1], 'c2': [6, 2], 'd2': [6, 3],'e2': [6, 4], 'f2': [6, 5], 'g2': [6, 6], 'h2': [6, 7],
    'a1': [7, 0], 'b1': [7, 1], 'c1': [7, 2], 'd1': [7, 3],'e1': [7, 4], 'f1': [7, 5], 'g1': [7, 6], 'h1': [7, 7],
    }



int_to_coordinates = {
    0:[0, 0],   1:[0, 1],  2:[0, 2],  3:[0, 3],  4:[0, 4],  5:[0, 5],  6:[0, 6],  7:[0, 7],
    8:[1, 0],   9:[1, 1], 10:[1, 2], 11:[1, 3], 12:[1, 4], 13:[1, 5], 14:[1, 6], 15:[1, 7],
    16:[2, 0], 17:[2, 1], 18:[2, 2], 19:[2, 3], 20:[2, 4], 21:[2, 5], 22:[2, 6], 23:[2, 7],
    24:[3, 0], 25:[3, 1], 26:[3, 2], 27:[3, 3], 28:[3, 4], 29:[3, 5], 30:[3, 6], 31:[3, 7],
    32:[4, 0], 33:[4, 1], 34:[4, 2], 35:[4, 3], 36:[4, 4], 37:[4, 5], 38:[4, 6], 39:[4, 7],
    40:[5, 0], 41:[5, 1], 42:[5, 2], 43:[5, 3], 44:[5, 4], 45:[5, 5], 46:[5, 6], 47:[5, 7],
    48:[6, 0], 49:[6, 1], 50:[6, 2], 51:[6, 3], 52:[6, 4], 53:[6, 5], 54:[6, 6], 55:[6, 7],
    56:[7, 0], 57:[7, 1], 58:[7, 2], 59:[7, 3], 60:[7, 4], 61:[7, 5], 62:[7, 6], 63:[7, 7],
    }

int_to_piece = {
        0:'_',
        1:'p', 2:'r', 3:'n', 4:'b', 5:'q', 6:'k',
        7:'P', 8:'R', 9:'N', 10:'B', 11:'Q', 12:'K'
    }


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Data Processsing Functions
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Loads ANN from a .JSON file
def load_ANN(filename):


    if filename.endswith('.json'):
        json_filename = filename
        h5_filename = filename[:-5] + '.h5'
    else: # assume local filename root only
        json_filename = 'ANNCAModels/' + filename + '.json'
        h5_filename = 'ANNCAModels/' + filename + '.h5'
    json_filename.replace('\\', '/')
    h5_filename.replace('\\', '/')


    with open(json_filename, 'r') as json_file:
        model_json = json_file.read()
        json_file.close()

    model = keras.models.model_from_json(model_json)
    model.load_weights(h5_filename)
    setup_ANN(model)

    return model

# Saves ANN as .JSON file
def save_ANN(model, filename):

    filename = 'ANNCAModels/' + filename
    model.save_weights(filename + '.h5')
    model_json = model.to_json()
    with open(filename + '.json', 'w') as json_file:
        json_file.write(model_json)

# Converts Board to custom format for ANN
def convert_board_to_custom_format(board):
    custom_board = []

    for rank in range(8):
        custom_rank = []
        for file in range(8):
            piece = board.piece_at(chess.square(file, 7 - rank))
            if piece is None:
                custom_rank.append("_")
            else:
                custom_rank.append(piece.symbol())
        custom_board.append(custom_rank)

    return custom_board


# Converts PGN file to a board input 2D list
def pgn_to_board(pgn_file):
    board = chess.Board()
    whiteTurn = True
    whiteSourceMoves =[]
    whiteTargetMoves =[]
    whiteBoards =[]

    blackSourceMoves =[]
    blackTargetMoves =[]
    blackBoards =[]


    # Open the PGN file for reading
    with open(pgn_file, 'r') as pgn:
        game = chess.pgn.read_game(pgn)
        
        # Extract the winner from the game's result
        result = game.headers.get('Result')
        if result == '1-0':
            winner = 'W'
        elif result == '0-1':
            winner = 'B'
        elif result == '1/2-1/2':
            winner = 'D'

        if game:
            board = game.board()
            for move in game.mainline_moves():
                
                if(whiteTurn):
                
                    whiteSourceMoves.append(str(move)[0:2])
                    whiteTargetMoves.append(str(move)[2:4])
                    whiteBoards.append(convert_board_to_custom_format(board))

                    whiteTurn = False
                else:

                    blackSourceMoves.append(str(move)[0:2])
                    blackTargetMoves.append(str(move)[2:4])
                    blackBoards.append(convert_board_to_custom_format(board))

                    whiteTurn = True

    
    # Translates board and moves into integer and index notations for ANN training and attaches input board along with it
    finWhiteBoards = preprocess_input(whiteBoards)
    finBlackBoards = preprocess_input(blackBoards)

    

    # Preprocess outputs to be fed into the ANN
    finBlackSourceMoves = preprocess_output(blackSourceMoves)
    finBlackTargetMoves = preprocess_output(blackTargetMoves)
    finWhiteSourceMoves = preprocess_output(whiteSourceMoves)
    finWhiteTargetMoves = preprocess_output(whiteTargetMoves)
    

    # Input Data must be in numpy array format
    finWhiteBoards = np.array(finWhiteBoards)
    finBlackBoards = np.array(finBlackBoards)
    
    finBlackSourceMoves = (np.array(finBlackSourceMoves))
    finBlackTargetMoves = (np.array(finBlackTargetMoves))
    finWhiteSourceMoves = (np.array(finWhiteSourceMoves))
    finWhiteTargetMoves = (np.array(finWhiteTargetMoves))
    

    return winner, finWhiteBoards,finBlackBoards,finWhiteSourceMoves,finWhiteTargetMoves,finBlackSourceMoves, finBlackTargetMoves
    


# Translates board from chars to integer representations (Changes board to numerical values)
def preprocess_input(boards):
    piece_to_int = {
        '_': 0,
        'p': 1, 'r': 2, 'n': 3, 'b': 4, 'q': 5, 'k': 6,
        'P': 7, 'R': 8, 'N': 9, 'B': 10, 'Q': 11, 'K': 12
    }

    input_boards = []

    for board in boards:
        
        input_board = [["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"]]

        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if piece in piece_to_int:
                    input_board[row][col] = piece_to_int[piece]

        input_boards.append(input_board)

    return input_boards

# Translates the inputted moves from algebraic coordinate notation to index notation
def preprocess_output(moves):


    position_to_Int= {
    'a8': 0, 'b8': 1, 'c8': 2, 'd8': 3,'e8': 4, 'f8': 5, 'g8': 6, 'h8': 7,
    'a7': 8, 'b7': 9, 'c7': 10, 'd7': 11,'e7': 12, 'f7': 13, 'g7': 14, 'h7': 15,
    'a6': 16, 'b6': 17, 'c6': 18, 'd6': 19,'e6': 20, 'f6': 21, 'g6': 22, 'h6': 23,
    'a5': 24, 'b5': 25, 'c5': 26, 'd5': 27,'e5': 28, 'f5': 29, 'g5': 30, 'h5': 31,
    'a4': 32, 'b4': 33, 'c4': 34, 'd4': 35,'e4': 36, 'f4': 37, 'g4': 38, 'h4': 39,
    'a3': 40, 'b3': 41, 'c3': 42, 'd3': 43,'e3': 44, 'f3': 45, 'g3': 46, 'h3': 47,
    'a2': 48, 'b2': 49, 'c2': 50, 'd2': 51,'e2': 52, 'f2': 53, 'g2': 54, 'h2': 55,
    'a1': 56, 'b1': 57, 'c1': 58, 'd1': 59,'e1': 60, 'f1': 61, 'g1': 62, 'h1': 63
    }

    position_to_coordinates = {
    'a8': [0, 0], 'b8': [0, 1], 'c8': [0, 2], 'd8': [0, 3],'e8': [0, 4], 'f8': [0, 5], 'g8': [0, 6], 'h8': [0, 7],
    'a7': [1, 0], 'b7': [1, 1], 'c7': [1, 2], 'd7': [1, 3],'e7': [1, 4], 'f7': [1, 5], 'g7': [1, 6], 'h7': [1, 7],
    'a6': [2, 0], 'b6': [2, 1], 'c6': [2, 2], 'd6': [2, 3],'e6': [2, 4], 'f6': [2, 5], 'g6': [2, 6], 'h6': [2, 7],
    'a5': [3, 0], 'b5': [3, 1], 'c5': [3, 2], 'd5': [3, 3],'e5': [3, 4], 'f5': [3, 5], 'g5': [3, 6], 'h5': [3, 7],
    'a4': [4, 0], 'b4': [4, 1], 'c4': [4, 2], 'd4': [4, 3],'e4': [4, 4], 'f4': [4, 5], 'g4': [4, 6], 'h4': [4, 7],
    'a3': [5, 0], 'b3': [5, 1], 'c3': [5, 2], 'd3': [5, 3],'e3': [5, 4], 'f3': [5, 5], 'g3': [5, 6], 'h3': [5, 7],
    'a2': [6, 0], 'b2': [6, 1], 'c2': [6, 2], 'd2': [6, 3],'e2': [6, 4], 'f2': [6, 5], 'g2': [6, 6], 'h2': [6, 7],
    'a1': [7, 0], 'b1': [7, 1], 'c1': [7, 2], 'd1': [7, 3],'e1': [7, 4], 'f1': [7, 5], 'g1': [7, 6], 'h1': [7, 7],
    }


    translatedMoves = []

    for move in moves:
        translatedMoves.append(position_to_coordinates[move])

    return translatedMoves




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chess move Validation functions
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Checks if move is valid for a white pawn
def IsValidMoveWhitePawn(source, target):

    if( source[1]==target[1] and source[0]-1==target[0]):
        return True
    
    elif (source[1]==target[1] and source[0]==6 and target[0]==4):
        return True
    else:
        return False
    

# Checks if move is valid for a Rook
def IsValidMoveRook(source, target):

    if(source[0] == target[0]):
        return True
    elif(source[1] == target[1]):
        return True
    else:
        return False
    

# Checks if move is valid for a King
def IsValidMoveKing(source, target):

    if(target[0] == source[0]+1 and target[1] == source[1]+1):
        return True
    elif(target[0] == source[0]+1 and target[1] == source[1]):
        return True
    elif(target[0] == source[0] and target[1] == source[1]+1):
        return True
    elif(target[0] == source[0]-1 and target[1] == source[1]-1):
        return True
    elif(target[0] == source[0]-1 and target[1] == source[1]):
        return True
    elif(target[0] == source[0] and target[1] == source[1]-1):
        return True
    elif(target[0] == source[0]-1 and target[1] == source[1]+1):
        return True
    elif(target[0] == source[0]+1 and target[1] == source[1]-1):
        return True
    else:
        return False


# Checks if move is valid for a Knight
def IsValidMoveKnight(source, target):

    if(target[0] == source[0]+1 and target[1] == source[1]+2):
        return True
    elif(target[0] == source[0]+2 and target[1] == source[1]+1):
        return True
    elif(target[0] == source[0]-1 and target[1] == source[1]+2):
        return True
    elif(target[0] == source[0]-2 and target[1] == source[1]+1):
        return True
    elif(target[0] == source[0]+1 and target[1] == source[1]-2):
        return True
    elif(target[0] == source[0]+2 and target[1] == source[1]-1):
        return True
    elif(target[0] == source[0]-1 and target[1] == source[1]-2):
        return True
    elif(target[0] == source[0]-2 and target[1] == source[1]-1):
        return True
    else:
        return False


# Checks if move is valid for a Queen
def IsValidMoveQueen(source, target):

    if(IsValidMoveRook(source, target)):
        return True
    elif(IsValidMoveBishop(source, target)):
        return True
    else:
        return False


# Checks if move is valid for a Bishop
def IsValidMoveBishop(source, target):

    validMoves = []

    x = source[0]
    y = source[1]

    while x < 8 and y < 8:
        x+=1
        y+=1
        validMoves.append([x,y])
    

    x = source[0]
    y = source[1]

    while x < 8 and y > -1:
        x+=1
        y-=1
        validMoves.append([x,y])
    
    x = source[0]
    y = source[1]

    while x > -1 and y > -1:
        x-=1
        y-=1
        validMoves.append([x,y])

    x = source[0]
    y = source[1]

    while x > -1 and y < 8:
        x-=1
        y+=1
        validMoves.append([x,y])
    

    if target in validMoves: 
        return True
    else: 
        return False
    

# Checks if move is valid for a black pawn
def IsValidMoveBlackPawn(source, target):

    if( source[1]==target[1] and source[0]+1==target[0]):
        return True
    
    elif (source[1]==target[1] and source[0]==1 and target[0]==3):
        return True
    else:
        return False



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Keras ANN Implemenation
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Create the neural network model
def create_chess_model():

    input_layer = Input(shape=(8, 8, 1))

    # Convolutional layers for feature extraction
    x = Conv2D(32, (3, 3), activation='relu')(input_layer)
    x = Conv2D(64, (3, 3), activation='relu')(x)

    # Flatten the feature maps
    x = Flatten()(x)

    # Fully connected layers for regression
    #x = Dense(8096, activation='relu')(x)
    #x = Dense(4048, activation='relu')(x)
    #x = Dense(1024, activation='relu')(x)
    x = Dense(512, activation='relu')(x)
    x = Dense(256, activation='relu')(x)
    x = Dense(128, activation='relu')(x)
    x = Dense(64, activation='relu')(x)
    

    # Output layers for source and target squares
    source_square = Dense(2, name='source_square', activation='linear')(x)
    target_square = Dense(2, name='target_square', activation='linear')(x)

    # Create the model
    model = Model(inputs=input_layer, outputs=[source_square, target_square])

   

    # Compile the model
    model.compile(optimizer="adam", loss='mean_absolute_error', metrics=['accuracy'])

    return model


# Sets up ANN
def setup_ANN(model):

    

    
    model.compile(optimizer="adam", loss='mean_absolute_error', metrics=['accuracy'])


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Loss Functions
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Training functions
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def trainANN():

    # Input pgn file with training data
    winner, finWhiteBoards,finBlackBoards,finWhiteSourceMoves,finWhiteTargetMoves,finBlackSourceMoves, finBlackTargetMoves = pgn_to_board('Training_Data/lichess_db_standard_rated_2014-07.pgn')

    # Creates models
    ANNCA_Black = create_chess_model()
    ANNCA_White = create_chess_model()

    # Loads models
    #ANNCA_Black = load_ANN("ANNCA_Black")
    #ANNCA_White = load_ANN("ANNCA_White")


    ANNCA_White.fit(finWhiteBoards, [finWhiteSourceMoves, finWhiteTargetMoves], batch_size=100, epochs=1000)
    ANNCA_Black.fit(finBlackBoards, [finBlackSourceMoves, finBlackTargetMoves], batch_size=100, epochs=1000)

    save_ANN(ANNCA_Black, 'ANNCA_Black')
    save_ANN(ANNCA_White, 'ANNCA_White')

    source_predictions, target_predictions = ANNCA_White.predict(preprocess_input([
        [["r","n","b","q","k","b","n","r"],
                ["p","p","p","p","p","p","p","p"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["P","P","P","P","P","P","P","P"],
                ["R","N","B","Q","K","B","N","R"]]
        ]))


    
    best_source = [math.ceil(source_predictions[0][0]),math.ceil(source_predictions[0][1])]
    best_target = [math.ceil(target_predictions[0][0]),math.ceil(target_predictions[0][1])]

    print("Final Prediction: " + str(best_source) + ", " + str(best_target))




#trainANN()