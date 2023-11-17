# Library Imports
import requests
import re



###############################################################################################################################################################
# Chess.com chessboard webscraper
###############################################################################################################################################################

class webscaper:

    def __init__(self):

        self.playerColor = ""
        self.gameURL = ""

        self.currentBoard = [["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"]]

        self.percentToIndex = {
            '0':0,
            '14.29%':1,
            '28.57%':2,
            '42.86%':3,
            '57.14%':4,
            '71.43%':5,
            '85.71%':6,
            '100%':7

        }

    # Updates the player color
    def updatePlayerColor(self, color):
        self.playerColor = color

    # Updates the game URL
    def updateGameURL(self, url):
        self.gameURL = url

    # Returns the player color
    def getPlayerColor(self):
        return self.playerColor

    # Returns the popluated piece locations of a chess.com game
    def updateCurrentBoard(self):

        response = requests.get(self.gameURL)

        # http request to chess.com
        if response.status_code == 200:
            htmlContent = response.text
        else:
            print("Failed to retrieve the game page.")

        
        # Finds the occurences of the pieces present
        def findAllOccurrences(text, searchSubstring):
            occurrences = []
            index = text.find(searchSubstring)

            while index != -1:
                occurrences.append(index)
                index = text.find(searchSubstring, index + 1)

            return occurrences


        # Seaches for this string which refers to populated pieces on the board
        searchSubstring = 'var(--theme-piece-set-'

        allOccurrences = findAllOccurrences(htmlContent, searchSubstring)
        
        


        # Processes the html content and returns it as a tuple of pieces and repective index postions on an 8x8 board
        pieceLocations = []

        for pieceIndex in allOccurrences:

            pieceType = htmlContent[pieceIndex+22:pieceIndex+24]

            preprocessedLocation = htmlContent[pieceIndex+112:pieceIndex+140]

            splitStrings =  re.split(' ', preprocessedLocation)

            firstNumber = splitStrings[0]
            secondNumber = splitStrings[1]

            pieceLocations.append((pieceType,(self.percentToIndex[firstNumber],self.percentToIndex[secondNumber])))
                
        
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

new = webscaper()
new.updateGameURL("https://www.chess.com/game/daily/585819547")
new.updatePlayerColor("b")
new.updateCurrentBoard()
print(new.getCurrentBoard())
