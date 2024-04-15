import tkinter as tk
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from RegularExpressionsModule import Controller



class GUI:
    # inicializando ventana
    def __init__ (self, window):
        self.window = window
        self.controller = Controller()

def main():
    win = tk.Tk()
    ui = GUI(win)
    
if __name__ == "__main__":
    main()