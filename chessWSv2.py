# Library Imports
from selenium import webdriver
import time
from typing import List, Dict




###############################################################################################################################################################
# Webscraper
###############################################################################################################################################################

class webScraper:
    """
    A class representing a web scraper for extracting the latest game data from a chess.com game session

    Attributes:
    - gamer_url (str): The url of the game session.
    - web_page (WebDriver): The hidden chrome web page instance of the chess.com game session.
    - move_history (List[str]): The latest move history of the game session.
    - OPPONENT_PERSPECTIVE_PIECE_LABELS (Dict[str, str]): The dictionary used to translate board piece labels to opposing player's perspective.

    Methods:
    - __init__(self): Initializes the Web Scraper with the OPPONENT_PERSPECTIVE_PIECE_LABELS dictionary.
    - update_game_url(self, url): Updates the game_url attribute with the one of the desired game session.
    - initialize_web_page(self): Initializes the hidden Chrome web page instance for web scraping.
    - get_web_page_content(self) -> str: Retrieves the HTML content of the current web page.
    - reverse_board_perspective(self, board: List[str]) -> List[str]: Reverses the board perspective to that of the opposite player's.
    - 

    """


    def __init__(self):
        """
        Initializes the WebScraper with the OPPONENT_PERSPECTIVE_PIECE_LABELS dictionary.
        """
        self.game_url = ""
        self.web_page = None
        self.move_history = []

        self.OPPONENT_PERSPECTIVE_PIECE_LABELS = {

            "_":"_",
            "p1": "op1", "p2": "op2", "p3": "op3", "p4": "op4", "p5": "op5", "p6": "op6", "p7": "op7", "p8": "op8",
            "n1": "on1", "n2": "on2", "n3": "on3", "n4": "on4", "n5": "on5", "n6": "on6", "n7": "on7", "n8": "on8", "n9": "on9", "n10": "on10",
            "b1": "ob1", "b2": "ob2", "b3": "ob3", "b4": "ob4", "b5": "ob5", "b6": "ob6", "b7": "ob7", "b8": "ob8", "b9": "ob9", "b10": "ob10",
            "r1": "or1", "r2": "or2", "r3": "or3", "r4": "or4", "r5": "or5", "r6": "or6", "r7": "or7", "r8": "or8", "r9": "or9", "r10": "or10",
            "q1": "oq1", "q2": "oq2", "q3": "oq3", "q4": "oq4", "q5": "oq5", "q6": "oq6", "q7": "oq7", "q8": "oq8", "q9": "oq9",
            "k": "ok",

        }


    def update_game_url(self, url):
        """
        Updates the game_url attribute with the URL of the desired game session.

        Parameters:
        - url (str): The URL of the desired Chess.com game session.
        """
        self.game_url = url


    def initialize_web_page(self):
        """
        Initializes the hidden Chrome web page instance for web scraping.
        """
        # Hides the chrome web page
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")

        self.web_page = webdriver.Chrome(options=chrome_options)

        # Navigates to game url webpage
        self.web_page.get(self.game_url)

        # Wait 5 seconds for page to load and retrieve most recent data
        time.sleep(5)


    def get_web_page_content(self) -> str:
        """
        Retrieves the HTML content of the current web page.

        Returns:
        str: The HTML content of the web page as a string.
        """
        return self.web_page.page_source
    

    def reverse_board_perspective(self, board: List[str]) -> List[str]:
        """
        Reverses the board perspective to that of the opposite player's.

        Parameters:
        - board (List[str]): The chessboard from the white player's perspective.

        Returns:
        List[str]: The reversed board state, reflecting the opposite player's perspective.
        """
        # Rotates the board 180 degrees
        board = [row[::-1] for row in board[::-1]]

        # Changes piece labels to reflect the opponent's perspective
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = self.OPPONENT_PERSPECTIVE_PIECE_LABELS[board[i][j]]
        
        return board


    # Returns the piece locations of the current chess.com game page
    def get_move_history(self):

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

    # Returns occurences of the pieces present
    def findAllOccurrences(self, text, searchSubstring):
        occurrences = []
        index = text.find(searchSubstring)

        while index != -1:
            occurrences.append(index)
            index = text.find(searchSubstring, index + 1)

        return occurrences            

    # Renders the pieces stored in currentPieceLocations from whites persepctive and returns it as a 2d array
    def render_white_board_perspective(self):

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


new = webScraper()
new.update_game_url("https://www.chess.com/game/daily/583143785")
new.initialize_web_page()
print(new.get_web_page_content())