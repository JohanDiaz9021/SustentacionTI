import tkinter as tk
import os
import sys
from tkinter import filedialog
from fpdf import FPDF

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
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            self.text_box.delete('1.0', tk.END)
            self.text_box.insert(tk.END, text)

    def save_pdf(self):
        text = self.text_box.get("1.0", tk.END)
        result = self.controller.validate_input(text)
        result_pdf = FPDF()
        result_pdf.add_page()
        result_pdf.set_font("Arial", size = 12)
        result_pdf.cell(200, 10, txt = result, ln = True)

        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            result_pdf.output(file_path)


def main():
    win = tk.Tk()
    ui = GUI(win)
    win.mainloop()
    
if __name__ == "__main__":
    main()