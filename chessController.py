# Imports
import pyautogui
import time
import cv2
import numpy as np






# b = Black, w = White
AI_Player_Color = ""

# Stores resolution of the display of the current device
display_Resolution = "1920x1080"

# Tile length for a resolution of 1920x1080 (in pixels)
tile_Length_1920x1080 = 85



# Keeps track of current state of the chessboard
# K = White King, Q = White Queen, B = White Bishop, N = White Knight, R = White Rook, P = White Pawn
# k = Black King, q = Black Queen, b = Black Bishop, n = Black Knight, r = Black Rook, p = Black Pawn
# Empty Tile = ""
current_Chess_Board_State = [

    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""]

    ]


# On screen coordinates for centre each tile of the chess board
# For full screen discord 1920x1080 resolution
discord_chess_Board_Coordinates_1920x1080 = [
        [[845, 190], [930, 190], [1015, 190], [1100, 190], [1185, 190], [1270, 190], [1355, 190], [1440, 190]],
        [[845, 275], [930, 275], [1015, 275], [1100, 275], [1185, 275], [1270, 275], [1355, 275], [1440, 275]],
        [[845, 360], [930, 360], [1015, 360], [1100, 360], [1185, 360], [1270, 360], [1355, 360], [1440, 360]],
        [[845, 445], [930, 445], [1015, 445], [1100, 445], [1185, 445], [1270, 445], [1355, 445], [1440, 445]],
        [[845, 530], [930, 530], [1015, 530], [1100, 530], [1185, 530], [1270, 530], [1355, 530], [1440, 530]],
        [[845, 615], [930, 615], [1015, 615], [1100, 615], [1185, 615], [1270, 615], [1355, 615], [1440, 615]],
        [[845, 700], [930, 700], [1015, 700], [1100, 700], [1185, 700], [1270, 700], [1355, 700], [1440, 700]],
        [[845, 785], [930, 785], [1015, 785], [1100, 785], [1185, 785], [1270, 785], [1355, 785], [1440, 785]]
    ]



chessdotcom_chess_Board_Coordinates_1920x1080 = [
        [[350, 240], [450, 240], [550, 240], [650, 240], [750, 240], [850, 240], [950, 240], [1050, 240]],
        [[350, 340], [450, 340], [550, 340], [650, 340], [750, 340], [850, 340], [950, 340], [1050, 340]],
        [[350, 440], [450, 440], [550, 440], [650, 440], [750, 440], [850, 440], [950, 440], [1050, 440]],
        [[350, 540], [450, 540], [550, 540], [650, 540], [750, 540], [850, 540], [950, 540], [1050, 540]],
        [[350, 640], [450, 640], [550, 640], [650, 640], [750, 640], [850, 640], [950, 640], [1050, 640]],
        [[350, 740], [450, 740], [550, 740], [650, 740], [750, 740], [850, 740], [950, 740], [1050, 740]],
        [[350, 840], [450, 840], [550, 840], [650, 840], [750, 840], [850, 840], [950, 840], [1050, 840]],
        [[350, 940], [450, 940], [550, 940], [650, 940], [750, 940], [850, 940], [950, 940], [1050, 940]],
    ]

# Returns the x y coordinates on button click
def get_mouse_coordinates(self):
    # Wait for a mouse click
    click_point = pyautogui.position()

    # Get the coordinates where the click occurred
    x, y = click_point

    return x, y

