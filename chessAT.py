# Library Imports
import os
import chess.pgn
import numpy as np
import chessRLE
import random
import re

###############################################################################################################################################################
# Agent Trainer - Version 2.0 (24/11/2023)
###############################################################################################################################################################

class trainer:

    def __init__(self, training_data_directory='Documents/ANNCA/training_data'):
        """
        Initializes an instance of the trainer class, and checks if the training data folder exists on device and if not creates it.
        """
        self.RLE = chessRLE.RLE()
        self.training_data_directory = training_data_directory

        home_directory = os.path.expanduser("~")
        full_model_directory = os.path.join(home_directory, self.training_data_directory)
        if not os.path.exists(full_model_directory):
            os.makedirs(full_model_directory)

        
    def active_train(self, number_of_games): # Trains Agent by Playing Against Itself

        for game in range(number_of_games):

            self.RLE.reset_game_state()
            total_reward = 0
            perspective = "w"

            while True:
                
                qValues = self.RLE.neuralNetwork.model.predict(self.RLE.preprosess_input())
                best_actions = np.argsort(qValues)[-10:][::-1]
                random_integer = random.randint(1, 1023)

                if random_integer > 511:                            # Randomly picks 1 of the current top 10 moves with decreasing likelihood
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0]]
                elif random_integer > 255:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[1]]
                elif random_integer > 127:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[2]]
                elif random_integer > 63:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[3]]
                elif random_integer > 31:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[4]]
                elif random_integer > 15:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[5]]
                elif random_integer > 7:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[6]]
                elif random_integer > 3:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[7]]
                elif random_integer > 1:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[8]]
                elif random_integer == 1:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[9]]
      
                action_info, final_board_state, action_reward, valid_move, game_end = self.RLE.attempt_action(action,perspective)

                if valid_move:              # Switches player turn on successful move being made 
                    if perspective == "w":
                        perspective = "b"
                    else:
                        perspective = "w"

                total_reward += action_reward

                if game_end:
                    break

            print(f"Game {game + 1}/{number_of_games}, Game's Total Reward: {total_reward}")

            self.RLE.neuralNetwork.save_model("ANNCA")


    def preprocess_board(self,board): # preprocesses board for input to the neural network
        
        preprocessed_board = []

        for rank in range(8):
            rank = []
            for file in range(8):
                piece = board.piece_at(chess.square(file, 7 - rank))
                if piece is None:
                    rank.append("_")
                else:
                    rank.append(piece.symbol())
            preprocessed_board.append(rank)

        return preprocessed_board
    

    def data_train(self): # Trains Agent by Reinforcing Winning Player's Game Moves in PGN Files 

        home_directory = os.path.expanduser("~")
        full_model_directory = os.path.join(home_directory, self.training_data_directory)
        for filename in os.listdir(full_model_directory):

            if filename.endswith(".pgn"):

                pgn_file_path = os.path.join(full_model_directory, filename)
                with open(pgn_file_path, 'r') as pgn:

                    game = chess.pgn.read_game(pgn)
                    
                    result = game.headers.get('Result')
                    if result == '1-0':
                        winner = 'w'
                    elif result == '0-1':
                        winner = 'b'
                    else:
                        winner = 'NA'

                    if game:

                        self.RLE.reset_game_state()

                        print(game.mainline_moves())

                        for move in game.mainline_moves():
                            #print(move)
                            pass

                self.RLE.neuralNetwork.save_model("ANNCA") 


###############################################################################################################################################################
new = trainer()
new.data_train()
