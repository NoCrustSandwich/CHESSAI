# Library Imports
import chessWS
import chessANN
import chessRLE
import chessIC
import chessANNT

# Flags to run unit testing for specific files
UT_For_chessWS = False
UT_For_chessANN = False
UT_For_chessRLE = True
UT_For_chessIC = False
UT_For_chessANNT = False

# ANSI escape codes to print text in green and red:
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'  # Reset color to default

###############################################################################################################################################################



###############################################################################################################################################################
# Unit Testing: Web Scraper 
###############################################################################################################################################################

def UT_chessWS():

    # WebScraper test fixture (UT Setup)
    UTWebScraper = chessWS.webScraper()
    UT_gameURL = input("WEB SCRAPER UNIT TESTING - Input chess.com gameURL:")
    UTWebScraper.updateGameURL(UT_gameURL)
    UTWebScraper.openWebPage()
    testPieceLocations = [('br', (0, 7)), ('bn', (0, 6)), ('bb', (0, 5)), ('bk', (0, 4)), ('bq', (0, 3)), ('bb', (0, 2)), ('bn', (0, 1)), ('br', (0, 0)), ('bp', (1, 7)), ('bp', (1, 6)), ('wp', (3, 4)), ('bp', (1, 4)), ('bp', 
(1, 3)), ('bp', (1, 2)), ('bp', (1, 1)), ('bp', (1, 0)), ('wp', (6, 7)), ('wp', (6, 6)), ('wp', (6, 5)), ('bp', (3, 5)), ('wp', (6, 3)), ('wp', (6, 2)), ('wp', (6, 1)), ('wp', (6, 0)), ('wr', (7, 7)), ('wn', (7, 6)), ('wb', (7, 5)), ('wk', (7, 4)), ('wq', (7, 3)), ('wb', (7, 2)), ('wn', (7, 1)), ('wr', (7, 0))]
    testWhiteBoard = [['or2', 'on2', 'ob2', 'oq', 'ok', 'ob1', 'on1', 'or1'], ['op8', 'op7', 'op6', 'op5', 'op4', '_', 'op3', 'op2'], ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', 'p1', 'op1', '_', '_'], 
['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_'], ['p2', 'p3', 'p4', 'p5', '_', 'p6', 'p7', 'p8'], ['r1', 'n1', 'b1', 'q', 'k', 'b2', 'n2', 'r2']]
    testBlackBoard = [['or2', 'on2', 'ob2', 'ok', 'oq', 'ob1', 'on1', 'or1'], ['op8', 'op7', 'op6', '_', 'op5', 'op4', 'op3', 'op2'], ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', 'p1', 'op1', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_'], ['p2', 'p3', '_', 'p4', 'p5', 'p6', 'p7', 'p8'], ['r1', 'n1', 'b1', 'k', 'q', 'b2', 'n2', 'r2']]

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tWEB SCRAPER UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")


    # Unit Test 1: Retrieval of piece Locations from web Page
    if UTWebScraper.getPieceLocations():
        print("chessWS Unit Test 1: Retrieval of piece Locations from web Page \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 1: Retrieval of piece Locations from web Page \n\t"+RED+"FAILED"+RESET+"\n")


    # Unit Test 2: Rendering piece Locations from white perspective
    if UTWebScraper.renderBoardWhite(testPieceLocations) ==  testWhiteBoard:
        print("chessWS Unit Test 2: Rendering piece Locations from white perspective \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 2: Rendering piece Locations from white perspective \n\t"+RED+"FAILED"+RESET+"\n")
    

    # Unit Test 3: Rendering piece Locations from black perspective
    if UTWebScraper.renderBoardBlack(testPieceLocations) ==  testBlackBoard:
        print("chessWS Unit Test 3: Rendering piece Locations from black perspective \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3: Rendering piece Locations from black perspective \n\t"+RED+"FAILED"+RESET+"\n")


    print("------------------------------------------------------------------------------------------------------------------------------")

if UT_For_chessWS:
    UT_chessWS()

###############################################################################################################################################################


###############################################################################################################################################################
# Unit Testing: Artificial Neural Network 
###############################################################################################################################################################

