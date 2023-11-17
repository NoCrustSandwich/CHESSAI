# Library Imports
from selenium import webdriver
import time
import re



###############################################################################################################################################################
# Webscraper
###############################################################################################################################################################

class webScraper:

    def __init__(self):

        self.playerColor = ""
        self.gameURL = ""
        self.webPage = None

        self.currentBoard = [["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"]]

        

    # Opens a chrome web page instance of the game
    def openWebPage(self):

        # Create ChromeOptions to prevent it from displaying the webpage GUI
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--headless")

        # Create a new instance of the Chrome browser
        self.webPage = webdriver.Chrome(options=chromeOptions)

        # Navigate to a website
        self.webPage.get(self.gameURL)

        # Wait 3 seconds for page to load and retrieve most recent data
        time.sleep(5)

    # Returns the webpage html content
    def getWebPageContent(self):
        return self.webPage.page_source
    

    # Updates the player color
    def updatePlayerColor(self, color):
        self.playerColor = color

    # Updates the game URL
    def updateGameURL(self, url):
        self.gameURL = url

    # Returns the player color
    def getPlayerColor(self):
        return self.playerColor

    # Finds the occurences of the pieces present
    def findAllOccurrences(self, text, searchSubstring):
        occurrences = []
        index = text.find(searchSubstring)

        while index != -1:
            occurrences.append(index)
            index = text.find(searchSubstring, index + 1)

        return occurrences


    # Returns the popluated piece locations of a chess.com game
    def updateCurrentBoard(self):

        # Retrives the webpage content
        htmlContent = self.getWebPageContent()
        
        # Seaches for this string which refers to populated pieces on the board
        searchSubstring = '<div class="piece '

        allOccurrences = self.findAllOccurrences(htmlContent, searchSubstring)

        # Processes the html content and returns it as a tuple of pieces and repective index postions on an 8x8 board
        pieceLocations = []

        for pieceIndex in allOccurrences:

            pieceType = htmlContent[pieceIndex+18:pieceIndex+20]
            
            preprocessedLocation = htmlContent[pieceIndex+28:pieceIndex+30]
            

            firstNumber = int(preprocessedLocation[0])-1
            secondNumber = int(preprocessedLocation[1])-1

            pieceLocations.append((pieceType,(firstNumber,secondNumber)))
                
        
        # adds rendered pieces
        if self.playerColor == "w":
            for piece in pieceLocations:

                color = piece[0][0]

                if color == "w":
                    pre = ""
                else:
                    pre = "o"
                
                newPiece = pre + piece[0][1]

                self.currentBoard[piece[1][1]][piece[1][0]]  = newPiece

            self.currentBoard = [row[::-1] for row in self.currentBoard[::-1]]


        else:

            for piece in pieceLocations:

                color = piece[0][0]

                if color == "b":
                    pre = ""
                else:
                    pre = "o"
                
                newPiece = pre + piece[0][1]

                self.currentBoard[piece[1][1]][piece[1][0]]  = newPiece


        # To maintain similar numbering between sides, numbered backwards for opponennt side because their side is mirrored
        opCounter = 8
        pCounter = 1
        bCounter = 1
        obCounter = 2
        rCounter = 1
        orCounter = 2
        nCounter = 1
        onCounter = 2

        # Adds Numbers to rendered pieces on currentboard
        for i in range(len(self.currentBoard)):
            for j in range(len(self.currentBoard[i])):

                if self.currentBoard[i][j] == "op":
                    self.currentBoard[i][j] =  self.currentBoard[i][j]+str(opCounter)
                    opCounter-=1
                
                if self.currentBoard[i][j] == "ob":
                    self.currentBoard[i][j] = self.currentBoard[i][j]+str(obCounter)
                    obCounter-=1
                
                if self.currentBoard[i][j] == "on":
                    self.currentBoard[i][j] = self.currentBoard[i][j]+str(onCounter)
                    onCounter-=1

                if self.currentBoard[i][j] == "or":
                    self.currentBoard[i][j] = self.currentBoard[i][j]+str(orCounter)
                    orCounter-=1


                if self.currentBoard[i][j] == "p":
                    self.currentBoard[i][j] = self.currentBoard[i][j]+str(pCounter)
                    pCounter+=1
                
                if self.currentBoard[i][j] == "b":
                    self.currentBoard[i][j] = self.currentBoard[i][j]+str(bCounter)
                    bCounter+=1
                
                if self.currentBoard[i][j] == "n":
                    self.currentBoard[i][j] = self.currentBoard[i][j]+str(nCounter)
                    nCounter+=1

                if self.currentBoard[i][j] == "r":
                    self.currentBoard[i][j] = self.currentBoard[i][j]+str(rCounter)
                    rCounter+=1

    def getCurrentBoard(self):
        return self.currentBoard

        
###############################################################################################################################################################

"""
new = webScraper()

new.updateGameURL("https://www.chess.com/game/daily/585819547")
new.updatePlayerColor("w")
new.openWebPage()
new.updateCurrentBoard()
print(new.getCurrentBoard())
"""