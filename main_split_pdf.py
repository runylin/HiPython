# main.py
from src.split_pdf import FileSelectorApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()