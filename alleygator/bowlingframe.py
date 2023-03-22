from tkinter import *
from tkinter import ttk
import re

def next_entry_factory(next_entry):
    def goto_next_entry(arg):
        next_entry.focus()

    return goto_next_entry

def point_validate_factory(next_entry):
    def point_validate(value):
        pattern = r"^([0-9]|\/|X)?$"
        if re.fullmatch(pattern, value) is None:
            return False

        next_entry.focus()
        return True

    return point_validate

def on_point_invalid_factory(entry):
    def on_point_invalid():
        print("invalid")

    return on_point_invalid

# for index, entry in enumerate(point_entries):
#     if (index+1 < len(point_entries)):
#         entry["validate"] = "key"
#         entry["validatecommand"] = (entry.register(point_validate_factory(point_entries[index+1])), "%P")
#         entry["invalidcommand"] = (entry.register(on_point_invalid_factory(entry)), )

class BowlingFrame(ttk.Frame):
    def __init__(self, root_frame: ttk.Frame, number, prev, next):
        super().__init__(root_frame)

        self["padding"] = (0, 16, 16, 16)

        self.prev: BowlingFrame = prev
        self.next: BowlingFrame = next

        self.pin_counts = (StringVar(), StringVar())
        self.score = StringVar(value="-")

        frame_number = ttk.Label(self, text=number)
        frame_number.grid(column=1, row=1, columnspan=3)

        first_points_entry = ttk.Entry(self, width=3, textvariable=self.pin_counts[0], justify=CENTER)
        first_points_entry.grid(column=1, row=2)

        second_points_entry = ttk.Entry(self, width=3, textvariable=self.pin_counts[1], justify=CENTER)
        second_points_entry.grid(column=2, row=2)

        score_number = ttk.Label(self, textvariable=self.score)
        score_number.grid(column=1, row=3, columnspan=3)

class BowlingLastFrame(BowlingFrame):
    def __init__(self, root_frame: ttk.Frame, number, prev):
        super().__init__(root_frame, number, prev, None)

        self["padding"] = (0, 16, 0, 16)

        self.pin_counts = (StringVar(), StringVar(), StringVar())

        third_points_entry = ttk.Entry(self, width=3, textvariable=self.pin_counts[2], justify=CENTER)
        third_points_entry.grid(column=3, row=2)