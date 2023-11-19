# Library Imports
from selenium import webdriver
import time
import re



###############################################################################################################################################################
# Webscraper
###############################################################################################################################################################

class webScraper:

    def __init__(self):

        self.gameURL = ""
        self.webPage = None

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


    # Opens a chrome web page instance of the game in the background
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


    # Updates the game URL
    def updateGameURL(self, url):
        self.gameURL = url

    # Returns the webpage html content
    def getWebPageContent(self):
        return self.webPage.page_source
    

    # Finds the occurences of the pieces present
    def findAllOccurrences(self, text, searchSubstring):
        occurrences = []
        index = text.find(searchSubstring)

        while index != -1:
            occurrences.append(index)
            index = text.find(searchSubstring, index + 1)

        return occurrences


    # Returns a reversed board side to play from the oppostive perspective
    def switchPlayer(self, board):
        
        # Rotates board 180 degrees
        board = [row[::-1] for row in board[::-1]]

        # Changes piece labels
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = self.playerChanger[board[i][j]]
        
        return board


    # Returns the piece locations of the current chess.com game page
    def getPieceLocations(self):

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
            

            col = int(preprocessedLocation[0])-1
            row = abs(int(preprocessedLocation[1])-8)

            pieceLocations.append((pieceType,(row,col)))

        return pieceLocations
                

    # Renders the pieces stored in currentPieceLocations from whites persepctive and returns it as a 2d array
    def renderBoardWhite(self, pieceLocations):

        # Initializes board as empty before rendering
        currentBoard = [["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"]]


         # Renders pieces from white's perscpective
        for piece in pieceLocations:

            color = piece[0][0]

            if color == "w":
                pre = ""
            else:
                pre = "o"
            
            newPiece = pre + piece[0][1]

            currentBoard[piece[1][0]][piece[1][1]]  = newPiece


        # To maintain similar numbering between sides, numbered backwards for opponennt side because their side is mirrored
        opCounter = 8
        pCounter = 1
        bCounter = 1
        obCounter = 2
        rCounter = 1
        orCounter = 2
        nCounter = 1
        onCounter = 2

        # Numbers rendered pieces on currentboard
        for i in range(len(currentBoard)):
            for j in range(len(currentBoard[i])):

                if currentBoard[i][j] == "op":
                    currentBoard[i][j] =  currentBoard[i][j]+str(opCounter)
                    opCounter-=1
                
                if currentBoard[i][j] == "ob":
                    currentBoard[i][j] = currentBoard[i][j]+str(obCounter)
                    obCounter-=1
                
                if currentBoard[i][j] == "on":
                    currentBoard[i][j] = currentBoard[i][j]+str(onCounter)
                    onCounter-=1

                if currentBoard[i][j] == "or":
                    currentBoard[i][j] = currentBoard[i][j]+str(orCounter)
                    orCounter-=1


                if currentBoard[i][j] == "p":
                    currentBoard[i][j] = currentBoard[i][j]+str(pCounter)
                    pCounter+=1
                
                if currentBoard[i][j] == "b":
                    currentBoard[i][j] = currentBoard[i][j]+str(bCounter)
                    bCounter+=1
                
                if currentBoard[i][j] == "n":
                    currentBoard[i][j] = currentBoard[i][j]+str(nCounter)
                    nCounter+=1

                if currentBoard[i][j] == "r":
                    currentBoard[i][j] = currentBoard[i][j]+str(rCounter)
                    rCounter+=1

        return currentBoard
    

    # Renders the pieces stored in currentPieceLocations from whites persepctive and returns it as a 2d array
    def renderBoardBlack(self, pieceLocations):

        # Renders pieces from white's perspective and then switches player perspective
        return self.switchPlayer(self.renderBoardWhite(pieceLocations))


        
###############################################################################################################################################################
