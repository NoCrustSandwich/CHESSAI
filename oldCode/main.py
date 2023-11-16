# A.N.N.C.A = Artificial Neural Network Chess Agent

import chessAI
import chessController
import time
import math
import gym




currentBoard = [["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"]]



int_to_position ={
    0:  'A8',    1: 'B8', 2:    'C8', 3:  'D8', 4:  'E8', 5:  'F8', 6:  'G8', 7:  'H8',
    8:  'A7',    9: 'B7', 10:   'C7', 11: 'D7', 12: 'E7', 13: 'F7', 14: 'G7', 15: 'H7',
    16: 'A6',   17: 'B6', 18:   'C6', 19: 'D6', 20: 'E6', 21: 'F6', 22: 'G6', 23: 'H6',
    24: 'A5',   25: 'B5', 26:   'C5', 27: 'D5', 28: 'E5', 29: 'F5', 30: 'G5', 31: 'H5',
    32: 'A4',   33: 'B4', 34:   'C4', 35: 'D4', 36: 'E4', 37: 'F4', 38: 'G4', 39: 'H4',
    40: 'A3',   41: 'B3', 42:   'C3', 43: 'D3', 44: 'E3', 45: 'F3', 46: 'G3', 47: 'H3',
    48: 'A2',   49: 'B2', 50:   'C2', 51: 'D2', 52: 'E2', 53: 'F2', 54: 'G2', 55: 'H2',
    56: 'A1',   57: 'B1', 58:   'C1', 59: 'D1', 60: 'E1', 61: 'F1', 62: 'G1', 63: 'H1'
}

position_to_coordinates = {
    (0, 0): 'A8', (0, 1): 'B8', (0, 2): 'C8', (0, 3): 'D8', (0, 4): 'E8', (0, 5): 'F8', (0, 6): 'G8', (0, 7): 'H8',
    (1, 0): 'A7', (1, 1): 'B7', (1, 2): 'C7', (1, 3): 'D7', (1, 4): 'E7', (1, 5): 'F7', (1, 6): 'G7', (1, 7): 'H7',
    (2, 0): 'A6', (2, 1): 'B6', (2, 2): 'C6', (2, 3): 'D6', (2, 4): 'E6', (2, 5): 'F6', (2, 6): 'G6', (2, 7): 'H6',
    (3, 0): 'A5', (3, 1): 'B5', (3, 2): 'C5', (3, 3): 'D5', (3, 4): 'E5', (3, 5): 'F5', (3, 6): 'G5', (3, 7): 'H5',
    (4, 0): 'A4', (4, 1): 'B4', (4, 2): 'C4', (4, 3): 'D4', (4, 4): 'E4', (4, 5): 'F4', (4, 6): 'G4', (4, 7): 'H4',
    (5, 0): 'A3', (5, 1): 'B3', (5, 2): 'C3', (5, 3): 'D3', (5, 4): 'E3', (5, 5): 'F3', (5, 6): 'G3', (5, 7): 'H3',
    (6, 0): 'A2', (6, 1): 'B2', (6, 2): 'C2', (6, 3): 'D2', (6, 4): 'E2', (6, 5): 'F2', (6, 6): 'G2', (6, 7): 'H2',
    (7, 0): 'A1', (7, 1): 'B1', (7, 2): 'C1', (7, 3): 'D1', (7, 4): 'E1', (7, 5): 'F1', (7, 6): 'G1', (7, 7): 'H1'
}



previousBoard = None
# Sets player color
playerColor = "w"

if playerColor == "b":
    # Loads models
    ANNCA_Black = chessAI.load_ANN("ANNCA_Black")
else:
    ANNCA_White = chessAI.load_ANN("ANNCA_White")



while True:

    
    time.sleep(1)

    # Populates board based on discord game board
    currentBoard = chessController.populateBoard(currentBoard)

    print(currentBoard)

    if previousBoard == currentBoard:
        continue

    if playerColor == "b":
    # Loads models
        source_predictions, target_predictions = ANNCA_Black.predict(chessAI.preprocess_input([currentBoard]))
    else:
        source_predictions, target_predictions = ANNCA_White.predict(chessAI.preprocess_input([currentBoard]))
    


    print("Final Prediction: " + str(source_predictions) + ", " + str(target_predictions))

    best_source = position_to_coordinates[tuple([math.ceil(source_predictions[0][0]),math.ceil(source_predictions[0][1])])]
    best_target = position_to_coordinates[tuple([math.ceil(target_predictions[0][0]),math.ceil(target_predictions[0][1])])]


    print("Final Prediction: " + str(best_source) + ", " + str(best_target))


    

    # Moves pieces internally on the matrix
    previousBoard = chessController.movePieceInternally(best_source,best_target,currentBoard,playerColor)

  

    # Moves pieces using mouse
    chessController.movePieceExternally(best_source,best_target,playerColor)



