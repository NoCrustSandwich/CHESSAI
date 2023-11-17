# Library Imports
import chess.pgn
import numpy as np

###############################################################################################################################################################
# ANN Trainer
###############################################################################################################################################################


class trainer:


    def __init__(self):

        # Construct the path to the PGN file in the F:\LichlessData directory
        self.PGNFilePath = r'F:\LichlessData\lichess_db_standard_rated_2013-01.pgn'

        self.pgn_to_board()
    

    # Converts Board to custom format for ANN
    def convertBoardToANNFormat(self,board):
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
    def pgn_to_board(self):

        board = chess.Board()

        inputBoards = []
        whiteTurn = True


        sourceMoves = []
        targetMoves = []

        

        # Open the PGN file for reading
        with open(self.PGNFilePath, 'r') as pgn:
            game = chess.pgn.read_game(pgn)
            
            # Extract the winner from the game's result
            result = game.headers.get('Result')
            if result == '1-0':
                winner = 'W'
            elif result == '0-1':
                winner = 'B'
            elif result == '1/2-1/2':
                winner = 'D'

            print(game.mainline_moves())

            if game:
                board = game.board()
                for move in game.mainline_moves():
                    
                    if(whiteTurn):
                    
                        # Only consider winning player's moves
                        if winner == 'W':


                            inputBoard = self.preprocessInput(self.convertBoardToANNFormat(board), winner)

                            sourceMove = str(move)[0:2]
                            targetMove = str(move)[2:4]

                            action = self.preprocessOutput(sourceMove,targetMove,inputBoard)

                            
                            

                        whiteTurn = False

                    else:

                        # Only consider winning player's moves
                        if winner == 'B':

                            inputBoard = self.preprocessInput(self.convertBoardToANNFormat(board), winner)

                            sourceMove = str(move)[0:2]
                            targetMove = str(move)[2:4]
                            
                            action = self.preprocessOutput(sourceMove,targetMove,inputBoard)

                    


                        whiteTurn = True
        




    # Translates board from chars to integer representations (Changes board to numerical values)
    def preprocessInput(self, board, playerColor):

        # Dictionary used to translate PGN board to ANN format if player is white
        PGN_To_ANN_White_Player = {

            "_": "_",

            "p": "op",
            "k": "ok",
            "q": "oq",
            "b": "ob",
            "r": "or",
            "n": "on",

            "P": "p",
            "K": "k",
            "Q": "q",
            "B": "b",
            "R": "r",
            "N": "n",

            
        }

        # Dictionary used to translate PGN board to ANN format if player is black
        PGN_To_ANN_Black_Player = {

            "_": "_",

            "p": "p",
            "k": "k",
            "q": "q",
            "b": "b",
            "r": "r",
            "n": "n",

            "P": "op",
            "K": "ok",
            "Q": "oq",
            "B": "ob",
            "R": "or",
            "N": "on",
        }

        
        inputBoard = [["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"]]


        # Populates the board based on player color
        if playerColor =="W":
            for row in range(8):
                for col in range(8):
                    inputBoard[row][col] = PGN_To_ANN_White_Player[board[row][col]]
        else:
            for row in range(8):
                for col in range(8):
                    inputBoard[row][col] = PGN_To_ANN_Black_Player[board[row][col]]

            # Reverses board to be from black players perspective
            inputBoard = [row[::-1] for row in inputBoard[::-1]]

         # To maintain similar numbering between sides, numbered backwards for opponennt side because their side is mirrored
        opCounter = 8
        pCounter = 1
        bCounter = 1
        obCounter = 2
        rCounter = 1
        orCounter = 2
        nCounter = 1
        onCounter = 2

        # Adds Numbers to rendered pieces on inputBoard
        for i in range(len(inputBoard)):
            for j in range(len(inputBoard)):

                if inputBoard[i][j] == "op":
                    inputBoard[i][j] =  inputBoard[i][j]+str(opCounter)
                    opCounter-=1
                
                if inputBoard[i][j] == "ob":
                    inputBoard[i][j] = inputBoard[i][j]+str(obCounter)
                    obCounter-=1
                
                if inputBoard[i][j] == "on":
                    inputBoard[i][j] = inputBoard[i][j]+str(onCounter)
                    onCounter-=1

                if inputBoard[i][j] == "or":
                    inputBoard[i][j] = inputBoard[i][j]+str(orCounter)
                    orCounter-=1


                if inputBoard[i][j] == "p":
                    inputBoard[i][j] = inputBoard[i][j]+str(pCounter)
                    pCounter+=1
                
                if inputBoard[i][j] == "b":
                    inputBoard[i][j] = inputBoard[i][j]+str(bCounter)
                    bCounter+=1
                
                if inputBoard[i][j] == "n":
                    inputBoard[i][j] = inputBoard[i][j]+str(nCounter)
                    nCounter+=1

                if inputBoard[i][j] == "r":
                    inputBoard[i][j] = inputBoard[i][j]+str(rCounter)
                    rCounter+=1

        return inputBoard

    # Translates the inputted moves from algebraic coordinate notation to index notation
    def preprocessOutput(self,moves):

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


new = trainer()





###############################################################################################################################################################