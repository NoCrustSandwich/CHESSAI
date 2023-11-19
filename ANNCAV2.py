# Class and Library Imports
import chessWS
import chessRLE
import chessIC
import numpy as np
import keyboard
import time



###############################################################################################################################################################
#ANNCAV2 - Artificial Neural Network Chess Agent Version 2
###############################################################################################################################################################

class ANNCA:

    def __init__(self, state):

        # Initializes instances of the classes necessary for the agent
        self.chessWebScraper = chessWS.webScraper()
        self.chessLogic = chessRLE.RLE()
        self.chessController = chessIC.controller()
        self.state = state

        # Enter IDLE state when you want ANNCA to play
        if self.state == "RUN":
            self.runState()

        if self.state == "UT":
            pass

    # Returns the state ANNCA is in currently
    def getState(self):
        return self.state

     # IDLE run state for Agent waiting for instruction
    def runState(self):

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

###############################################################################################################################################################