# Returns the coordinates of all the pieces of the type input present on the board
def getPieceLocations(image_path, threshold=0.99):

    # Load the template image
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Capture the screen content
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)

    # Match the template in the screenshot
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    # Find locations where the match score is above the threshold
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))  # Reverse to get (x, y) coordinates

    # Get the dimensions of the template image
    h, w, _ = template.shape

    # Convert the coordinates to a list of (x, y) tuples
    coordinates = [(loc[0] + w // 2, loc[1] + h // 2) for loc in locations]

    return coordinates

# Searches for the right position based on coordinates array
def addPiece(piece, chessBoard, coords):

    if coords == []:
        return chessBoard

    # Repeats for the amount of entries of coordinates
    for entry in coords:

        xPositionFound = False
        yPositionFound = False
        xPositionThreshold = 880
        yPositionThreshold = 200
        rowIndex = 0
        colIndex = 0

        # Loops until x position is found
        while not xPositionFound and colIndex < 8:

            if entry[0] <= xPositionThreshold:
                xPositionFound = True
            else:
                xPositionThreshold += 85
                colIndex += 1

        # Loops until x position is found
        while not yPositionFound and rowIndex < 8:

            if entry[1] <= yPositionThreshold:
                yPositionFound = True
            else:
                yPositionThreshold += 85
                rowIndex += 1

        # Adds piece to the board based on the location
        if xPositionFound and yPositionFound:
            chessBoard[rowIndex][colIndex] = piece

    print(chessBoard)

    return chessBoard


# Populates the game board
def populateBoard(chessBoard):

    thresh = 0.90
    # Populates the chess board based on pieces present on screen

    #Populates Black Pawns present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/black_Pawn_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("p", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Pawn_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("p", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Pawn_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("p", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Pawn_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("p", chessBoard, coordinates)


    #Populates Black Bishops present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/black_Bishop_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("b", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Bishop_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("b", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Bishop_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("b", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Bishop_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("b", chessBoard, coordinates)



    #Populates Black Rooks present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/black_Rook_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("r", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Rook_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("r", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Rook_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("r", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Rook_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("r", chessBoard, coordinates)



    #Populates Black Knights present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/black_Knight_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("n", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Knight_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("n", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Knight_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("n", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Knight_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("n", chessBoard, coordinates)


    #Populates Black Queens present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/black_Queen_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("q", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Queen_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("q", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Queen_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("q", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_Queen_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("q", chessBoard, coordinates)



    #Populates Black Kings present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/black_King_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("k", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_King_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("k", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_King_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("k", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/black_King_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("k", chessBoard, coordinates)


    #Populates White Pawns present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/white_Pawn_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("P", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Pawn_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("P", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Pawn_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("P", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Pawn_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("P", chessBoard, coordinates)


    #Populates White Bishops present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/white_Bishop_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("B", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Bishop_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("B", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Bishop_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("B", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Bishop_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("B", chessBoard, coordinates)



    #Populates White Rooks present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/white_Rook_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("R", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Rook_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("R", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Rook_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("R", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Rook_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("R", chessBoard, coordinates)


    #Populates White Knights present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/white_Knight_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("N", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Knight_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("N", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Knight_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("N", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Knight_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("N", chessBoard, coordinates)



    #Populates White Queens present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/white_Queen_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("Q", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Queen_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("Q", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Queen_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("Q", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_Queen_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("Q", chessBoard, coordinates)


    #Populates White Kings present on the board
    coordinates = getPieceLocations("game_Piece_PNGS/white_King_Black_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("K", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_King_White_Tile.PNG", threshold=thresh)
    chessBoard=addPiece("K", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_King_Black_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("K", chessBoard, coordinates)
    coordinates = getPieceLocations("game_Piece_PNGS/white_King_White_Tile_Selected.PNG", threshold=thresh)
    chessBoard=addPiece("K", chessBoard, coordinates)


    return chessBoard

# Finds item index in 2d array
def find_Index_2d(array, item):

    for row_idx, row in enumerate(array):
        if item in row:
            col_idx = row.index(item)
            return row_idx, col_idx
    return None 


# Translates chess player game notation to index notation
def PGNtoIndex( move, playerColor):


    # Coordinates translated to chess format that will correlate with the display coordinates, if you are playing white
    chessBoard_Translated_White_Coordinates = [
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
    chessBoard_Translated_Black_Coordinates = [
        ["H1", "G1", "F1", "E1", "D1", "C1", "B1", "A1"],
        ["H2", "G2", "F2", "E2", "D2", "C2", "B2", "A2"],
        ["H3", "G3", "F3", "E3", "D3", "C3", "B3", "A3"],
        ["H4", "G4", "F4", "E4", "D4", "C4", "B4", "A4"],
        ["H5", "G5", "F5", "E5", "D5", "C5", "B5", "A5"],
        ["H6", "G6", "F6", "E6", "D6", "C6", "B6", "A6"],
        ["H7", "G7", "F7", "E7", "D7", "C7", "B7", "A7"],
        ["H8", "G8", "F8", "E8", "D8", "C8", "B8", "A8"]
    ]

    if playerColor=="w":
        rowIndex, colIndex = find_Index_2d(chessBoard_Translated_White_Coordinates, move.upper())
    else:
        rowIndex, colIndex = find_Index_2d(chessBoard_Translated_Black_Coordinates, move.upper())


    return rowIndex, colIndex 



# Moves a piece from initial location to the end location in the internal matrix
def movePieceInternally(startAddress, endAddress, chessBoard, playerColor):


    # Translates addresses from PGN to index notation
    startAddress = PGNtoIndex( startAddress, playerColor)
    endAddress = PGNtoIndex( endAddress, playerColor)
 



    # If trying to move an empty slot end function
    if chessBoard[startAddress[0]][startAddress[1]] == "_":
        return chessBoard

    else:

        # Retrieves the pieceType
        pieceType = chessBoard[startAddress[0]][startAddress[1]]

        chessBoard[endAddress[0]][endAddress[1]] = pieceType
        chessBoard[startAddress[0]][startAddress[1]] = "_"

    return chessBoard

# Moves a piece from initial location to the end location in the internal matrix
def movePieceExternally(startAddress, endAddress, playerColor):

    # Translates addresses from PGN to index notation
    startAddress = PGNtoIndex( startAddress, playerColor)
    endAddress = PGNtoIndex( endAddress, playerColor)


    chess_Board_Coordinates_1920x1080 = [
        [[845, 190], [930, 190], [1015, 190], [1100, 190], [1185, 190], [1270, 190], [1355, 190], [1440, 190]],
        [[845, 275], [930, 275], [1015, 275], [1100, 275], [1185, 275], [1270, 275], [1355, 275], [1440, 275]],
        [[845, 360], [930, 360], [1015, 360], [1100, 360], [1185, 360], [1270, 360], [1355, 360], [1440, 360]],
        [[845, 445], [930, 445], [1015, 445], [1100, 445], [1185, 445], [1270, 445], [1355, 445], [1440, 445]],
        [[845, 530], [930, 530], [1015, 530], [1100, 530], [1185, 530], [1270, 530], [1355, 530], [1440, 530]],
        [[845, 615], [930, 615], [1015, 615], [1100, 615], [1185, 615], [1270, 615], [1355, 615], [1440, 615]],
        [[845, 700], [930, 700], [1015, 700], [1100, 700], [1185, 700], [1270, 700], [1355, 700], [1440, 700]],
        [[845, 785], [930, 785], [1015, 785], [1100, 785], [1185, 785], [1270, 785], [1355, 785], [1440, 785]]
    ]
    

    x, y = chess_Board_Coordinates_1920x1080[startAddress[0]][startAddress[1]]
    pyautogui.moveTo(x, y, 1)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseUp()
    time.sleep(1)
    x, y = chess_Board_Coordinates_1920x1080[endAddress[0]][endAddress[1]]
    pyautogui.moveTo(x, y, 1)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseUp()

    # Moves mouse back to neutral position
    pyautogui.moveTo(1400, 1000, 1)

    return
