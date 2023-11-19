# Library Imports
import chess.pgn
import numpy as np
import chessRLE
import random
import re

###############################################################################################################################################################
# ANN Trainer
###############################################################################################################################################################

class trainer:

    def __init__(self, state):

        # Dictionary used to translate PGN board to ANN format if player is white
        self.PGN_To_ANN_White_Player = {

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
        self.PGN_To_ANN_Black_Player = {

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

        # Coordinates from white players perspective
        self.positionToCoordinatesWhite = {
        'a8': (0, 0), 'b8': (0, 1), 'c8': (0, 2), 'd8': (0, 3),'e8': (0, 4), 'f8': (0, 5), 'g8': (0, 6), 'h8': (0, 7),
        'a7': (1, 0), 'b7': (1, 1), 'c7': (1, 2), 'd7': (1, 3),'e7': (1, 4), 'f7': (1, 5), 'g7': (1, 6), 'h7': (1, 7),
        'a6': (2, 0), 'b6': (2, 1), 'c6': (2, 2), 'd6': (2, 3),'e6': (2, 4), 'f6': (2, 5), 'g6': (2, 6), 'h6': (2, 7),
        'a5': (3, 0), 'b5': (3, 1), 'c5': (3, 2), 'd5': (3, 3),'e5': (3, 4), 'f5': (3, 5), 'g5': (3, 6), 'h5': (3, 7),
        'a4': (4, 0), 'b4': (4, 1), 'c4': (4, 2), 'd4': (4, 3),'e4': (4, 4), 'f4': (4, 5), 'g4': (4, 6), 'h4': (4, 7),
        'a3': (5, 0), 'b3': (5, 1), 'c3': (5, 2), 'd3': (5, 3),'e3': (5, 4), 'f3': (5, 5), 'g3': (5, 6), 'h3': (5, 7),
        'a2': (6, 0), 'b2': (6, 1), 'c2': (6, 2), 'd2': (6, 3),'e2': (6, 4), 'f2': (6, 5), 'g2': (6, 6), 'h2': (6, 7),
        'a1': (7, 0), 'b1': (7, 1), 'c1': (7, 2), 'd1': (7, 3),'e1': (7, 4), 'f1': (7, 5), 'g1': (7, 6), 'h1': (7, 7),
        }

        # Coordinates from black players perspective
        self.positionToCoordinatesBlack = {
        'h1': (0, 0), 'g1': (0, 1), 'f1': (0, 2), 'e1': (0, 3),'d1': (0, 4), 'c1': (0, 5), 'b1': (0, 6), 'a1': (0, 7),
        'h2': (1, 0), 'g2': (1, 1), 'f2': (1, 2), 'e2': (1, 3),'d2': (1, 4), 'c2': (1, 5), 'b2': (1, 6), 'a2': (1, 7),
        'h3': (2, 0), 'g3': (2, 1), 'f3': (2, 2), 'e3': (2, 3),'d3': (2, 4), 'c3': (2, 5), 'b3': (2, 6), 'a3': (2, 7),
        'h4': (3, 0), 'g4': (3, 1), 'f4': (3, 2), 'e4': (3, 3),'d4': (3, 4), 'c4': (3, 5), 'b4': (3, 6), 'a4': (3, 7),
        'h5': (4, 0), 'g5': (4, 1), 'f5': (4, 2), 'e5': (4, 3),'d5': (4, 4), 'c5': (4, 5), 'b5': (4, 6), 'a5': (4, 7),
        'h6': (5, 0), 'g6': (5, 1), 'f6': (5, 2), 'e6': (5, 3),'d6': (5, 4), 'c6': (5, 5), 'b6': (5, 6), 'a6': (5, 7),
        'h7': (6, 0), 'g7': (6, 1), 'f7': (6, 2), 'e7': (6, 3),'d7': (6, 4), 'c7': (6, 5), 'b7': (6, 6), 'a7': (6, 7),
        'h8': (7, 0), 'g8': (7, 1), 'f8': (7, 2), 'e8': (7, 3),'d8': (7, 4), 'c8': (7, 5), 'b8': (7, 6), 'a8': (7, 7),
        }

        # Loads the Reinforcment Learning Enviorment
        self.RLE = chessRLE.RLE()
    

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


    # Trains the logic of the agent to be more accurate by playing against itself
    def activeTrain(self, numOfEpisodes):

        for episode in range(numOfEpisodes):

            self.RLE.resetBoard()
            total_reward = 0

            while True:
                
                # Randomlly picks 1 of top 10 moves with decreasing likelihood
                qValues = self.RLE.ANN.model.predict(self.RLE.preprosessANNInput())

                topIndices = np.argsort(qValues)[-10:][::-1]

                randomInteger = random.randint(1, 1023)

                if randomInteger > 511:
                    action = self.RLE.actionSpace[topIndices[0]]
                elif randomInteger > 255:
                    action = self.RLE.actionSpace[topIndices[1]]
                elif randomInteger > 127:
                    action = self.RLE.actionSpace[topIndices[2]]
                elif randomInteger > 63:
                    action = self.RLE.actionSpace[topIndices[3]]
                elif randomInteger > 31:
                    action = self.RLE.actionSpace[topIndices[4]]
                elif randomInteger > 15:
                    action = self.RLE.actionSpace[topIndices[5]]
                elif randomInteger > 7:
                    action = self.RLE.actionSpace[topIndices[6]]
                elif randomInteger > 3:
                    action = self.RLE.actionSpace[topIndices[7]]
                elif randomInteger > 1:
                    action = self.RLE.actionSpace[topIndices[8]]
                elif randomInteger == 1:
                    action = self.RLE.actionSpace[topIndices[9]]
      
                observation, reward, done, info, switchPlayer, startLocation, endLocation = self.RLE.step(action)

                if switchPlayer:
                    self.RLE.render()
                    self.RLE.changePlayer()

                total_reward += reward

                if done:
                    break

            print(f"Episode {episode + 1}/{numOfEpisodes}, Total Reward: {total_reward}")

            # Saves trained model after each simulated round
            self.RLE.ANN.saveANN("CANN")

        # Saves trained model
        self.RLE.ANN.saveANN("CANN")

        # Used for unit testing
        return True


    # Converts PGN file to a board input 2D list
    def dataTrain(self, PGNFilePath):

        whiteTurn = True
        
        # Open the PGN file for reading
        with open(PGNFilePath, 'r') as pgn:
            game = chess.pgn.read_game(pgn)
            
            # Extract the winner from the game's result
            result = game.headers.get('Result')
            if result == '1-0':
                winner = 'w'
            elif result == '0-1':
                winner = 'b'
            elif result == '1/2-1/2':
                winner = 'd'

            if game:
                self.RLE.resetBoard()

                for move in game.mainline_moves():
                    print("Move: "+ str(move))
                    
                    if(whiteTurn):

                        print("White")

                        print("Before Move: "+str(self.RLE.getCurrentBoard()))

                        pattern = r'\b[A-Za-z]\d+\b'
                        result = re.sub(pattern, '', str(move))

                        print(result)

                        if len(result) == 4:
                            sourceMove = str(result)[0:2]
                            targetMove = str(result)[2:4]

                            action = self.preprocessOutput(sourceMove,targetMove,self.RLE.getCurrentBoard(),"w")

                            # Very high reward to incentivise this move over any others
                            reward = 100000.0
                            
                            # Retrieves Qvalues from ANN and action index of the action being trained
                            qValues = self.RLE.ANN.model.predict(self.RLE.preprosessANNInput())
                            actionIndex = self.RLE.actionSpace.index(action)

                            # Only consider winning player's moves
                            if winner == "W":
                                self.RLE.trainANN(reward, qValues, actionIndex)

                            self.RLE.updateBoardWithMove(self.positionToCoordinatesWhite[sourceMove], self.positionToCoordinatesWhite[targetMove])
                            self.RLE.changePlayer()
    
                        whiteTurn = False

                    else:
                        
                        print("Black")

                        print("Before Move: "+str(self.RLE.getCurrentBoard()))
                                         
                        pattern = r'\b[A-Za-z]\d+\b'
                        result = re.sub(pattern, '', str(move))

                        print(result)

                        if len(result) == 4:

                            sourceMove = str(result)[0:2]
                            targetMove = str(result)[2:4]

                            action = self.preprocessOutput(sourceMove,targetMove,self.RLE.getCurrentBoard(),"b")

                            print(action)

                            # Very high reward to incentivise this move over any others
                            reward = 100000.0

                            # Retrieves Qvalues from ANN and action index of the action being trained
                            qValues = self.RLE.ANN.model.predict(self.RLE.preprosessANNInput())
                            actionIndex = self.RLE.actionSpace.index(action)

                            # Only consider winning player's moves
                            if winner == "B":
                                self.RLE.trainANN(reward, qValues, actionIndex)

                            self.RLE.updateBoardWithMove(self.positionToCoordinatesBlack[sourceMove], self.positionToCoordinatesBlack[targetMove])
                            self.RLE.changePlayer()
                            
                        whiteTurn = True

                    print("After Move: "+str(self.RLE.getCurrentBoard()))

        # Saves trained model
        self.RLE.ANN.saveANN("CANN")

        # Used for unit testing
        return True


    # Translates board from chars to integer representations (Changes board to numerical values)
    def preprocessInput(self, board, playerColor):

        # Initilizes input board as empty to be populated by translated board elements
        inputBoard = [["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"]]

        # Populates the board based on player color
        if playerColor =="w":
            for row in range(8):
                for col in range(8):
                    inputBoard[row][col] = self.PGN_To_ANN_White_Player[board[row][col]]
        else:
            for row in range(8):
                for col in range(8):
                    inputBoard[row][col] = self.PGN_To_ANN_Black_Player[board[row][col]]

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
    def preprocessOutput(self,sourceMove,targetMove,inputBoard, playerColor):

        # Preprocesses the format to be like the action format for the ANN
        if playerColor == "w":
            sourceCoords = self.positionToCoordinatesWhite[sourceMove]
            targetCoords = self.positionToCoordinatesWhite[targetMove]
            piece = inputBoard[sourceCoords[0]][sourceCoords[1]]

            action = (piece,(targetCoords[0]-sourceCoords[0],targetCoords[1]-sourceCoords[1]))
        else:
            sourceCoords = self.positionToCoordinatesBlack[sourceMove]
            targetCoords = self.positionToCoordinatesBlack[targetMove]
            piece = inputBoard[sourceCoords[0]][sourceCoords[1]]

            action = (piece,(targetCoords[0]-sourceCoords[0],targetCoords[1]-sourceCoords[1]))

        return action

###############################################################################################################################################################