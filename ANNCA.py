import time
import chessAT
import chessIC
import chessWS
import chessRLE
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk


###############################################################################################################################################################
# Adaptive Neural Network Chess Agent (ANNCA) - Version 3.5 (21/12/2023)
###############################################################################################################################################################

def on_button_click_play():
    """
    ANNCA enters the playing state, where it interacts with chess.com game based on game url input.
    """
    interface_controller = chessIC.controller()
    web_scraper = chessWS.webScraper()
    adaptive_agent = chessRLE.RLE()

    game_url = input("Input gameURL:")
    web_scraper.update_game_url(game_url)
    player_perspective = input("Input player Color (w/b):").lower() 

    interface_controller.calibrate_board_tile_display_coordinates()
    web_scraper.initialize_web_page()

    action_history = []
    game_end = False

    while not game_end:

        latest_move_history_san = web_scraper.fetch_latest_move_history_san()
        
        if len(latest_move_history_san) == 0 and player_perspective=="w":

            if adaptive_agent.perspective != player_perspective:
                adaptive_agent.change_perspective()

            valid_move = False
            while not valid_move: # Continues Attempting the most viable action known to ANNCA.

                q_values = adaptive_agent.neuralNetwork.model.predict(adaptive_agent.preprosess_input(adaptive_agent.board_state))
                action_index = np.argmax(q_values)
                action = adaptive_agent.POSSIBLE_MOVES[action_index] 
                action_info, action_reward, valid_move, game_end = adaptive_agent.attempt_action(action)
            
            action_history.append(action)
            interface_controller.execute_action(action, adaptive_agent.board_state)
            
        elif len(latest_move_history_san) == 0:
            print("Waiting for opposing player's Move...")
            time.sleep(5)
            continue


        latest_action_history = adaptive_agent.san_to_an(latest_move_history_san)

        latest_action_history_length = len(latest_action_history)
        action_history_length = len(action_history)

        if (latest_action_history_length==action_history_length) and ((latest_action_history_length%2 == 0 and player_perspective == "w") or (latest_action_history_length%2 == 1 and player_perspective == "b")): # Condition to make a move

            if adaptive_agent.perspective != player_perspective:
                adaptive_agent.change_perspective()

            valid_move = False
            while not valid_move: # Continues Attempting the most viable action known to ANNCA.

                q_values = adaptive_agent.neuralNetwork.model.predict(adaptive_agent.preprosess_input(adaptive_agent.board_state))
                action_index = np.argmax(q_values)
                action = adaptive_agent.POSSIBLE_MOVES[action_index] 
                action_info, action_reward, valid_move, game_end = adaptive_agent.attempt_action(action)
            
            action_history.append(action)
            interface_controller.execute_action(action, adaptive_agent.board_state)

        elif latest_action_history_length > action_history_length: # Condition to update board to most recent
            for index in range(action_history_length, latest_action_history_length):
                if index%2 == 0 and adaptive_agent.perspective != "w":
                    adaptive_agent.change_perspective()
                elif index%2 == 1 and adaptive_agent.perspective != "b":
                    adaptive_agent.change_perspective()
                    
                action = latest_action_history[index]
                action_info, action_reward, valid_move, game_end = adaptive_agent.attempt_action(action)

                q_values = adaptive_agent.neuralNetwork.model.predict(adaptive_agent.preprosess_input(adaptive_agent.board_state))
                action_index = np.argmax(q_values)
                adaptive_agent.train_neural_network(adaptive_agent.board_state, 1000, q_values, action_index)
                action_history.append(action)

        else:
            print("Waiting for opposing player's Move...")
            time.sleep(5)
        
        time.sleep(5)

def on_button_click_IDLE():
    """
    ANNCA enters the IDLE state, where it waits for instructions.
    """
    text_box.insert(tk.END, "Welcome! Please select an option above...")
    bold_and_center_text(text_box)
    text_box.configure(state=tk.DISABLED)

    while True:
        time.sleep(5)


def on_button_click_data_train():
    """
    ANNCA enters the data training state, where it trains the agent on given data.
    """
    clear_text(text_box)
    text_box.insert(tk.END, "Data training started...")
    agent_trainer = chessAT.trainer()
    agent_trainer.data_train()
    clear_text(text_box)
    text_box.insert(tk.END, "Data training completed. Please select an option above...")
    

def on_button_click_active_train():
    """
    ANNCA enters the active training state, where it trains the agent by simulating games against itself.
    """
    clear_text(text_box)
    text_box.insert(tk.END, "Active training started...")
    agent_trainer = chessAT.trainer()
    agent_trainer.active_train(1000)
    clear_text(text_box)
    text_box.insert(tk.END, "Active training completed. Please select an option above...")


def clear_text(widget):
    """
    Clears the text in the widget that is input.

    Parameters:
            - widget: GUI Widget.
    """
    widget.configure(state=tk.NORMAL)
    widget.delete("1.0", tk.END)
    widget.configure(state=tk.DISABLED)


def bold_and_center_text(widget):
    """
    Bolds and centres the text in the widget that is input.

    Parameters:
            - widget: GUI Widget.
    """
    widget.tag_configure("center", justify="center")
    widget.tag_add("center", 1.0, "end")
    widget.tag_configure("bold", font=("Helvetica", 12, "bold"))
    widget.tag_add("bold", 1.0, "end")


#----------------------------------------------------------------------------------------------------------------------------------------------
# Graphical User Interface - Version 1.0 (30/11/2023)
#----------------------------------------------------------------------------------------------------------------------------------------------
"""
Graphical User Interface for ANNCA application.
"""
root = tk.Tk()
root.title("ANNCA")

window_width = 400                                                                          # Sets the window size and position
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = screen_width - window_width                                                    # Sets x_position for the middle right
y_position = (screen_height - window_height) // 2                                           # Sets y_position for the middle

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

icon_path = "media/icon.ico"                                                                
root.iconbitmap(icon_path)

icon_path = "media/icon.png"   
icon_image = Image.open(icon_path)
photo_image = ImageTk.PhotoImage(icon_image)
root.tk.call('wm', 'iconphoto', root._w, photo_image)


button_play = tk.Button(root, text="Play", command=on_button_click_play, font=("Helvetica", 12), bg="#f0f0f0", fg="black")                                                  # Creates and places buttons in four quadrants
button_play.grid(row=0, column=0, columnspan=2, sticky="nsew")

button_data_train = tk.Button(root, text="Data Train", command=on_button_click_data_train, font=("Helvetica", 12), bg="#f0f0f0", fg="black")
button_data_train.grid(row=1, column=0, sticky="nsew")

button_active_train = tk.Button(root, text="Active Train", command=on_button_click_active_train, font=("Helvetica", 12), bg="#f0f0f0", fg="black")
button_active_train.grid(row=1, column=1, sticky="nsew")

button_active_train = tk.Button(root, text="IDLE", command=on_button_click_IDLE, font=("Helvetica", 12), bg="#f0f0f0", fg="black")
button_active_train.grid(row=2, columnspan=2, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

text_box = tk.Text(root, height=6, wrap=tk.WORD, state=tk.NORMAL)
text_box.grid(row=3, column=0, columnspan=2, sticky="nsew")

text_box.insert(tk.END, "Welcome! Please select an option above...")
bold_and_center_text(text_box)
text_box.configure(state=tk.DISABLED)

root.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------

###############################################################################################################################################################
