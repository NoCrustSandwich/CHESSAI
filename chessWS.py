# Library Imports
import time
from typing import Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By



###############################################################################################################################################################
# Web Scraper - Version 2.0 (21/11/2023) 
###############################################################################################################################################################

class webScraper:
    """
    A class representing a web scraper for extracting the latest game data from a chess.com game session

    Attributes:
        - gamer_url (str): The url of the game session.
        - web_page (WebDriver): The hidden chrome web page instance of the chess.com game session.

    Methods:
        - __init__(self): Initializes the Web Scraper class.
        - update_game_url(self, url): Updates the game_url attribute with the one of the desired game session.
        - fetch_latest_move_history_san(self) -> Tuple[int, str, str]: Retrieves the latest move history of the current Chess.com game session in Standard Algebraic Notation.

    Usage Example:
        - chessWS = webScraper()
        - chessWS.update_game_url("https://www.chess.com/game/daily/583143785")
        - chessWS.initialize_web_page()
        - latest_move_history_san = chessWS.fetch_latest_move_history_san()
    """
    
    def __init__(self):
        """
        Initializes the WebScraper class.
        """
        self.game_url = ""
        self.web_page = None
        

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
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")   # Hides the chrome web page

        self.web_page = webdriver.Chrome(options=chrome_options)

        self.web_page.get(self.game_url)    # Navigates to game url webpage

        time.sleep(5)   # Wait 5 seconds for page to load and retrieve most recent data

    
    def fetch_latest_move_history_san(self) -> Tuple[int, str, str]:
        """
        Retrieves the move history of the current Chess.com game session in Standard Algebraic Notation.

        Returns:
            - Tuple[int, str, str]: The history of moves in the game session.
        """
        div_class = 'move'
        div_elements = self.web_page.find_elements(By.CLASS_NAME, div_class)

        latest_move_history = []
        
        for index, div_element in enumerate(div_elements, 1):
            div_content = div_element.text
            seperated_moves = div_content.split("\n")

            latest_move_history.append((index,seperated_moves[1],seperated_moves[2]))
        
        return latest_move_history

###############################################################################################################################################################


