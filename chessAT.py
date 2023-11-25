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
    

    def san_to_action(self, board, san_move, lan_move, perspective):

        if str(san_move) == "o-o-o":
            return ("k", (0,-2))
        
        if str(san_move) == "o-o":
            return ("k", (0,2))

        if len(san_move) == 2:

            source_coordinates = str(lan_move)[0:2]
            target_coordinates = str(lan_move)[2:4]
            
            if perspective == "w":
                source_indices = self.RLE.COORDINATES_TO_TILE_INDICES_WHITE_PERSPECTIVE[source_coordinates]
                target_indices = self.RLE.COORDINATES_TO_TILE_INDICES_WHITE_PERSPECTIVE[target_coordinates]
            else:
                source_indices = self.RLE.COORDINATES_TO_TILE_INDICES_BLACK_PERSPECTIVE[source_coordinates]
                target_indices = self.RLE.COORDINATES_TO_TILE_INDICES_BLACK_PERSPECTIVE[target_coordinates]

            piece = board[source_indices[0]][source_indices[1]]
            dx = target_indices[0] - source_indices[0]
            dy = target_indices[1] - source_indices[1]

            return (piece, (dx, dy))

        elif len(san_move) in {3,4,5,6} and str(san_move)[2] != "=":

            source_coordinates = str(lan_move)[0:2]
            target_coordinates = str(lan_move)[2:4]
            
            if perspective == "w":
                source_indices = self.RLE.COORDINATES_TO_TILE_INDICES_WHITE_PERSPECTIVE[source_coordinates]
                target_indices = self.RLE.COORDINATES_TO_TILE_INDICES_WHITE_PERSPECTIVE[target_coordinates]
            else:
                source_indices = self.RLE.COORDINATES_TO_TILE_INDICES_BLACK_PERSPECTIVE[source_coordinates]
                target_indices = self.RLE.COORDINATES_TO_TILE_INDICES_BLACK_PERSPECTIVE[target_coordinates]

            piece = board[source_indices[0]][source_indices[1]]
            dx = target_indices[0] - source_indices[0]
            dy = target_indices[1] - source_indices[1]

            return (piece, (dx, dy))

        elif len(san_move) == 4 and str(san_move)[2] == "=":

            source_coordinates = str(lan_move)[0:2]
            target_coordinates = str(lan_move)[2:4]
            
            if perspective == "w":
                source_indices = self.RLE.COORDINATES_TO_TILE_INDICES_WHITE_PERSPECTIVE[source_coordinates]
                target_indices = self.RLE.COORDINATES_TO_TILE_INDICES_WHITE_PERSPECTIVE[target_coordinates]
            else:
                source_indices = self.RLE.COORDINATES_TO_TILE_INDICES_BLACK_PERSPECTIVE[source_coordinates]
                target_indices = self.RLE.COORDINATES_TO_TILE_INDICES_BLACK_PERSPECTIVE[target_coordinates]

            piece = board[source_indices[0]][source_indices[1]]
            dx = target_indices[0] - source_indices[0]
            dy = target_indices[1] - source_indices[1]

            return (piece, (dx, dy), str(san_move)[3].lower())
        


    def data_train(self):
        """
        Trains the Agent by Reinforcing Winning Player's Game Moves in PGN Files.

        This method reads chess games from PGN files, identifies the winning player, and reinforces
        the neural network based on the moves made by the winning player.

        The training process involves iterating through the moves of each game, extracting the SAN
        (Standard Algebraic Notation) moves, and updating the neural network based on the moves made
        by the winning player.

        Note: The neural network used for training should be associated with the Reinforcement
        Learning Environment (RLE) instance.

        Returns:
            - None

        Example:
            chessAT = trainer()
            chessAT.data_train()
        """
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
                        
                        perpsective = "w"
                        move_index = 0
                        self.RLE.reset_game_state()

                        full_move_history_san = str(game.mainline_moves()).split(" ")
                        filtered_move_history_san = []
                        

                        for index in range(len(full_move_history_san)):
                            if index % 3 == 1:
                                filtered_move_history_san.append(full_move_history_san[index])
                            elif index % 3 == 2:
                                filtered_move_history_san.append(full_move_history_san[index])
                        
                        for lan_move in game.mainline_moves():

                            print(filtered_move_history_san[move_index])
                            print(lan_move)

                            if perpsective == "w": # White's Move

                                action = self.san_to_action(self.RLE.board_white, filtered_move_history_san[move_index], lan_move, perpsective)
                                q_values = self.RLE.neuralNetwork.model.predict(self.RLE.preprosess_input(self.RLE.board_white))
                                action_index = self.RLE.POSSIBLE_MOVES.index(action)

                                if winner == "w":
                                    self.RLE.train_neural_network(self.RLE.board_white, 10000.0, q_values, action_index)

                                self.RLE.attempt_action(action, perpsective)
                                perpsective = "b"
                                move_index += 1

                            else:              # Black's Move

                                action = self.san_to_action(self.RLE.board_black, filtered_move_history_san[move_index],lan_move, perpsective)
                                q_values = self.RLE.neuralNetwork.model.predict(self.RLE.preprosess_input(self.RLE.board_black))
                                action_index = self.RLE.POSSIBLE_MOVES.index(action)

                                if winner == "b":
                                    self.RLE.train_neural_network(self.RLE.board_black, 10000.0, q_values, action_index)
                                
                                self.RLE.attempt_action(action, perpsective)
                                perpsective = "w"
                                move_index += 1

                        self.RLE.neuralNetwork.save_model("ANNCA") 

###############################################################################################################################################################
new = trainer()
new.data_train()