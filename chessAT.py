import os
import random
import chessRLE
import chess.pgn
import numpy as np


###############################################################################################################################################################
# Agent Trainer - Version 3.3 (18/12/2023)
###############################################################################################################################################################

class trainer:
    """
    Trainer is a class responsible for training the neural network, by either feeding it PGN game data 
    or by simulating chess games against itself.

    Methods:
        - __init__(self): Initializes an instance of the trainer class.
        - active_train(self, number_of_games: int): Trains the agent by playing against itself, considering the top 10 moves at each step.
        - san_to_action(self, board, san_move, lan_move, perspective): Translates Standard Algebraic Notation to an action format that can be fed 
                                                                       into the ANN as an expected output.
        - data_train(self): Trains the agent by reinforcing the winning player's game moves in PGN files.

    Usage Example:
        - chessAT = trainer()
        - chessAT.data_train()
        or
        - chessAT.active_train(10)
    """

    def __init__(self):
        """
        Initializes an instance of the trainer class.
        """
        self.RLE = chessRLE.RLE()
        
    
    def active_train(self, number_of_games: int): # Trains Agent by Playing Against Itself
        """
        Trains the agent by playing against itself, considering the top 10 moves at each step.

        Parameters:
            - number_of_games (int): The number of games to play for training.

        Returns:
            - None
        """
        for game in range(number_of_games):

            self.RLE.reset_game_state()
            total_reward = 0

            while True:
                
                q_values = self.RLE.neuralNetwork.model.predict(self.RLE.preprosess_input(self.RLE.board_state))
                best_actions = np.argsort(q_values)[-10:][::-1]
                random_integer = random.randint(1, 1023)

                print(q_values)
                print(best_actions)

                if random_integer > 511:                            # Randomly picks 1 of the current top 10 moves with decreasing likelihood
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0][0]]
                elif random_integer > 255:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0][1]]
                elif random_integer > 127:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0][2]]
                elif random_integer > 63:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0][3]]
                elif random_integer > 31:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0][4]]
                elif random_integer > 15:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0][5]]
                elif random_integer > 7:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0][6]]
                elif random_integer > 3:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0][7]]
                elif random_integer > 1:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0][8]]
                elif random_integer == 1:
                    action = self.RLE.POSSIBLE_MOVES[best_actions[0][9]]

                print("Board State: "+ str(self.RLE.board_state))
                print("Action: " +str(action))
                action_info, action_reward, valid_move, game_end = self.RLE.attempt_action(action)
                print(action_info)

                if valid_move:              # Switches player turn on successful move being made 
                    self.RLE.change_perspective()

                total_reward += action_reward

                self.RLE.neuralNetwork.save_model("ANNCA")

                if game_end:
                    break
                
            print(f"Game {game + 1}/{number_of_games}, Game's Total Reward: {total_reward}")


    def san_to_action(self, board, san_move, lan_move, perspective):
        """
        Translates Standard Algebraic Notation to an action format that can be fed into the ANN as an expected output.

        Parameters:
            - board (list): The current state of the chessboard.
            - san_move (str): Standard Algebraic Notation move.
            - lan_move (chess.Move): The corresponding move in LAN format.
            - perspective (str): The perspective, either 'w' for white or 'b' for black.

        Returns:
            - Tuple: A tuple representing the action in the format (piece, (dx, dy), [promotion] or [castling]).
        """
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
        Trains the agent by reinforcing the winning player's game moves in PGN files.

        This method reads chess games from PGN files, identifies the winning player,
        and reinforces the neural network based on the moves made by the winning player.

        Returns:
            - None
        """
        full_model_directory = "training_data"

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

                    print("NEWGAME***************")
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
                            action = self.san_to_action(self.RLE.board_state, filtered_move_history_san[move_index], lan_move, perpsective)
                            print("Perspective: "+ perpsective)
                            print("Board State: "+ str(self.RLE.board_state))
                            print("Move: "+ str(lan_move))
                            print("Action: " +str(action))
                            q_values = self.RLE.neuralNetwork.model.predict(self.RLE.preprosess_input(self.RLE.board_state))
                            action_index = self.RLE.POSSIBLE_MOVES.index(action)
                            action_info, action_reward, valid_move, game_end = self.RLE.attempt_action(action)
                            print(action_info)

                            if perpsective == "w": # White's Move

                                if winner == "w":
                                    self.RLE.train_neural_network(self.RLE.board_state, 10000.0, q_values, action_index)

                                self.RLE.change_perspective()
                                perpsective = "b"
                                move_index += 1

                            else:              # Black's Move
                            
                                if winner == "b":
                                    self.RLE.train_neural_network(self.RLE.board_state, 10000.0, q_values, action_index)
                            
                                self.RLE.change_perspective()
                                perpsective = "w"
                                move_index += 1

                        self.RLE.neuralNetwork.save_model("ANNCA") 

###############################################################################################################################################################