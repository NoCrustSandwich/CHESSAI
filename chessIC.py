# Library Imports
import time
import pyautogui
from typing import List

###############################################################################################################################################################
# Chess.com Interface Controller - Version 1.1 (21/11/2023)
###############################################################################################################################################################

class controller:
    """
    Controller class for automating interactions with the Chess.com interface.

    Attributes:
        - board_tile_display_coordinates: List to store the calibrated coordinates of each chessboard tile.
        - CHESSBOARD_TILE_COORDINATES_WHITE_PERSPECTIVE: 2D list representing the chessboard coordinates from the white perspective.
        - CHESSBOARD_TILE_COORDINATES_BLACK_PERSPECTIVE: 2D list representing the chessboard coordinates from the black perspective.

    Methods:
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
        - source_tile_indices = chessIC.tile_coordinates_to_white_board_indices("E2")
        - target_tile_indices = chessIC.tile_coordinates_to_white_board_indices("E4")
        - chessIC.move_piece_on_board(source_tile_indices, target_tile_indices)
        """


    def __init__(self):
        """
        Initializes the Chessboard Controller class.

        Attributes:
            - board_tile_display_coordinates: The variable to store calibrated coordinates of each chessboard tile.
            It is initialized to None and is intended to be populated during calibration.
            - CHESSBOARD_TILE_COORDINATES_WHITE_PERSPECTIVE: 2D list representing the chessboard coordinates from the white perspective.
            The indices represent the row and column, and the values represent the chessboard coordinates.
            - CHESSBOARD_TILE_COORDINATES_BLACK_PERSPECTIVE: 2D list representing the chessboard coordinates from the black perspective.
            Similar to the white perspective, the indices represent the row and column, and the values represent the chessboard coordinates.
        """
        self.board_tile_display_coordinates = None
        self.CHESSBOARD_TILE_COORDINATES_WHITE_PERSPECTIVE = [
                ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"],
                ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
                ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
                ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
                ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
                ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H4"],
                ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
                ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]
            ]
        self.CHESSBOARD_TILE_COORDINATES_BLACK_PERSPECTIVE = [
            ["H1", "G1", "F1", "E1", "D1", "C1", "B1", "A1"],
            ["H2", "G2", "F2", "E2", "D2", "C2", "B2", "A2"],
            ["H3", "G3", "F3", "E3", "D3", "C3", "B3", "A3"],
            ["H4", "G4", "F4", "E4", "D4", "C4", "B4", "A4"],
            ["H5", "G5", "F5", "E5", "D5", "C5", "B5", "A5"],
            ["H6", "G6", "F6", "E6", "D6", "C6", "B6", "A6"],
            ["H7", "G7", "F7", "E7", "D7", "C7", "B7", "A7"],
            ["H8", "G8", "F8", "E8", "D8", "C8", "B8", "A8"]
        ]

    
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
        for x in range(8):
            for y in range(8):
                if tile_coordinates.upper() == self.CHESSBOARD_TILE_COORDINATES_WHITE_PERSPECTIVE[x][y]:
                    return[x,y]


    def tile_coordinates_to_black_board_indices(self, tile_coordinates: str) -> List[int]:
        """
        Converts chessboard tile coordinates to indices from the black perspective.

        Parameters:
            - tile_coordinates (str): A string representing the coordinates of a chessboard tile.

        Returns:
            - List[int]: The corresponding chessboard indices from the black perspective.
        """
        for x in range(8):
            for y in range(8):
                if tile_coordinates.upper() == self.CHESSBOARD_TILE_COORDINATES_BLACK_PERSPECTIVE[x][y]:
                    return[x,y]


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

            display_calibration_points.append(self.get_mouse_coordinates())

            if i<2:
                print("Tile "+str(i+1)+" Coordinates captured at: "+ str(self.get_mouse_coordinates()))
            else:
                print("Tile "+str(9)+" Coordinates captured at: "+ str(self.get_mouse_coordinates()))

        # Calculates block lengths to interpolate the rest of the tile's coordinates 
        column_Length = display_calibration_points[1][0] - display_calibration_points[0][0]
        row_Length = display_calibration_points[2][1] - display_calibration_points[0][1]

        current_coordinates = display_calibration_points[0].copy()
        for x in range(8):
            for y in range(8):    
                self.board_tile_display_coordinates[x][y] = current_coordinates.copy()
                current_coordinates[0] += column_Length

            current_coordinates[0] = self.board_tile_display_coordinates[0][0]
            current_coordinates[1] += row_Length
        

    def move_piece_on_board(self, source_tile_indices, target_tile_indices):
        """
        Moves a chess piece from the source location to the target location on the Chess.com game Board.

        Parameters:
            - source_tile_indices, (List[int,int]): A list representing the row and column indices of the source chessboard tile location.
            - target_tile_indices, (List[int,int]): A list representing the row and column indices of the target chessboard tile location.

        Note:
            - Adjust the sleep durations as needed based on the responsiveness of the Chess.com interface.
            - The final line moves the mouse back to a neutral position (1, 1, 1) to avoid unintended actions.
        """
        x, y = self.board_tile_display_coordinates[source_tile_indices[0],source_tile_indices[1]]

        pyautogui.moveTo(x, y, 1)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(1)

        x, y = self.board_tile_display_coordinates[target_tile_indices[0],target_tile_indices[1]]

        pyautogui.moveTo(x, y, 1)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()

        pyautogui.moveTo(1, 1, 1)

###############################################################################################################################################################