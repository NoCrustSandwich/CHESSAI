import chessWS
import chessIC
import chessAT
import chessANN
import chessRLE


# Flags to run unit testing on the classes you want to
ut_for_chessWS = False
ut_for_chessANN = False
ut_for_chessRLE = False
ut_for_chessIC = False
ut_for_chessANNT = False
ut_for_chessGUI = False

# ANSI escape codes to print text in green and red:
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

###############################################################################################################################################################


###############################################################################################################################################################
# Unit Testing: Web Scraper  - Version 1.1 (21/11/2023)
###############################################################################################################################################################

def ut_chessWS():
    """
    Perform unit tests for the Chess WebScraper (chessWS) module.

    This function sets up a test fixture, including creating a Chess WebScraper instance, providing a game URL,
    and defining a test piece location configuration. It then executes the following unit tests:
    
    1. Unit Test 1: Retrieval of latest move history from game session

    Results of each unit test are printed, indicating success or failure.

    Usage:
        - ut_chessWS()
    """
    webScraper = chessWS.webScraper()
    ut_game_url = input("WEB SCRAPER UNIT TESTING - Input chess.com game session URL:")
    webScraper.update_game_url(ut_game_url)
    webScraper.initialize_web_page()
    
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tWEB SCRAPER UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")

    print("chessWS Unit Test 1: Retrieval of latest move history from game session \n") # Unit Test 1: Retrieval of latest move history from game session
    if webScraper.fetch_latest_move_history_san():
        print("\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("\t"+RED+"FAILED"+RESET+"\n")

    print("------------------------------------------------------------------------------------------------------------------------------")

if ut_for_chessWS:
    ut_chessWS()

###############################################################################################################################################################


###############################################################################################################################################################
# Unit Testing: Artificial Neural Network - Version 1.1 (21/11/2023)
###############################################################################################################################################################

def ut_chessANN():
    """
    Perform unit tests for the Artificial Neural Network (chessANN) module.

    This function sets up a test fixture, including creating an instance of the neural network,
    defining a model name for unit testing, and executing a unit test:

    1. Unit Test 1: Creating, saving, and loading a new neural network model.

    Results of each unit test are printed, indicating success or failure.

    Usage:
        - ut_chessANN()
    """
    neuralNetwork = chessANN.neuralNetwork()
    model_name = "Unit Test Model"

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tARTIFICIAL NEURAL NETWORK UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")
    
    print("chessANN Unit Test 1: Creating, Saving and Loading a New Neural Network Model \n")   # Unit Test 1: Creating, Saving and Loading a New Neural Network Model
    neuralNetwork.create_new_model(model_name)
    if neuralNetwork.load_model(model_name):
        neuralNetwork.delete_model(model_name)
        print("\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("\t"+RED+"FAILED"+RESET+"\n")
    
    print("------------------------------------------------------------------------------------------------------------------------------")

if ut_for_chessANN:
    ut_chessANN()

###############################################################################################################################################################


###############################################################################################################################################################
# Unit Testing: Reinforcment Learning Enviornment
###############################################################################################################################################################

def ut_chessRLE():

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

if ut_for_chessRLE:
    ut_chessRLE()


###############################################################################################################################################################


###############################################################################################################################################################
# Unit Testing: Interface Controller - Version 1.1 (21/11/2023) 
###############################################################################################################################################################

def ut_chessIC():
    """
    Perform unit tests for the Chess,com Interface Controller (chessIC) module.

    
    Results of each unit test are printed, indicating success or failure.

    Usage:
        - ut_chessIC()
    """
    controller = chessIC.controller()

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tINTERFACE CONTROLLER UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")

    print("------------------------------------------------------------------------------------------------------------------------------")

if ut_for_chessIC:
    ut_chessIC()

###############################################################################################################################################################

###############################################################################################################################################################
# Unit Testing: Agent Trainer
###############################################################################################################################################################

def ut_chessANNT():

    # DIRECTORIES WITH LICHLESS DATA (on host machine)
    # ---------------------------------------------------
    # F:\LichlessData\lichess_db_standard_rated_2013-01.pgn
    # F:\LichlessData\lichess_db_standard_rated_2014-07.pgn

    # Artificial Neural Network Trainer test fixture (UT Setup)
    UT_ANNT = chessAT.trainer()
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

if ut_for_chessANNT:
    ut_chessANNT()


###############################################################################################################################################################