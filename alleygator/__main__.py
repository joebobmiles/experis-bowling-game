from tkinter import *
from tkinter import ttk

if __name__ == "__main__":
    root = Tk()
    root.title("AlleyGator")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.mainloop()