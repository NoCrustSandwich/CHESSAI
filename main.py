# A.N.N.C.A = Artificial Neural Network Chess Agent

import chessAI
import chessController
import time
import math







currentBoard = [["r","n","b","q","k","b","n","r"],
               ["p","p","p","p","p","p","p","p"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["_","_","_","_","_","_","_","_"],
               ["P","P","P","P","P","P","P","P"],
               ["R","N","B","Q","K","B","N","R"]]



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


previousBoard = None
# Sets player color
playerColor = "b"

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
    
    best_source = int_to_position[math.ceil(source_predictions[0])]
    best_target = int_to_position[math.ceil(target_predictions[0])]


    # Moves pieces internally on the matrix
    previousBoard = chessController.movePieceInternally(best_source,best_target,currentBoard,playerColor)

  

    # Moves pieces using mouse
    chessController.movePieceExternally(best_source,best_target,playerColor)



