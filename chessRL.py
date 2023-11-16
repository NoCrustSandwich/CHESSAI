# Library Imports
import gym
from gym import spaces
import numpy as np
import copy
import chessANN


###############################################################################################################################################################
# Reinforcment Learning Enviorment
###############################################################################################################################################################

# Class for the chess board enviorment for the RL
class ChessRLEnv(gym.Env):

    def __init__(self):
        



        
        # Dictionary to translate board to opposing players perspective
        self.playerChanger = {

            "_":"_",
            "p1": "op1", "p2": "op2", "p3": "op3", "p4": "op4", "p5": "op5", "p6": "op6", "p7": "op7", "p8": "op8",
            "op1": "p1", "op2": "p2", "op3": "p3", "op4": "p4", "op5": "p5", "op6": "p6", "op7": "p7", "op8": "p8",
            "n1": "on1", "n2": "on2",
            "on1": "n1", "on2": "n2",
            "b1": "ob1", "b2": "ob2",
            "ob1": "b1", "ob2": "b2",
            "r1": "or1", "r2": "or2",
            "or1": "r1", "or2": "r2",
            "q": "oq",
            "oq": "q",
            "k": "ok",
            "ok": "k",

        }

        # Dictionary to translate board ints to string representations
        self.intToPiece ={
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

        
        # Dictionary to translate board string to integer representations
        self.pieceToInt = {
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
        self.actionSpace    =   [   

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

        self.observationSpace = spaces.Box(low=-6, high=6, shape=(8, 8), dtype=int)
        self.ANN = chessANN.ANN()

    # Reverses the board side to play from the oppostive perspective
    def changePlayer(self):
        
        self.board = [row[::-1] for row in self.board[::-1]]

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = self.playerChanger[self.board[i][j]]
        

    # Renders the current board
    def render(self):
        for row in self.board:
            print(" ".join("{:<3}".format(cell) for cell in row))
            print("\n")


    # Resets back to starting position
    def resetBoard(self):
        # Reset the board to its initial state
        self.board = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q","k","b2","n2","r2"]]


    

    # Returns translated board in numpy array format for ANN input
    def preprosessANNInput(self):
        translatedBoard = [[self.pieceToInt[piece] for piece in row] for row in self.board]
        return np.array([translatedBoard])

    # Trains ANN based on reward
    def trainANN(self, reward, qValues, actionIndex):

        qValues[0, actionIndex] = reward
        self.ANN.model.fit(self.preprosessANNInput(), qValues, epochs=1, verbose=0)


        

    # Runs through an action for the RL
    def step(self, action):
        
        # Retrieves Qvalues from ANN and action index of the action being trained
        qValues = self.ANN.model.predict(self.preprosessANNInput())
        actionIndex = self.actionSpace.index(action)
        
       
       

        # Determines the index location of the piece taking the action
        piecePresent = False

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == action[0]:
                    sourceLocation = [x,y]
                    targetLocation =  [x-action[1][1],y+action[1][0]]
                    piecePresent = True

        

        # Checks if the piece being moved is present on the board
        if not piecePresent:

            observation = self.board
            reward = -1000.0
            done = False
            info = {"Invalid Move, Piece is not present on the board"}
            switchPlayer = False

            self.trainANN(reward,qValues, actionIndex)

            return observation, reward, done, info,switchPlayer

        # Checks if the move is out of range
        if targetLocation[0]>7 or targetLocation[1]>7 or targetLocation[0]<0 or targetLocation[1]<0:

            observation = self.board
            reward = -1000.0
            done = False
            info = {"Invalid Move, Target Location is out of range"}
            switchPlayer = False

            self.trainANN(reward,qValues, actionIndex)

            return observation, reward, done, info,switchPlayer






        # Retrieves item present at the target tile
        targetTilePiece = self.board[targetLocation[0]][targetLocation[1]] 

        # Prevents capture of own pieces
        if targetTilePiece in {"k", "q", "p1", "p2", "p3", "p4","p5","p6","p7","p8","r1","r2","b1","b2","n1","n2"}:

            observation = self.board
            reward = -1000.0
            done = False
            info = {"Invalid Move, Cannot capture piece that belongs to player"}
            switchPlayer = False

            self.trainANN(reward,qValues, actionIndex)

            return observation, reward, done, info, switchPlayer
       




        # Pawn invalid move attempts
        if action[0] in {"p1", "p2", "p3", "p4","p5","p6","p7","p8"}:

            if action[1][1] == 2 and sourceLocation[0]!=6:

                observation = self.board
                reward = -1000.0
                done = False
                info = {"Invalid Move, pawn cannot move 2 spaces unless in starting position"}
                switchPlayer = False

                self.trainANN(reward,qValues, actionIndex)

                return observation, reward, done, info, switchPlayer
            
            if action[1][0]!=0 and targetTilePiece == "_":

                observation = self.board
                reward = -1000.0
                done = False
                info = {"Invalid Move, pawn cannot side ways unless opossing piece is there"}
                switchPlayer = False

                self.trainANN(reward,qValues, actionIndex)

                return observation, reward, done, info, switchPlayer
            

            if action[1][1] == 2 and sourceLocation[0]==6 and self.board[sourceLocation[0]-1][sourceLocation[1]] != "_":

                observation = self.board
                reward = -1000.0
                done = False
                info = {"Invalid Move, pawn is blocked by other piece in it's path"}
                switchPlayer = False

                self.trainANN(reward,qValues, actionIndex)

                return observation, reward, done, info, switchPlayer

            if action[1][1] == 1 and targetTilePiece != "_":

                observation = self.board
                reward = -1000.0
                done = False
                info = {"Invalid Move, pawn is blocked by other piece in it's path"}
                switchPlayer = False

                self.trainANN(reward,qValues, actionIndex)

                return observation, reward, done, info, switchPlayer



        # Rook and queen invalid move attempts
        if action[0] in {"r1", "r2", "q"}:

            
            if action[1][1] > 0:

                for index in range(action[1][1]):

                    if index == 0:
                        continue

                    if self.board[sourceLocation[0]-index][sourceLocation[1]] !=  "_":

                        observation = self.board
                        reward = -1000.0
                        done = False
                        info = {"Invalid Move, rook or queen is blocked by other piece in it's path"}
                        switchPlayer = False

                        self.trainANN(reward,qValues, actionIndex)

                        return observation, reward, done, info, switchPlayer
                    



            if action[1][1] < 0:

                for index in range(-action[1][1]):

                    if index == 0:
                        continue

                    if self.board[sourceLocation[0]+index][sourceLocation[1]] !=  "_":

                        observation = self.board
                        reward = -1000.0
                        done = False
                        info = {"Invalid Move, rook or queen is blocked by other piece in it's path"}
                        switchPlayer = False

                        self.trainANN(reward,qValues, actionIndex)

                        return observation, reward, done, info, switchPlayer



            if action[1][0] > 0:

                for index in range(action[1][0]):

                    if index == 0:
                        continue

                    if self.board[sourceLocation[0]][sourceLocation[1]+index] !=  "_":

                        observation = self.board
                        reward = -1000.0
                        done = False
                        info = {"Invalid Move, rook or queen is blocked by other piece in it's path"}
                        switchPlayer = False

                        self.trainANN(reward,qValues, actionIndex)

                        return observation, reward, done, info, switchPlayer
                    



            if action[1][0] < 0:

                for index in range(-action[1][0]):

                    if index == 0:
                        continue

                    if self.board[sourceLocation[0]][sourceLocation[1]-index] !=  "_":

                        observation = self.board
                        reward = -1000.0
                        done = False
                        info = {"Invalid Move, rook or queen is blocked by other piece in it's path"}
                        switchPlayer = False

                        self.trainANN(reward,qValues, actionIndex)

                        return observation, reward, done, info, switchPlayer


        # bishop and queen invalid move attempts
        if action[0] in {"b1", "b2", "q"}:

            if action[1][0] > 0 and action[1][1] > 0:

                for index in range(action[1][0]):

                    if index == 0:
                        continue

                    if self.board[sourceLocation[0]-index][sourceLocation[1]+index] !=  "_":

                        observation = self.board
                        reward = -1000.0
                        done = False
                        info = {"Invalid Move, bishop or queen is blocked by other piece in it's path"}
                        switchPlayer = False

                        self.trainANN(reward,qValues, actionIndex)

                        return observation, reward, done, info, switchPlayer
                    




            if action[1][0] > 0 and action[1][1] < 0:

                for index in range(action[1][0]):

                    if index == 0:
                        continue

                    if self.board[sourceLocation[0]+index][sourceLocation[1]+index] !=  "_":

                        observation = self.board
                        reward = -1000.0
                        done = False
                        info = {"Invalid Move, bishop or queen is blocked by other piece in it's path"}
                        switchPlayer = False

                        self.trainANN(reward,qValues, actionIndex)

                        return observation, reward, done, info, switchPlayer

            if action[1][0] < 0 and action[1][1] > 0:

                for index in range(-action[1][0]):

                    if index == 0:
                        continue

                    if self.board[sourceLocation[0]-index][sourceLocation[1]-index] !=  "_":

                        observation = self.board
                        reward = -1000.0
                        done = False
                        info = {"Invalid Move, bishop or queen is blocked by other piece in it's path"}
                        switchPlayer = False

                        self.trainANN(reward,qValues, actionIndex)

                        return observation, reward, done, info, switchPlayer

            if action[1][0] < 0 and action[1][1] < 0:

                for index in range(-action[1][0]):

                    if index == 0:
                        continue

                    if self.board[sourceLocation[0]+index][sourceLocation[1]-index] !=  "_":

                        observation = self.board
                        reward = -1000.0
                        done = False
                        info = {"Invalid Move, bishop or queen is blocked by other piece in it's path"}
                        switchPlayer = False

                        self.trainANN(reward,qValues, actionIndex)

                        return observation, reward, done, info, switchPlayer




        # If valid move and target tile is empty
        if targetTilePiece == "_":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            self.board[sourceLocation[0]][sourceLocation[1]] = "_"
            observation = self.board
            reward = -1.0
            done = False
            info = {"Valid move made onto empty tile"}
            switchPlayer = True
            
            

        # If valid move and target tile is an opponent pawn
        if targetTilePiece in {"op1", "op2", "op3", "op4","op5","op6","op7","op8"}:

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            self.board[sourceLocation[0]][sourceLocation[1]] = "_"
            observation = self.board
            reward = 10.0
            done = False
            info = {"Valid move made, opponent pawn taken"}
            switchPlayer = True
            

        # If valid move and target tile is an opponent knight
        if targetTilePiece == "on1" or targetTilePiece == "on2":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            self.board[sourceLocation[0]][sourceLocation[1]] = "_"
            observation = self.board
            reward = 30.0
            done = False
            info = {"Valid move made, opponent knight taken"}
            switchPlayer = True
            
        
        # If valid move and target tile is an opponent bishop
        if targetTilePiece == "ob1" or targetTilePiece == "ob2":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            self.board[sourceLocation[0]][sourceLocation[1]] = "_"
            observation = self.board
            reward = 30.0
            done = False
            info = {"Valid move made, opponent bishop taken"}
            switchPlayer = True
            
        
        # If valid move and target tile is an opponent rook
        if targetTilePiece == "or1" or targetTilePiece == "or2":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            self.board[sourceLocation[0]][sourceLocation[1]] = "_"
            observation = self.board
            reward = 50.0
            done = False
            info = {"Valid move made, opponent rook taken"}
            switchPlayer = True
            
        
        # If valid move and target tile is an opponent queen
        if targetTilePiece == "oq":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            self.board[sourceLocation[0]][sourceLocation[1]] = "_"
            observation = self.board
            reward = 90.0
            done = False
            info = {"Valid move made, opponent queen taken"}
            switchPlayer = True

        if targetTilePiece == "ok":

            self.board[targetLocation[0]][targetLocation[1]] = action[0]
            self.board[sourceLocation[0]][sourceLocation[1]] = "_"
            observation = self.board
            reward = 100000.0
            done = True
            info = {"Valid move made, opponent King taken"}
            switchPlayer = True


        '''

        print("Board: "+str(self.board))
        print("Action: "+str(action))
        print("Source Location: " + str(sourceLocation))
        print("Target Location: " + str(targetLocation))
        print("Source Tile: " + str(self.board[sourceLocation[0]][sourceLocation[1]]))
        print("Target Tile: " + str(self.board[targetLocation[0]][targetLocation[1]]))

        '''

        self.trainANN( reward, qValues, actionIndex)

        return observation, reward, done, info,switchPlayer
    
###############################################################################################################################################################




###############################################################################################################################################################
# AI Training
###############################################################################################################################################################
def trainAI():

    env = ChessRLEnv()
    num_episodes = 1

    for episode in range(num_episodes):
        state = env.reset()
        total_reward = 0

        while True:
            # Replace the following line with your RL algorithm to choose an action
            action = env.actionSpace[np.random.choice(len(env.actionSpace))]
            observation, reward, done, info,switchPlayer = env.step(action)

            if switchPlayer:
                env.render()
                env.changePlayer()

            total_reward += reward

            if done:
                break

        print(f"Episode {episode + 1}/{num_episodes}, Total Reward: {total_reward}")

    # Save the trained model
    env.ANN.save_ANN("CANN")


trainAI()
###############################################################################################################################################################