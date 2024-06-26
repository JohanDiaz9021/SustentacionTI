import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import RegularExpressionsModule.Controller as con


class GUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Visualizador y Guardado de PDF")
        self.window.geometry("800x600")
        self.controller = con.Controller()

        self.title_label = tk.Label(self.window, text="Visualizador y Guardado de PDF", font=("Arial", 20))
        self.title_label.pack(pady=20)

        self.text_box = tk.Text(self.window, height=20, width=80)
        self.text_box.pack(pady=20)

        self.load_button = tk.Button(self.window, text="Cargar PDF", command=self.load_pdf)
        self.load_button.pack(side=tk.LEFT, padx=20)

        self.save_button = tk.Button(self.window, text="Guardar como PDF", command=self.save_pdf)
        self.save_button.pack(side=tk.RIGHT, padx=20)

    def load_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            try:
                pdf_text = ""
                with open(file_path, "rb") as pdf_file:
                    pdf_reader = PdfReader(pdf_file)
                    for page in pdf_reader.pages:
                        pdf_text += page.extract_text()
                self.text_box.delete("1.0", tk.END)
                self.text_box.insert(tk.END, pdf_text)
            except Exception as e:
                self.text_box.delete("1.0", tk.END)
                self.text_box.insert(tk.END, f"Error al cargar el PDF: {e}")

    def save_pdf(self):
        text = self.text_box.get("1.0", tk.END)
        text_to_save = self.controller.validate_input(text)
    
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    
        if file_path:
            try:
                # Crear un lienzo para escribir el texto
                c = canvas.Canvas(file_path, pagesize=letter)
                c.drawString(72, 750, f"{text_to_save}")
                c.save()
                self.text_box.delete("1.0", tk.END)
            except Exception as e:
                self.text_box.delete("1.0", tk.END)
                self.text_box.insert(tk.END, f"Error al guardar como PDF: {e}")
            


def main():
    win = tk.Tk()
    ui = GUI(win)
    win.mainloop()


if __name__ == "__main__":
    main()
