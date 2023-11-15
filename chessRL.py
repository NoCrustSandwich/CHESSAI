import gym
from gym import spaces
import chess
import chess.svg
from PIL import Image
import numpy as np
import math
import chessAI

import keras
from keras.models import Model
from keras.layers import Input, Flatten, Dense

import numpy as np

import chess
import chess.pgn





# Class for the chess board enviorment for the RL
class ChessEnv(gym.Env):
    def __init__(self):


        # Scroing will be rounded up in the end

        # Player / Opponent board weightings
        # _ = 0, 
        # p1 = 1,   |     op1 = -1, 
        # p2 = 2,   |     op2 = -2, 
        # p3 = 3,   |     op3 = -3, 
        # p4 = 4,   |     op4 = -4, 
        # p5 = 5,   |     op5 = -5, 
        # p6 = 6,   |     op6 = -6, 
        # p7 = 7,   |     op7 = -7, 
        # p8 = 8,   |     op8 = -8,
        # n1 = 9,   |     on1 = -9,
        # n2 = 10,  |     on2 = -10,
        # b1 = 11,  |     ob1 = -11,
        # b2 = 12,  |     ob2 = -12,
        # r1 = 13,  |     or1 = -13,
        # r2 = 14,  |     or2 = -14,
        # q = 15,   |     oq = -15,
        # k = 16,   |     ok = -16,


        # Dictionary to translate board ints to string representations
        int_to_piece ={
            0:"_", 
            1:"p1", 2:"p2", 3:"p3", 4:"p4", 5:"p5", 6:"p6", 7:"p7", 8:"p8",
            -1:"op1", -2:"op2", -3:"op3", -4:"op4", -5:"op5", -6:"op6", -7:"op7", -8:"op8",
            9:"n1", 10:"n2",
            -9:"on1", -10:"on2",
            11:"b1", 12:"b2",
            -11:"ob1", -12:"ob2",
            13:"r1", 14:"r2",
            -13:"or1", -14:"or2",
            15:"q",
            -15:"oq",  
            16:"k",
            -16:"ok",

        }

        #added
        # Dictionary to translate board string to integer representations
        piece_to_int = {
        "_": 0,
        "p1": 1, "p2": 2, "p3": 3, "p4": 4, "p5": 5, "p6": 6, "p7": 7, "p8": 8,
        "op1": -1, "op2": -2, "op3": -3, "op4": -4, "op5": -5, "op6": -6, "op7": -7, "op8": -8,
        "n1": 9, "n2": 10,
        "on1": -9, "on2": -10,
        "b1": 11, "b2": 12,
        "ob1": -11, "ob2": -12,
        "r1": 13, "r2": 14,
        "or1": -13, "or2": -14,
        "q": 15,
        "oq": -15,
        "k": 16,
        "ok": -16,
        }



        super(ChessEnv, self).__init__()

        self.board = [  [-13,-9,-11,-15,-16,-12,-10,-14],
                        [-1,-2,-3,-4,-5,-6,-7,-8],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [1,2,3,4,5,6,7,8],
                        [13,9,11,15,16,12,10,14] ]
        
        # o = opponent, ie. or1 = opponent rook 1
        self.board = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q","k","b2","n2","r2"]]
        
        # Tuple of 226 possible actions to be taken: ("piece", (Horizontal index change, Vertical index change))
        self.action_space    =   [   

                ("p1", (0, 1)),
                ("p1", (-1, 1)),
                ("p1", (1, 1)),
                ("p1", (0, 2)),

                ("p2", (0, 1)),
                ("p2", (-1, 1)),
                ("p2", (1, 1)),
                ("p2", (0, 2)),

                ("p3", (0, 1)),
                ("p3", (-1, 1)),
                ("p3", (1, 1)),
                ("p3", (0, 2)),

                ("p4", (0, 1)),
                ("p4", (-1, 1)),
                ("p4", (1, 1)),
                ("p4", (0, 2)),


                ("p5", (0, 1)),
                ("p5", (-1, 1)),
                ("p5", (1, 1)),
                ("p5", (0, 2)),

                ("p6", (0, 1)),
                ("p6", (-1, 1)),
                ("p6", (1, 1)),
                ("p6", (0, 2)),

                ("p7", (0, 1)),
                ("p7", (-1, 1)),
                ("p7", (1, 1)),
                ("p7", (0, 2)),

                ("p8", (0, 1)),
                ("p8", (-1, 1)),
                ("p8", (1, 1)),
                ("p8", (0, 2)),
                

                ("k", (0, 1)),
                ("k", (-1, 1)),
                ("k", (1, 1)),
                ("k", (-1, 0)),
                ("k", (-2, 0)),
                ("k", (1, 0)),
                ("k", (2, 0)),
                ("k", (0, -1)),
                ("k", (-1, -1)),
                ("k", (1, -1)),
                

                ("b1", (1, 1)),
                ("b1", (2, 2)),
                ("b1", (3, 3)),
                ("b1", (4, 4)),
                ("b1", (5, 5)),
                ("b1", (6, 6)),
                ("b1", (7, 7)),
                ("b1", (-1, -1)),
                ("b1", (-2, -2)),
                ("b1", (-3, -3)),
                ("b1", (-4, -4)),
                ("b1", (-5, -5)),
                ("b1", (-6, -6)),
                ("b1", (-7, -7)),
                ("b1", (-1, 1)),
                ("b1", (-2, 2)),
                ("b1", (-3, 3)),
                ("b1", (-4, 4)),
                ("b1", (-5, 5)),
                ("b1", (-6, 6)),
                ("b1", (-7, 7)),
                ("b1", (1, -1)),
                ("b1", (2, -2)),
                ("b1", (3, -3)),
                ("b1", (4, -4)),
                ("b1", (5, -5)),
                ("b1", (6, -6)),
                ("b1", (7, -7)),

                
                ("b2", (1, 1)),
                ("b2", (2, 2)),
                ("b2", (3, 3)),
                ("b2", (4, 4)),
                ("b2", (5, 5)),
                ("b2", (6, 6)),
                ("b2", (7, 7)),
                ("b2", (-1, -1)),
                ("b2", (-2, -2)),
                ("b2", (-3, -3)),
                ("b2", (-4, -4)),
                ("b2", (-5, -5)),
                ("b2", (-6, -6)),
                ("b2", (-7, -7)),
                ("b2", (-1, 1)),
                ("b2", (-2, 2)),
                ("b2", (-3, 3)),
                ("b2", (-4, 4)),
                ("b2", (-5, 5)),
                ("b2", (-6, 6)),
                ("b2", (-7, 7)),
                ("b2", (1, -1)),
                ("b2", (2, -2)),
                ("b2", (3, -3)),
                ("b2", (4, -4)),
                ("b2", (5, -5)),
                ("b2", (6, -6)),
                ("b2", (7, -7)),


                ("r1", (0, 1)),
                ("r1", (0, 2)),
                ("r1", (0, 3)),
                ("r1", (0, 4)),
                ("r1", (0, 5)),
                ("r1", (0, 6)),
                ("r1", (0, 7)),
                ("r1", (0, -1)),
                ("r1", (0, -2)),
                ("r1", (0, -3)),
                ("r1", (0, -4)),
                ("r1", (0, -5)),
                ("r1", (0, -6)),
                ("r1", (0, -7)),
                ("r1", (1, 0)),
                ("r1", (2, 0)),
                ("r1", (3, 0)),
                ("r1", (4, 0)),
                ("r1", (5, 0)),
                ("r1", (6, 0)),
                ("r1", (7, 0)),
                ("r1", (-1, 0)),
                ("r1", (-2, 0)),
                ("r1", (-3, 0)),
                ("r1", (-4, 0)),
                ("r1", (-5, 0)),
                ("r1", (-6, 0)),
                ("r1", (-7, 0)),


                ("r2", (0, 1)),
                ("r2", (0, 2)),
                ("r2", (0, 3)),
                ("r2", (0, 4)),
                ("r2", (0, 5)),
                ("r2", (0, 6)),
                ("r2", (0, 7)),
                ("r2", (0, -1)),
                ("r2", (0, -2)),
                ("r2", (0, -3)),
                ("r2", (0, -4)),
                ("r2", (0, -5)),
                ("r2", (0, -6)),
                ("r2", (0, -7)),
                ("r2", (1, 0)),
                ("r2", (2, 0)),
                ("r2", (3, 0)),
                ("r2", (4, 0)),
                ("r2", (5, 0)),
                ("r2", (6, 0)),
                ("r2", (7, 0)),
                ("r2", (-1, 0)),
                ("r2", (-2, 0)),
                ("r2", (-3, 0)),
                ("r2", (-4, 0)),
                ("r2", (-5, 0)),
                ("r2", (-6, 0)),
                ("r2", (-7, 0)),

                

                ("n1", (1, -2)),
                ("n1", (2, -1)),
                ("n1", (1, 2)),
                ("n1", (2, 1)),
                ("n1", (-1, -2)),
                ("n1", (-2, -1)),
                ("n1", (-1, 2)),
                ("n1", (-2, 1)),



                ("n2", (1, -2)),
                ("n2", (2, -1)),
                ("n2", (1, 2)),
                ("n2", (2, 1)),
                ("n2", (-1, -2)),
                ("n2", (-2, -1)),
                ("n2", (-1, 2)),
                ("n2", (-2, 1)),

                
                
                ("q", (1, 1)),
                ("q", (2, 2)),
                ("q", (3, 3)),
                ("q", (4, 4)),
                ("q", (5, 5)),
                ("q", (6, 6)),
                ("q", (7, 7)),
                ("q", (-1, -1)),
                ("q", (-2, -2)),
                ("q", (-3, -3)),
                ("q", (-4, -4)),
                ("q", (-5, -5)),
                ("q", (-6, -6)),
                ("q", (-7, -7)),
                ("q", (-1, 1)),
                ("q", (-2, 2)),
                ("q", (-3, 3)),
                ("q", (-4, 4)),
                ("q", (-5, 5)),
                ("q", (-6, 6)),
                ("q", (-7, 7)),
                ("q", (1, -1)),
                ("q", (2, -2)),
                ("q", (3, -3)),
                ("q", (4, -4)),
                ("q", (5, -5)),
                ("q", (6, -6)),
                ("q", (7, -7)),
                ("q", (0, 1)),
                ("q", (0, 2)),
                ("q", (0, 3)),
                ("q", (0, 4)),
                ("q", (0, 5)),
                ("q", (0, 6)),
                ("q", (0, 7)),
                ("q", (0, -1)),
                ("q", (0, -2)),
                ("q", (0, -3)),
                ("q", (0, -4)),
                ("q", (0, -5)),
                ("q", (0, -6)),
                ("q", (0, -7)),
                ("q", (1, 0)),
                ("q", (2, 0)),
                ("q", (3, 0)),
                ("q", (4, 0)),
                ("q", (5, 0)),
                ("q", (6, 0)),
                ("q", (7, 0)),
                ("q", (-1, 0)),
                ("q", (-2, 0)),
                ("q", (-3, 0)),
                ("q", (-4, 0)),
                ("q", (-5, 0)),
                ("q", (-6, 0)),
                ("q", (-7, 0)),
        ]

        self.observation_space = spaces.Box(low=-6, high=6, shape=(8, 8), dtype=int)
        self.modelWhite = chessAI.load_ANN("ANNCA_White")
        self.modelBlack = chessAI.load_ANN("ANNCA_Black")


    def change_Player(board):
        
        return [row[::-1] for row in reversed(board)]

    # Resets back to starting position
    def reset(self):
        # Reset the board to its initial state
        self.board = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q","k","b2","n2","r2"]]
        return np.array(self.board)


    # Returns the indexes of a piece on the board
    def find_piece_indexes(self, board, piece):
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == piece:
                    return i, j
        return None



    def step(self, action):
        
        # Flags that determine rewards
        piecePresent = False            # reward = -1000
        pieceTaken = False              # (value based on piece Taken)
        opponentKingInCheck = False     # reward = 10
        opponentKingInCheckmate = False # reward = 1000
        playerKingInCheck = False       # reward = -1000
        moveOutOfRange = False

        # Determines the indexed location of the piece taking the action
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == action[0]:
                    sourceLocation = [x, y]
                    targetLocation =  [x+action[1][0],y+action[1][0]]
                    piecePresent = True


        # Checks if the piece being moved is present on the board
        if not piecePresent:

            observation = np.array(self.board)
            reward = -1000.0
            done = False
            info = {"Piece is not present on the board"}
            return observation, reward, done, info

        # Checks if the move is out of range
        if targetLocation[0]>7 or targetLocation[1]>7 or targetLocation[0]<0 or targetLocation[1]<0:

            observation = np.array(self.board)
            reward = -1000.0
            done = False
            info = {"Target Location is out of range"}
            return observation, reward, done, info


        # Retrieves item present at the target tile
        targetTilePiece = self.board[targetLocation[0]][targetLocation[1]] 

        # If valid move and target tile is empty
        if targetTilePiece == "_":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            observation = np.array(self.board)
            reward = 1.0
            done = False
            info = {"Valid move made onto empty tile"}
            
        

        # If valid move and target tile is an opponent pawn
        if targetTilePiece == "op1" or targetTilePiece == "op2":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            observation = np.array(self.board)
            reward = 10.0
            done = False
            info = {"Valid move made, opponent pawn taken"}
            

        # If valid move and target tile is an opponent knight
        if targetTilePiece == "on1" or targetTilePiece == "on2":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            observation = np.array(self.board)
            reward = 30.0
            done = False
            info = {"Valid move made, opponent knight taken"}
            
        
        # If valid move and target tile is an opponent bishop
        if targetTilePiece == "ob1" or targetTilePiece == "ob2":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            observation = np.array(self.board)
            reward = 30.0
            done = False
            info = {"Valid move made, opponent bishop taken"}
            
        
        # If valid move and target tile is an opponent rook
        if targetTilePiece == "or1" or targetTilePiece == "or2":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            observation = np.array(self.board)
            reward = 50.0
            done = False
            info = {"Valid move made, opponent rook taken"}
            
        
        # If valid move and target tile is an opponent queen
        if targetTilePiece == "oq":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            observation = np.array(self.board)
            reward = 90.0
            done = False
            info = {"Valid move made, opponent queen taken"}
            

        return observation, reward, done, info
    
    
env = ChessEnv()
num_episodes = 1000

for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0

    while True:
        # Replace the following line with your RL algorithm to choose an action
        action = env.action_space[np.random.choice(len(env.action_space))]
        observation, reward, done, info = env.step(action)

        total_reward += reward

        if done:
            break

    print(f"Episode {episode + 1}/{num_episodes}, Total Reward: {total_reward}")

# Save the trained model
env.save_model("trained_chess_model.h5")