from tkinter import *
from tkinter import ttk

from scoreboard import ScoreBoard

if __name__ == "__main__":
    root = Tk()
    root.title("AlleyGator")

    mainframe = ttk.Frame(root)
    mainframe["padding"] = 8
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    score_board = ScoreBoard(mainframe)
    score_board.grid(column=1, row=1)

    reset_btn = ttk.Button(mainframe, text="Reset")
    reset_btn.grid(column=1, row=2, columnspan=22, sticky=E)

    root.mainloop()