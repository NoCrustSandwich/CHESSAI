# Library Imports
import chessWS
import chessANN
import chessRLE
import chessIC
import chessANNT


# Flags to run unit testing for specific files
UT_For_chessWS = False
UT_For_chessANN = False
UT_For_chessRLE = False
UT_For_chessIC = False
UT_For_chessANNT = True



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
        print("chessWS Unit Test 1: Retrieval of piece Locations from web Page \n\tSUCCESS\n")
    else:
        print("chessWS Unit Test 1: Retrieval of piece Locations from web Page \n\tFAILED\n")


    # Unit Test 2: Rendering piece Locations from white perspective
    if UTWebScraper.renderBoardWhite(testPieceLocations) ==  testWhiteBoard:
        print("chessWS Unit Test 2: Rendering piece Locations from white perspective \n\tSUCCESS\n")
    else:
        print("chessWS Unit Test 2: Rendering piece Locations from white perspective \n\tFAILED\n")
    

    # Unit Test 3: Rendering piece Locations from black perspective
    if UTWebScraper.renderBoardBlack(testPieceLocations) ==  testBlackBoard:
        print("chessWS Unit Test 3: Rendering piece Locations from black perspective \n\tSUCCESS\n")
    else:
        print("chessWS Unit Test 3: Rendering piece Locations from black perspective \n\tFAILED\n")


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
        print("chessANN Unit Test 1: Creating Neural Network Model \n\tSUCCESS\n")
    else:
        print("chessANN Unit Test 1: Creating Neural Network Model \n\tFAILED\n")

    # Unit Test 2: Loading Neural Network Model
    if UT_ANN.loadANN(testModelName):
        print("chessANN Unit Test 2: Loading Neural Network Model \n\tSUCCESS\n")
    else:
        print("chessANN Unit Test 2: Loading Neural Network Model \n\tFAILED\n")

    # Unit Test 3: Saving Neural Network Model
    if UT_ANN.saveANN(testModelName):
        print("chessANN Unit Test 3: Saving Neural Network Model \n\tSUCCESS\n")
    else:
        print("chessANN Unit Test 3: Saving Neural Network Model \n\tFAILED\n")

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
        print("chessWS Unit Test 1: Retrieval of piece Locations from web Page \n\tSUCCESS\n")
    else:
        print("chessWS Unit Test 1: Retrieval of piece Locations from web Page \n\tFAILED\n")


    # Unit Test 2: Rendering piece Locations from white perspective
    if UTWebScraper.renderBoardWhite(testPieceLocations) ==  testWhiteBoard:
        print("chessWS Unit Test 2: Rendering piece Locations from white perspective \n\tSUCCESS\n")
    else:
        print("chessWS Unit Test 2: Rendering piece Locations from white perspective \n\tFAILED\n")
    

    # Unit Test 3: Rendering piece Locations from black perspective
    if UTWebScraper.renderBoardBlack(testPieceLocations) ==  testBlackBoard:
        print("chessWS Unit Test 3: Rendering piece Locations from black perspective \n\tSUCCESS\n")
    else:
        print("chessWS Unit Test 3: Rendering piece Locations from black perspective \n\tFAILED\n")


    print("------------------------------------------------------------------------------------------------------------------------------")

if UT_For_chessWS:
    UT_chessWS()

###############################################################################################################################################################

###############################################################################################################################################################
# Unit Testing: Reinforcment Learning Enviorment
###############################################################################################################################################################

def UT_chessRLE():

    # Reinforcment Learning Enviorment test fixture (UT Setup)
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
    testResetBoardNumerical = np.array[[[-14,-10,-12,-15,-16,-11,-9,-13],
                [-8,-7,-6,-5,-4,-3,-2,-1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,2,3,4,5,6,7,8],
                [13,9,11,15,16,12,10,14]]]
    

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tREINFORCMENT LEARNING ENVIORMENT UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")

    # Unit Test 1: Board reset
    if UT_RLE.getCurrentBoard() == testResetBoard:
        print("chessRLE Unit Test 1: Board reset \n\tSUCCESS\n")
    else:
        print("chessRLE Unit Test 1: Board reset \n\tFAILED\n")


    # Unit Test 2: Preprocessing Input into correct numerical format
    if UT_RLE.preprosessANNInput() == testResetBoardNumerical:
        print("chessRLE Unit Test 2: Preprocessing Input into correct numerical format \n\tSUCCESS\n")
    else:
        print("chessRLE Unit Test 2: Preprocessing Input into correct numerical format \n\tFAILED\n")
    

    # Unit Test 3: Move Validation

    testMoveValidationBoard = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q","k","b2","n2","r2"]]
    
    testMoveValidationAction = ("p1",(-3,0))


    if UTWebScraper.renderBoardBlack(testPieceLocations) ==  testBlackBoard:
        print("chessWS Unit Test 3: Rendering piece Locations from black perspective \n\tSUCCESS\n")
    else:
        print("chessWS Unit Test 3: Rendering piece Locations from black perspective \n\tFAILED\n")


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
        print("chessANNT Unit Test 1: Preprocessing output for ANN as an action from PGN Data for white player \n\tSUCCESS\n")
    else:
        print("chessANNT Unit Test 1: Preprocessing output for ANN as an action from PGN Data for white player \n\tFAILED\n")

    # Unit Test 2: Preprocessing output for ANN as an action from PGN Data for black player 
    if UT_ANNT.preprocessOutput(testSourceTileBlack,testTargetTileBlack,testInputBoard,"b") == testActionBlack:
        print("chessANNT Unit Test 2: Preprocessing output for ANN as an action from PGN Data for black player \n\tSUCCESS\n")
    else:
        print("chessANNT Unit Test 2: Preprocessing output for ANN as an action from PGN Data for black player \n\tFAILED\n")


    # Unit Test 3: Training on lichless chess data
    if UT_ANNT.dataTrain(input("ARTIFICIAL NEURAL NETWORK TRAINER (DATA TRAINER) - Input PGN data file directory path:")):
        print("chessANNT Unit Test 3: Training on lichless chess data \n\tSUCCESS\n")
    else:
        print("chessANNT Unit Test 3: Training on lichless chess data \n\tFAILED\n")

    # Unit Test 2: Active training against self
    if UT_ANNT.activeTrain(int(input("ARTIFICIAL NEURAL NETWORK TRAINER (ACTIVE TRAINER) - Input number of simulated chess matches:"))):
        print("chessANNT Unit Test 4: Active training against self \n\tSUCCESS\n")
    else:
        print("chessANNT Unit Test 4: Active training against self \n\tFAILED\n")

    print("------------------------------------------------------------------------------------------------------------------------------")

if UT_For_chessANNT:
    UT_chessANNT()


###############################################################################################################################################################