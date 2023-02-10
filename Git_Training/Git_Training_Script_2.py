import sys
import os
from tkinter import messagebox

if sys.version_info[0] < 3:
    import Tkinter as tkinter
else:
    import tkinter
 
window = tkinter.Tk()
window.geometry('640x380')

messagebox.showwarning("Oops!", "I did it again")
window.mainloop()