def UT_chessANN():

    # ANN test fixture (UT Setup)
    from keras.models import Model
    UT_ANN = chessANN.ANN()
    testModelName = "CANN" # CANN - Chess Artificial Neural Network

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tARTIFICIAL NEURAL NETWORK UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")


    # Unit Test 1: Creating Neural Network Model
    if str(type(UT_ANN.createChessModel())) == "<class 'keras.src.engine.functional.Functional'>":
        print("chessANN Unit Test 1: Creating Neural Network Model \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessANN Unit Test 1: Creating Neural Network Model \n\t"+RED+"FAILED"+RESET+"\n")


    # Unit Test 2: Loading Neural Network Model
    if UT_ANN.loadANN(testModelName):
        print("chessANN Unit Test 2: Loading Neural Network Model \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessANN Unit Test 2: Loading Neural Network Model \n\t"+RED+"FAILED"+RESET+"\n")


    # Unit Test 3: Saving Neural Network Model
    if UT_ANN.saveANN(testModelName):
        print("chessANN Unit Test 3: Saving Neural Network Model \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessANN Unit Test 3: Saving Neural Network Model \n\t"+RED+"FAILED"+RESET+"\n")


    print("------------------------------------------------------------------------------------------------------------------------------")

if UT_For_chessANN:
    UT_chessANN()

###############################################################################################################################################################


###############################################################################################################################################################
# Unit Testing: Web Scraper 
###############################################################################################################################################################

def UT_chessWS():

    # WebScraper test fixture (UT Setup)
    UTWebScraper = chessWS.webScraper()
    UT_gameURL = input("WEB SCRAPER UNIT TESTING - Input gameURL:")
    UTWebScraper.updateGameURL(UT_gameURL)
    UTWebScraper.openWebPage()
    testPieceLocations = [('br', (0, 7)), ('bn', (0, 6)), ('bb', (0, 5)), ('bk', (0, 4)), ('bq', (0, 3)), ('bb', (0, 2)), ('bn', (0, 1)), ('br', (0, 0)), ('bp', (1, 7)), ('bp', (1, 6)), ('wp', (3, 4)), ('bp', (1, 4)), ('bp', 
(1, 3)), ('bp', (1, 2)), ('bp', (1, 1)), ('bp', (1, 0)), ('wp', (6, 7)), ('wp', (6, 6)), ('wp', (6, 5)), ('bp', (3, 5)), ('wp', (6, 3)), ('wp', (6, 2)), ('wp', (6, 1)), ('wp', (6, 0)), ('wr', (7, 7)), ('wn', (7, 6)), ('wb', (7, 5)), ('wk', (7, 4)), ('wq', (7, 3)), ('wb', (7, 2)), ('wn', (7, 1)), ('wr', (7, 0))]
    testWhiteBoard = [['or2', 'on2', 'ob2', 'oq', 'ok', 'ob1', 'on1', 'or1'], 
                      ['op8', 'op7', 'op6', 'op5', 'op4', '_', 'op3', 'op2'], 
                      ['_', '_', '_', '_', '_', '_', '_', '_'], 
                      ['_', '_', '_', '_', 'p1', 'op1', '_', '_'], 
                      ['_', '_', '_', '_', '_', '_', '_', '_'], 
                      ['_', '_', '_', '_', '_', '_', '_', '_'], 
                      ['p2', 'p3', 'p4', 'p5', '_', 'p6', 'p7', 'p8'], 
                      ['r1', 'n1', 'b1', 'q', 'k', 'b2', 'n2', 'r2']]
    
    testBlackBoard = [['or2', 'on2', 'ob2', 'ok', 'oq', 'ob1', 'on1', 'or1'], 
                      ['op8', 'op7', 'op6', '_', 'op5', 'op4', 'op3', 'op2'], 
                      ['_', '_', '_', '_', '_', '_', '_', '_'], 
                      ['_', '_', '_', '_', '_', '_', '_', '_'], 
                      ['_', '_', 'p1', 'op1', '_', '_', '_', '_'], 
                      ['_', '_', '_', '_', '_', '_', '_', '_'], 
                      ['p2', 'p3', '_', 'p4', 'p5', 'p6', 'p7', 'p8'], 
                      ['r1', 'n1', 'b1', 'k', 'q', 'b2', 'n2', 'r2']]

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tWEB SCRAPER UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")


    # Unit Test 1: Retrieval of piece Locations from web Page
    if UTWebScraper.getPieceLocations():
        print("chessWS Unit Test 1: Retrieval of piece Locations from web Page \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 1: Retrieval of piece Locations from web Page \n\t"+RED+"FAILED"+RESET+"\n")


    # Unit Test 2: Rendering piece Locations from white perspective
    if UTWebScraper.renderBoardWhite(testPieceLocations) ==  testWhiteBoard:
        print("chessWS Unit Test 2: Rendering piece Locations from white perspective \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 2: Rendering piece Locations from white perspective \n\t"+RED+"FAILED"+RESET+"\n")
    

    # Unit Test 3: Rendering piece Locations from black perspective
    if UTWebScraper.renderBoardBlack(testPieceLocations) ==  testBlackBoard:
        print("chessWS Unit Test 3: Rendering piece Locations from black perspective \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3: Rendering piece Locations from black perspective \n\t"+RED+"FAILED"+RESET+"\n")


    print("------------------------------------------------------------------------------------------------------------------------------")

