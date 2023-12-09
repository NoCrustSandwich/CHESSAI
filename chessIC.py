import copy
import time
import pyautogui
from typing import List

###############################################################################################################################################################
# Chess.com Interface Controller - Version 1.4 (9/12/2023)
###############################################################################################################################################################

class controller:
    """
    Controller class for automating interactions with the Chess.com interface.

    Attributes:
        - board_tile_display_coordinates: List to store the calibrated coordinates of each chessboard tile.
        - COORDINATES_TO_TILE_INDICES_WHITE_PERSPECTIVE: Dictonary representing the indices for each chessboard tile coordinates from the white perspective.
        - COORDINATES_TO_TILE_INDICES_BLACK_PERSPECTIVE: Dictonary representing the indices for each chessboard tile coordinates from the black perspective.

    Methods:
        - __init__(self): Initializes the Chessboard Controller class.
        - get_mouse_coordinates(): Returns the x and y coordinates of the current mouse position.
        - get_board_tile_display_coordinates(): Returns the calibrated chessboard tile coordinates.
        - tile_coordinates_to_white_board_indices(coordinates): Converts coordinates to chessboard indices from the white perspective.
        - tile_coordinates_to_black_board_indices(coordinates): Converts coordinates to chessboard indices from the black perspective.
        - calibrate_board_tile_display_coordinates(): Calibrates and stores the coordinates of each chessboard tile.
        - move_piece_on_board(startAddressIndex, endAddressIndex): Moves a chess piece from the source to target tile on the Chess.com interface.

    Usage:
        - Create an instance of the Controller class.
        - Calibrate the board using calibrate_board_tile_display_coordinates().
        - Use tile_coordinates_to_white_board_indices() to translate tile coordinates to indices 
        - Use move_piece_on_board() to automate chess piece movements.

    Example:
        - chessIC = Controller()
        - chessIC.calibrate_board_tile_display_coordinates()
        - source_tile_indices = chessIC.tile_coordinates_to_white_board_indices("e2")
        - target_tile_indices = chessIC.tile_coordinates_to_white_board_indices("e4")
        - chessIC.move_piece_on_board(source_tile_indices, target_tile_indices)
        """

    def __init__(self):
        """
        Initializes the Chessboard Controller class.
        """
        self.board_tile_display_coordinates = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                               [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                               [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                               [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                               [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                               [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                               [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                                               [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]]
        self.COORDINATES_TO_TILE_INDICES_WHITE_PERSPECTIVE = {
            "a8":[0,0], "b8":[0,1], "c8":[0,2], "d8":[0,3], "e8":[0,4], "f8":[0,5], "g8":[0,6], "h8":[0,7],
            "a7":[1,0], "b7":[1,1], "c7":[1,2], "d7":[1,3], "e7":[1,4], "f7":[1,5], "g7":[1,6], "h7":[1,7],
            "a6":[2,0], "b6":[2,1], "c6":[2,2], "d6":[2,3], "e6":[2,4], "f6":[2,5], "g6":[2,6], "h6":[2,7],
            "a5":[3,0], "b5":[3,1], "c5":[3,2], "d5":[3,3], "e5":[3,4], "f5":[3,5], "g5":[3,6], "h5":[3,7],
            "a4":[4,0], "b4":[4,1], "c4":[4,2], "d4":[4,3], "e4":[4,4], "f4":[4,5], "g4":[4,6], "h4":[4,7],
            "a3":[5,0], "b3":[5,1], "c3":[5,2], "d3":[5,3], "e3":[5,4], "f3":[5,5], "g3":[5,6], "h3":[5,7],
            "a2":[6,0], "b2":[6,1], "c2":[6,2], "d2":[6,3], "e2":[6,4], "f2":[6,5], "g2":[6,6], "h2":[6,7],
            "a1":[7,0], "b1":[7,1], "c1":[7,2], "d1":[7,3], "e1":[7,4], "f1":[7,5], "g1":[7,6], "h1":[7,7],
        }
        self.COORDINATES_TO_TILE_INDICES_BLACK_PERSPECTIVE = {
            "h1":[0,0], "g1":[0,1], "f1":[0,2], "e1":[0,3], "d1":[0,4], "c1":[0,5], "b1":[0,6], "a1":[0,7],
            "h2":[1,0], "g2":[1,1], "f2":[1,2], "e2":[1,3], "d2":[1,4], "c2":[1,5], "b2":[1,6], "a2":[1,7],
            "h3":[2,0], "g3":[2,1], "f3":[2,2], "e3":[2,3], "d3":[2,4], "c3":[2,5], "b3":[2,6], "a3":[2,7],
            "h4":[3,0], "g4":[3,1], "f4":[3,2], "e4":[3,3], "d4":[3,4], "c4":[3,5], "b4":[3,6], "a4":[3,7],
            "h5":[4,0], "g5":[4,1], "f5":[4,2], "e5":[4,3], "d5":[4,4], "c5":[4,5], "b5":[4,6], "a5":[4,7],
            "h6":[5,0], "g6":[5,1], "f6":[5,2], "e6":[5,3], "d6":[5,4], "c6":[5,5], "b6":[5,6], "a6":[5,7],
            "h7":[6,0], "g7":[6,1], "f7":[6,2], "e7":[6,3], "d7":[6,4], "c7":[6,5], "b7":[6,6], "a7":[6,7],
            "h8":[7,0], "g8":[7,1], "f8":[7,2], "e8":[7,3], "d8":[7,4], "c8":[7,5], "b8":[7,6], "a8":[7,7],
        }

    
    def get_mouse_coordinates(self) -> List[int]:
        """
        Retrieves the current x and y coordinates of the mouse cursor.

        Returns:
            - List[int, int]: A list containing the x and y coordinates of the mouse cursor.
        """
        click_point = pyautogui.position()
        x, y = click_point

        return [x, y]


    def get_board_tile_display_coordinates(self) -> List[List[int]] :
        """
        Retrieves the calibrated coordinates of each chessboard tile.

        Returns:
            - List[List[int]]: A list representing the calibrated coordinates of each chessboard tile.
        """
        return self.board_tile_display_coordinates


    def tile_coordinates_to_white_board_indices(self, tile_coordinates: str) -> List[int]:
        """
        Converts chessboard tile coordinates to indices from the white perspective.

        Parameters:
            - tile_coordinates (str): A string representing the coordinates of a chessboard tile.

        Returns:
            - List[int]: The corresponding chessboard indices from the white perspective.
        """
        return self.COORDINATES_TO_TILE_INDICES_WHITE_PERSPECTIVE[tile_coordinates]


    def tile_coordinates_to_black_board_indices(self, tile_coordinates: str) -> List[int]:
        """
        Converts chessboard tile coordinates to indices from the black perspective.

        Parameters:
            - tile_coordinates (str): A string representing the coordinates of a chessboard tile.

        Returns:
            - List[int]: The corresponding chessboard indices from the black perspective.
        """
        return self.COORDINATES_TO_TILE_INDICES_BLACK_PERSPECTIVE[tile_coordinates]


    def calibrate_board_tile_display_coordinates(self):
        """
        Initiates the calibration process for obtaining the display coordinates of each chessboard tile.

        During calibration, the user is prompted to place the mouse pointer in the center of TILE 1, TILE 2, and TILE 9
        in that order. The method captures the mouse coordinates at each position and calculates the block lengths
        to populate the calibrated coordinates for each chessboard tile.

        This method guides the user through the calibration process and populates the calibrated coordinates of each chessboard tile.
        The calibrated coordinates are stored in the `board_tile_display_coordinates` attribute.

        Note:
        - Follow the on-screen instructions during calibration.
        - The method uses the `get_mouse_coordinates` method to capture mouse positions.
        - Ensure that the chessboard is visible on the screen during calibration.
        - Adjust the sleep durations as needed based on the user's responsiveness.
        """
        print("------------------------------------------------------------------------------------------")
        print("\n")
        print("Imagine the chess board tiles are numbered as shown here:")
        print("\n")
        print("| 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  |")
        print("| 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 |")
        print("| 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |")
        print("| 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 |")
        print("| 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |")
        print("| 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 |")
        print("| 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 |")
        print("| 57 | 58 | 59 | 60 | 61 | 62 | 63 | 64 |")
        print("\n")
        print("For calibration leave your mouse pointer in the CENTER of \nTILE 1, then TILE 2 and then TILE 9\n\n*IN THAT ORDER*")
        print("\n")
        print("You will be given 5 seconds each time to get your mouse into postion")
        print("\n")
        print("------------------------------------------------------------------------------------------")
        print("\n")
        input("PRESS ENTER TO BEGIN BOARD CALIBRATION")
        print("\n")

        display_calibration_points = []

        for i in range(3):

            for j in range(5):
                time.sleep(1)
                print(str(5-j) +"...")

            display_calibration_points.append((self.get_mouse_coordinates()))
            
            if i<2:
                print("Tile "+str(i+1)+" Coordinates captured at: "+ str(self.get_mouse_coordinates()))
            else:
                print("Tile "+str(9)+" Coordinates captured at: "+ str(self.get_mouse_coordinates()))

        column_Length = display_calibration_points[1][0] - display_calibration_points[0][0] # Calculates block lengths to interpolate the rest of the tile's coordinates
        row_Length = display_calibration_points[2][1] - display_calibration_points[0][1]


        current_coordinates = copy.deepcopy(display_calibration_points[0])
        
        for row in range(8):
            for col in range(8):    
                self.board_tile_display_coordinates[row][col] = copy.deepcopy(current_coordinates)
                current_coordinates[0] += column_Length

            current_coordinates = self.board_tile_display_coordinates[0][0]
            current_coordinates[1] += row_Length
        

    def execute_action(self, action, board):
        """
        Executes the given action on the screen.

        Parameters:
            - action, (Tuple): A tuple representing the action to be taken.
            - board, (List[List[str]]): A 2d list representing the current chessboard state.

        Returns:
            - None
        """
        for i in range(8):
            for j in range(8):
                if board[i][j] == action[0]:
                    source_tile = [i,j]

        target_tile = [source_tile[0]+action[1][0], source_tile[1]+action[1][1]]

        if len(action) == 3:
            self.move_piece_on_board(source_tile, target_tile, action[2])
        else:
            self.move_piece_on_board(source_tile, target_tile, None)


    def move_piece_on_board(self, source_tile_indices, target_tile_indices, promotion_piece):
        """
        Moves a chess piece from the source location to the target location on the Chess.com game Board.

        Parameters:
            - source_tile_indices, (List[int,int]): A list representing the row and column indices of the source chessboard tile location.
            - target_tile_indices, (List[int,int]): A list representing the row and column indices of the target chessboard tile location.

        Note:
            - Adjust the sleep durations as needed based on the responsiveness of the Chess.com interface.
            - The final line moves the mouse back to a neutral position (1, 1, 1) to avoid unintended actions.
        """
        print(self.board_tile_display_coordinates)
        print(source_tile_indices)
        print(target_tile_indices)

        x, y = self.board_tile_display_coordinates[source_tile_indices[0]][source_tile_indices[1]]
        pyautogui.moveTo(x, y, 1)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(1)

        x, y = self.board_tile_display_coordinates[target_tile_indices[0]][target_tile_indices[1]]
        pyautogui.moveTo(x, y, 1)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(1)

        if promotion_piece == "q":
            x, y = self.board_tile_display_coordinates[target_tile_indices[0]][target_tile_indices[1]]
        elif promotion_piece == "n":
            x, y = self.board_tile_display_coordinates[target_tile_indices[0]+1][target_tile_indices[1]]
        elif promotion_piece == "r":
            x, y = self.board_tile_display_coordinates[target_tile_indices[0]+2][target_tile_indices[1]]
        elif promotion_piece == "b":
            x, y = self.board_tile_display_coordinates[target_tile_indices[0]+3][target_tile_indices[1]]
        else:
            pyautogui.moveTo(1, 1, 1)
            return

        pyautogui.moveTo(x, y, 1)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()

        pyautogui.moveTo(1, 1, 1)

###############################################################################################################################################################
