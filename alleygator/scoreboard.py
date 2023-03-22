from tkinter import *
from tkinter import ttk

from bowlingframe import BowlingFrame, BowlingLastFrame

class ScoreBoard(ttk.Frame):
    def __init__(self, root_frame: ttk.Frame):
        super().__init__(root_frame)

        first_bowling_frame = BowlingFrame(self, 1, None, None)
        first_bowling_frame.grid(column=1, row=1)
        self.__first_bowling_frame = first_bowling_frame
        self.__last_bowling_frame = self.__first_bowling_frame

        for i in range(8):
            previous_bowling_frame = self.__last_bowling_frame
            bowling_frame = BowlingFrame(self, i+2, previous_bowling_frame, None)
            bowling_frame.grid(column=i+2, row=1)
            self.__last_bowling_frame.next = bowling_frame

        previous_bowling_frame = self.__last_bowling_frame
        last_bowling_frame = BowlingLastFrame(self, 10, self.__last_bowling_frame)
        last_bowling_frame.grid(column=10, row=1)
        self.__last_bowling_frame = last_bowling_frame