if UT_For_chessWS:
    UT_chessWS()

###############################################################################################################################################################

###############################################################################################################################################################
# Unit Testing: Reinforcment Learning Enviornment
###############################################################################################################################################################

def UT_chessRLE():

    # Reinforcment Learning Enviornment test fixture (UT Setup)
    import numpy as np
    UT_RLE = chessRLE.RLE()
    UT_RLE.resetBoard()
    testResetBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q","k","b2","n2","r2"]]
    testResetBoardNumerical = np.array([
                [-14,-10,-12,-15,-16,-11,-9,-13],
                [-8,-7,-6,-5,-4,-3,-2,-1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,2,3,4,5,6,7,8],
                [13,9,11,15,16,12,10,14]])
    

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tREINFORCMENT LEARNING ENVIORNMENT UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")


    # Unit Test 1: Board reset
    if UT_RLE.getCurrentBoard() == testResetBoard:
        print("chessRLE Unit Test 1: Board reset \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessRLE Unit Test 1: Board reset \n\t"+RED+"FAILED"+RESET+"\n")


    # Unit Test 2: Preprocessing Input into correct numerical format
    if UT_RLE.preprosessANNInput().all() == testResetBoardNumerical.all():
        print("chessRLE Unit Test 2: Preprocessing Input into correct numerical format \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessRLE Unit Test 2: Preprocessing Input into correct numerical format \n\t"+RED+"FAILED"+RESET+"\n")
    

    # Unit Test 3: Illegal Move Validation

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Unit Test 3.1: Illegal Move Validation - Rook Blocked Path
    testMoveValidationBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","on1","ob1","oq","ok","ob2","on2","r2"]]
    
    # Unit Test 3.1.1: X-Path
    testIllegalMoveValidationAction = ("r1",(-3,0))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, rook or queen is blocked by other piece in it's path"}:
        print("chessWS Unit Test 3.1.1: Illegal Move Validation - Rook Blocked X-Path \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.1.1: Illegal Move Validation - Rook Blocked X-Path \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    # Unit Test 3.1.2: Y-Path
    testIllegalMoveValidationAction = ("r2",(0,-4))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)
    
    if info ==  {"Invalid Move, rook or queen is blocked by other piece in it's path"}:
        print("chessWS Unit Test 3.1.2: Illegal Move Validation - Rook Blocked Y-Path \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.1.2: Illegal Move Validation - Rook Blocked Y-Path \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Unit Test 3.2: Illegal Move Validation - Bishop Blocked Path
    testMoveValidationBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q","k","b2","n2","r2"]]
    
    # Unit Test 3.2.1: UL-Path
    testIllegalMoveValidationAction = ("b1",(-3,3))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, bishop or queen is blocked by other piece in it's path"}:
        print("chessWS Unit Test 3.2.1: Illegal Move Validation - Bishop Blocked UL-Path \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.2.1: Illegal Move Validation - Bishop Blocked UL-Path \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    # Unit Test 3.2.2: UR-Path
    testIllegalMoveValidationAction = ("b2",(-3,-3))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, bishop or queen is blocked by other piece in it's path"}:
        print("chessWS Unit Test 3.2.2: Illegal Move Validation - Bishop Blocked UR-Path \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.2.2: Illegal Move Validation - Bishop Blocked UR-Path \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Unit Test 3.3: Illegal Move Validation - Out of Range
    testMoveValidationBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","q","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b2","_","k","_","n2","r2"]]
    
    # Unit Test 3.3.1: right-Side of board
    testIllegalMoveValidationAction = ("q",(0,7))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, Target Location is out of range"}:
        print("chessWS Unit Test 3.3.1: Illegal Move Validation - Out of Range Right-Side of board \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.3.1: Illegal Move Validation - Out of Range Right-Side of board  \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    # Unit Test 3.3.2: left-Side of board
    testIllegalMoveValidationAction = ("q",(0,-7))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, Target Location is out of range"}:
        print("chessWS Unit Test 3.3.2: Illegal Move Validation - Out of Range Left-Side of board \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.3.2: Illegal Move Validation - Out of Range Left-Side of board  \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    # Unit Test 3.3.3: top-Side of board
    testIllegalMoveValidationAction = ("q",(-7,0))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, Target Location is out of range"}:
        print("chessWS Unit Test 3.3.3: Illegal Move Validation - Out of Range Top-Side of board \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.3.3: Illegal Move Validation - Out of Range Top-Side of board  \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    # Unit Test 3.3.4: bottom-Side of board
    testIllegalMoveValidationAction = ("q",(7,0))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, Target Location is out of range"}:
        print("chessWS Unit Test 3.3.4: Illegal Move Validation - Out of Range Bottom-Side of board \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.3.4: Illegal Move Validation - Out of Range Bottom-Side of board  \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")


    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Unit Test 3.4: Illegal Move Validation - Pawn Blocked Path
    testMoveValidationBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","op1","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","on1","ob1","oq","ok","ob2","on2","r2"]]
    
    testIllegalMoveValidationAction = ("p2",(-2,0))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, pawn is blocked by other piece in it's path"}:
        print("chessWS Unit Test 3.4: Illegal Move Validation - pawn is blocked \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.4: Illegal Move Validation - pawn is blocked \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Unit Test 3.5: Illegal Move Validation - Pawn diagonal empty space move
    testMoveValidationBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","op1","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","on1","ob1","oq","ok","ob2","on2","r2"]]
    
    testIllegalMoveValidationAction = ("p2",(-1,1))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, pawn cannot side ways unless opossing piece is there"}:
        print("chessWS Unit Test 3.5: Illegal Move Validation - Pawn diagonal empty space move \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.5: Illegal Move Validation - Pawn diagonal empty space move \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Unit Test 3.6: Illegal Move Validation - pawn cannot move 2 spaces unless in starting position
    testMoveValidationBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","p2","_","_","_","_","_","_"],
                ["p1","_","p3","p4","p5","p6","p7","p8"],
                ["r1","on1","ob1","oq","ok","ob2","on2","r2"]]
    
    testIllegalMoveValidationAction = ("p2",(-2,0))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, pawn cannot move 2 spaces unless in starting position"}:
        print("chessWS Unit Test 3.6: Illegal Move Validation - pawn cannot move 2 spaces unless in starting position \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.6: Illegal Move Validation - pawn cannot move 2 spaces unless in starting position \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")


    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Unit Test 3.7: Illegal Move Validation - king castling outside of starting conditions for rook and king

    # Unit Test 3.7.1: Starting Position Right Castle
    testMoveValidationBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","r2"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","_","_","_","k","_","_","_"]]
    
    testIllegalMoveValidationAction = ("k",(0,2))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, king cannot castle unless King and rook are in starting position"}:
        print("chessWS Unit Test 3.7.1: Illegal Move Validation, king cannot castle unless King and rook are in starting position - Starting Position Right Castle \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.7.1: Illegal Move Validation, king cannot castle unless King and rook are in starting position - Starting Position Right Castle \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    # Unit Test 3.7.2: Starting Position Left Castle
    testMoveValidationBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["r1","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["_","_","_","_","k","_","_","r1"]]
    
    testIllegalMoveValidationAction = ("k",(0,-2))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, king cannot castle unless King and rook are in starting position"}:
        print("chessWS Unit Test 3.7.2: Illegal Move Validation, king cannot castle unless King and rook are in starting position - Starting Position Left Castle \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.7.2: Illegal Move Validation, king cannot castle unless King and rook are in starting position - Starting Position Left Castle \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    # Unit Test 3.7.3: Outside of Starting Position Castle
    testMoveValidationBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","k","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","_","_","_","_","_","_","r2"]]
    
    testIllegalMoveValidationAction = ("k",(0,-2))
    UT_RLE.updateBoard(testMoveValidationBoard)
    observation, reward, done, info, switchPlayer, startLocation, endLocation = UT_RLE.step(testIllegalMoveValidationAction)

    if info ==  {"Invalid Move, king cannot castle unless King and rook are in starting position"}:
        print("chessWS Unit Test 3.7.3: Illegal Move Validation, king cannot castle unless King and rook are in starting position - Outside Starting Position Castle \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessWS Unit Test 3.7.3: Illegal Move Validation, king cannot castle unless King and rook are in starting position - Outside Starting Position Castle \n\t"+RED+"FAILED"+RESET+"")
        print(info)
        print("\n")

    print("------------------------------------------------------------------------------------------------------------------------------")

if UT_For_chessRLE:
    UT_chessRLE()


###############################################################################################################################################################


###############################################################################################################################################################
# Unit Testing: Interface Controller
###############################################################################################################################################################

def UT_chessIC():

    # Interface Controller test fixture (UT Setup)
    UT_IC = chessIC.controller()

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tINTERFACE CONTROLLER UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")

    print("------------------------------------------------------------------------------------------------------------------------------")

if UT_For_chessIC:
    UT_chessIC()

###############################################################################################################################################################

###############################################################################################################################################################
# Unit Testing: Artificial Neural Network Trainer
###############################################################################################################################################################

def UT_chessANNT():

    # DIRECTORIES WITH LICHLESS DATA (on host machine)
    # ---------------------------------------------------
    # F:\LichlessData\lichess_db_standard_rated_2013-01.pgn
    # F:\LichlessData\lichess_db_standard_rated_2014-07.pgn

    # Artificial Neural Network Trainer test fixture (UT Setup)
    UT_ANNT = chessANNT.trainer()
    testSourceTileWhite = "e2"
    testTargetTileWhite = "e4"
    testSourceTileBlack = "f7"
    testTargetTileBlack = "f5"
    testInputBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q","k","b2","n2","r2"]]
    testActionWhite = ("p4", (-2,0))
    testActionBlack = ("p3", (-2,0))

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tARTIFICIAL NEURAL NETWORK TRAINER UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")

    # Unit Test 1: Preprocessing output for ANN as an action from PGN Data for white player 
    if UT_ANNT.preprocessOutput(testSourceTileWhite,testTargetTileWhite,testInputBoard,"w") == testActionWhite:
        print("chessANNT Unit Test 1: Preprocessing output for ANN as an action from PGN Data for white player \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessANNT Unit Test 1: Preprocessing output for ANN as an action from PGN Data for white player \n\t"+RED+"FAILED"+RESET+"\n")

    # Unit Test 2: Preprocessing output for ANN as an action from PGN Data for black player 
    if UT_ANNT.preprocessOutput(testSourceTileBlack,testTargetTileBlack,testInputBoard,"b") == testActionBlack:
        print("chessANNT Unit Test 2: Preprocessing output for ANN as an action from PGN Data for black player \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessANNT Unit Test 2: Preprocessing output for ANN as an action from PGN Data for black player \n\t"+RED+"FAILED"+RESET+"\n")


    # Unit Test 3: Training on lichless chess data
    if UT_ANNT.dataTrain(input("ARTIFICIAL NEURAL NETWORK TRAINER (DATA TRAINER) - Input PGN data file directory path:")):
        print("chessANNT Unit Test 3: Training on lichless chess data \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessANNT Unit Test 3: Training on lichless chess data \n\t"+RED+"FAILED"+RESET+"\n")

    # Unit Test 2: Active training against self
    if UT_ANNT.activeTrain(int(input("ARTIFICIAL NEURAL NETWORK TRAINER (ACTIVE TRAINER) - Input number of simulated chess matches:"))):
        print("chessANNT Unit Test 4: Active training against self \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessANNT Unit Test 4: Active training against self \n\t"+RED+"FAILED"+RESET+"\n")

    print("------------------------------------------------------------------------------------------------------------------------------")

if UT_For_chessANNT:
    UT_chessANNT()


###############################################################################################################################################################