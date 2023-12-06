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
ut_for_chessAT = True


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
# Unit Testing: Reinforcment Learning Enviornment - Version 2.0 (5/12/2023) 
###############################################################################################################################################################

def ut_chessRLE():
    """
    Perform unit tests for the adaptive chess agent's reinforcement learning enviorment (chessRLE) module.

    
    Results of each unit test are printed, indicating success or failure.

    Usage:
        - ut_chessRLE()
    """
    adaptive_agent = chessRLE.RLE()
    adaptive_agent.reset_game_state()
    board = [["or2","on2","ob2","oq","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q","k","b2","n2","r2"]]
    
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tREINFORCMENT LEARNING ENVIORNMENT UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")

    print("------------------------------------------------------------------------------------------------------------------------------")

if ut_for_chessRLE:
    ut_chessRLE()

###############################################################################################################################################################


###############################################################################################################################################################
# Unit Testing: Interface Controller - Version 1.1 (21/11/2023) 
###############################################################################################################################################################

def ut_chessIC():
    """
    Perform unit tests for the Chess.com Interface Controller (chessIC) module.

    
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
# Unit Testing: Agent Trainer - Version 2.0 (5/12/2023) 
###############################################################################################################################################################

def ut_chessAT():
    """
    Perform unit tests for the adaptive chess agent trainer (chessAT) module.

    
    Results of each unit test are printed, indicating success or failure.

    Usage:
        - ut_chessAT()
    """
    trainer = chessAT.trainer()

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\tARTIFICIAL NEURAL NETWORK TRAINER UNIT TESTING")
    print("------------------------------------------------------------------------------------------------------------------------------\n")

    board = [   ["or2","on2","ob2","oq1","ok","ob1","on1","or1"],
                ["op8","op7","op6","op5","op4","op3","op2","op1"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["_","_","_","_","_","_","_","_"],
                ["p1","p2","p3","p4","p5","p6","p7","p8"],
                ["r1","n1","b1","q1","k","b2","n2","r2"]]
    san_move = "e4"
    lan_move = "e2e4"
    perspective = "w"

    if trainer.san_to_action( board, san_move, lan_move, perspective) == ("p5",(-2,0)):
        print("chessAT Unit Test 1.1: Testing SAN to Action conversion - Pawn Move \n\t"+GREEN+"SUCCESS"+RESET+"\n")
    else:
        print("chessAT Unit Test 1.1: Testing SAN to Action conversion - Pawn Move \n\t"+RED+"FAILED"+RESET+"\n")

    print("------------------------------------------------------------------------------------------------------------------------------")

if ut_for_chessAT:
    ut_chessAT()

###############################################################################################################################################################