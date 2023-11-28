# Class and Library Imports
import chessAT
import tkinter as tk

###############################################################################################################################################################
# Adaptive Neural Network Chess Agent (ANNCA) - Version 3.2 (28/11/2023)
###############################################################################################################################################################

def on_button_click_data_train():
    agent_trainer = chessAT.trainer()
    agent_trainer.data_train()

def on_button_click_active_train():
    agent_trainer = chessAT.trainer()
    agent_trainer.active_train()

state = "IDLE"
    


root = tk.Tk()
root.title("ANNCA")

label = tk.Label(root, text="Enter your name:")
label.pack()

button = tk.Button(root, text="Play", command=on_button_click)
button.pack()

button = tk.Button(root, text="Unit Test", command=on_button_click)
button.pack()

button = tk.Button(root, text="Data Train", command=on_button_click_data_train)
button.pack()

button = tk.Button(root, text="Active Train", command=on_button_click_active_train)
button.pack()



###############################################################################################################################################################

