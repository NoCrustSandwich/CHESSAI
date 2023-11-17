# Class and Library Imports
import chessWS
import chessRL
import chessController
import numpy as np
import keyboard
import time


###############################################################################################################################################################
#ANNCAV2 - Artificial Neural Network Chess Agent Version 2
###############################################################################################################################################################

class ANNCAv2:

    def __init__(self):

        # Initializes instances of the classes necessary for the agent
        self.chessWebScraper = chessWS.webScraper()
        self.chessLogic = chessRL.ChessRLEnv()
        self.chessController = chessController.controller()

        # Automatically enter IDLE state by default
        self.IDLEState()

     # IDLE state for Agent waiting for instruction
    def IDLEState(self):

        # Input the gameURL
        gameURL = input("Input gameURL:")
        self.chessWebScraper.updateGameURL(url=gameURL)
        playerColor = input("Input player Color (w/b):").lower() 
        self.chessWebScraper.updatePlayerColor(color=playerColor)

        # Opens web page in the background
        self.chessWebScraper.openWebPage()

        while True:

            time.sleep(1)

            # Makes a move
            if keyboard.is_pressed('space'):
                self.chessWebScraper.updateCurrentBoard()
                self.chessLogic.updateBoard(self.chessWebScraper.getCurrentBoard())
                sourceTile, targetTile = self.chessLogic.getMovePrediction()
                self.chessController.movePieceExternally(sourceTile,targetTile)

                if self.chessWebScraper.getPlayerColor == "w":
                    print("Move made: "+self.chessController.getWhiteCoords(sourceTile)+" to "+ self.chessController.getWhiteCoords(targetTile))
                else:
                    print("Move made: "+self.chessController.getBlackCoords(sourceTile)+" to "+ self.chessController.getBlackCoords(targetTile))

                self.chessLogic.ANN.save_ANN("CANN")

            # Saves ANN and then ends application
            if keyboard.is_pressed('esc'):
                # Saves trained model
                self.chessLogic.ANN.save_ANN("CANN")
                exit()

            

    # Trains the logic of the agent to be more accurate by playing against itself
    def trainLogic(self, numOfEpisodes):

        for episode in range(numOfEpisodes):
            self.chessLogic.reset()
            total_reward = 0

            while True:
                
                action = self.chessLogic.actionSpace[np.random.choice(len(self.chessLogic.actionSpace))]
                observation, reward, done, info, switchPlayer, startLocation, endLocation = self.chessLogic.step(action)

                if switchPlayer:
                    self.chessLogic.render()
                    self.chessLogic.changePlayer()

                total_reward += reward

                if done:
                    break

            print(f"Episode {episode + 1}/{numOfEpisodes}, Total Reward: {total_reward}")

        # Saves trained model
        self.chessLogic.ANN.save_ANN("CANN")



###############################################################################################################################################################

ANNCA = ANNCAv2()