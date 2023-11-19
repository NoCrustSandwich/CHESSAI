# Library Imports
import pyautogui
import time

###############################################################################################################################################################
# Chess.com controller for AI
###############################################################################################################################################################

class controller:

    def __init__(self):
        
        self.calibrated_Board_Coordinates = [
            [[350, 230], [450, 230], [550, 230], [650, 230], [750, 230], [850, 230], [950, 230], [1050, 230]],
            [[350, 330], [450, 330], [550, 330], [650, 330], [750, 330], [850, 330], [950, 330], [1050, 330]],
            [[350, 430], [450, 430], [550, 430], [650, 430], [750, 430], [850, 430], [950, 430], [1050, 430]],
            [[350, 530], [450, 530], [550, 530], [650, 530], [750, 530], [850, 530], [950, 530], [1050, 530]],
            [[350, 630], [450, 630], [550, 630], [650, 630], [750, 630], [850, 630], [950, 630], [1050, 630]],
            [[350, 730], [450, 730], [550, 730], [650, 730], [750, 730], [850, 730], [950, 730], [1050, 730]],
            [[350, 830], [450, 830], [550, 830], [650, 830], [750, 830], [850, 830], [950, 830], [1050, 830]],
            [[350, 930], [450, 930], [550, 930], [650, 930], [750, 930], [850, 930], [950, 930], [1050, 930]]
        ]

        self.board_Calibration_Coordinates = []

        # Coordinates translated to chess format that will correlate with the display coordinates, if you are playing white
        self.chessBoardTranslatedWhiteCoordinates = [
                ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"],
                ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
                ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
                ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
                ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
                ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H4"],
                ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
                ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]
            ]

        # Coordinates translated to chess format that will correlate with the display coordinates, if you are playing black
        self.chessBoardTranslatedBlackCoordinates = [
            ["H1", "G1", "F1", "E1", "D1", "C1", "B1", "A1"],
            ["H2", "G2", "F2", "E2", "D2", "C2", "B2", "A2"],
            ["H3", "G3", "F3", "E3", "D3", "C3", "B3", "A3"],
            ["H4", "G4", "F4", "E4", "D4", "C4", "B4", "A4"],
            ["H5", "G5", "F5", "E5", "D5", "C5", "B5", "A5"],
            ["H6", "G6", "F6", "E6", "D6", "C6", "B6", "A6"],
            ["H7", "G7", "F7", "E7", "D7", "C7", "B7", "A7"],
            ["H8", "G8", "F8", "E8", "D8", "C8", "B8", "A8"]
        ]
    
    # Returns the x and y coordinates on button click
    def get_Mouse_Coordinates(self):
        # Wait for a mouse click
        click_point = pyautogui.position()

        # Get the coordinates where the click occurred
        x, y = click_point

        return [x, y]

    # Calibrates board coordinates
    def calibrate_Board(self):

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

        # Resets the board calibration points
        self.board_Calibration_Coordinates = []

        # Gets the 3 board coordinate locations for calibration, in 5 second intervals
        for i in range(3):

            for j in range(5):
                time.sleep(1)
                print(str(5-j) +"...")

            self.board_Calibration_Coordinates.append(self.get_Mouse_Coordinates())

            if i<2:
                print("Tile "+str(i+1)+" Coordinates captured at: "+ str(self.get_Mouse_Coordinates()))
            else:
                print("Tile "+str(9)+" Coordinates captured at: "+ str(self.get_Mouse_Coordinates()))

        # Calculates block lengths
        column_Length = self.board_Calibration_Coordinates[1][0] - self.board_Calibration_Coordinates[0][0]
        row_Length = self.board_Calibration_Coordinates[2][1] - self.board_Calibration_Coordinates[0][1]

        current_Coordinates = self.board_Calibration_Coordinates[0].copy()

        # Populates the calibrated coordinates
        for x in range(8):

            for y in range(8):    
                self.calibrated_Board_Coordinates[x][y] = current_Coordinates.copy()
                current_Coordinates[0] += column_Length

            current_Coordinates[0] = self.board_Calibration_Coordinates[0][0]
            current_Coordinates[1] += row_Length
        
        return True

    # Returns the current calibrated Coords
    def get_Current_Calibrated_Coords(self):
        return self.calibrated_Board_Coordinates

    # Returns the board coordinates if player color is white
    def getWhiteCoords(self, index):
        return self.chessBoardTranslatedWhiteCoordinates[index[0]][index[1]]

    # Returns the board coordinates if player color is white
    def getBlackCoords(self, index):
        return self.chessBoardTranslatedBlackCoordinates[index[0]][index[1]]

    # Moves piece from initial location to the end location on the chess.com gamerBoard
    def movePieceExternally(self, startAddressIndex, endAddressIndex):

        x, y = self.calibrated_Board_Coordinates(startAddressIndex[0],startAddressIndex[1])

        pyautogui.moveTo(x, y, 1)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()
        time.sleep(1)

        x, y = self.calibrated_Board_Coordinates(endAddressIndex[0],endAddressIndex[1])

        pyautogui.moveTo(x, y, 1)
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.mouseUp()

        # Moves mouse back to neutral position
        pyautogui.moveTo(1300, 1000, 1)

###############################################################################################################################################################