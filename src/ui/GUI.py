import tkinter as tk
import os
import sys
from tkinter import filedialog

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from RegularExpressionsModule.Controller import Controller



class GUI:
    # inicializando ventana
    def __init__ (self, window):
        #set window and controller
        self.window = window
        self.controller = Controller()
        #set window parts
        self.window.title("Recolector de información segurAutos")
        self.window.geometry("1000x800")
        
        self.title_label = tk.Label(self.window, text="Recolector de información segurAutos", font=("Arial", 20))
        self.title_label.pack(pady=20)
        
        self.text_box = tk.Text(self.window, height=20, width=80)
        self.text_box.pack(pady=20)

        self.load_button = tk.Button(self.window, text="Cargar PDF", command=self.load_pdf)
        self.load_button.pack(side=tk.LEFT, padx=20)

        self.save_button = tk.Button(self.window, text="Descargar PDF", command=self.save_pdf)
        self.save_button.pack(side=tk.RIGHT, padx=20)


    def load_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            pass

    def save_pdf(self):
        pass

def main():
    win = tk.Tk()
    ui = GUI(win)
    win.mainloop()
    
if __name__ == "__main__":
    main()