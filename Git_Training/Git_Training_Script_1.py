#
#    .VERSION
#       ...
#    .SYNOPSIS
#       ...
#    .DESCRIPTION
#       ...
#    .PARAMETER 
#    None
#    .EXAMPLE
#    ...
#
#test JOYCE
#test Chris
   
#------------------- Importing required modules -------------------

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import json

#------------------- Main function -------------------

# Each participant to write a meesage
Training_Participants = {'Joyce': "Message", 
                            'Mika': "Message", 
                            'Chris': "Message", 
                            'Xavier': "Message", 
                            'Julien': "Message", 
                            'Fred': "Hello"}

# Comments
Title = "Welcome to the Git Training !"
for participant in Training_Participants :
    #print(participant)
    #print(Training_Participants[participant])
    
    # Displaying a box with participant and message
    Box_Title = "Welcome "+participant
    Box_Message = Training_Participants[participant]
    #class tkinter.messagebox.Message(master=None, **options)
    #tkinter.messagebox.showinfo(title=Box_Title, message=Box_Message)

    # Display a message with participant information
    root = tk.Tk()
    root.title(Box_Title)
    root.geometry('500x300')
    root.mainloop()

    #tkinter.messagebox.showwarning(title="Example", message="Error")

# Asking user to provide Participant name 
Input_Participant = input("Please enter participant: ")
Participant_found = False

for participant in Training_Participants :
    if participant == Input_Participant :
        Participant_found = True

if Participant_found == True:
    print("Participant "+Input_Participant+" found in the list")
else :
    print("Participant "+Input_Participant+" NOT found in the list")

# Ending script
print ("Script end !")

# Wrong code put here