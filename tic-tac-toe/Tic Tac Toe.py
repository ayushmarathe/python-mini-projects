# imports


import tkinter as tk
from tkinter import PhotoImage, ttk
from collections import deque
from tkinter import font


# /imports

# Colours
color_primary = "#7FBCD2"
color_secondary = "#A5F1E9"
color_text_primary = "#E1FFEE"
color_text_secondary = "#FFEEAF"
# /colours


class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.columnconfigure(0, weight=1)
        self.title("TIC TAC TOE")
        self.geometry("450x400+350+150")
        self.resizable(False, False)
        image = PhotoImage(
          file="img//unnamed.png")
        self.iconphoto(False, image)
       # Styling
        style = ttk.Style()
        style.configure(
            "Background.TFrame",
            background=color_primary,
            font=("Arial", 10)
        )
        style.configure(
            "Button.TButton",
            background="white",
            foreground="blue",
            font=("Arial", 12)
        )
        style.configure(
            "Heading.TLabel",
            background=color_primary,
            foreground=color_text_primary,
            font=("Arial", 12)
        )
        style.configure(
            "Text.TLabel",
            background = color_primary,
            foreground = "red",
            font = ("Arial",14)
        )
        # /styling
        self["background"] = color_primary

        heading_frame = ttk.Frame(self, padding=20, style="Background.TFrame")
        heading_frame.grid(row=0, column=0, columnspan=3)
        heading_label = ttk.Label(
            heading_frame, text="TIC                TAC                TOE", style="Heading.TLabel")
        heading_label.grid(row=0, column=0)
        heading_frame.tkraise()
        # Win Frame
        self.win_frame = ttk.Frame(self, padding=80,style="Background.TFrame")
        self.win_frame.grid(row=0, column=0, rowspan=4, columnspan=3)

        self.X_or_O = tk.StringVar()

        win_label = ttk.Label(self.win_frame, textvariable=self.X_or_O,style="Text.TLabel")
        win_label.grid(columnspan=2,pady=5)

        # Draw Frame
        self.draw_frame = ttk.Frame(self, padding=80,style="Background.TFrame")
        self.draw_frame.grid(row=0, column=0, rowspan=4, columnspan=3)

        draw_label = ttk.Label(self.draw_frame, text="Game Draw!",style="Text.TLabel")
        draw_label.grid(columnspan=2,pady=5)
        frames = [self.win_frame, self.draw_frame]
        for frame in frames:
            self.resetButton = ttk.Button(frame, text="Restart",command=self.restart,style="Button.TButton")
            self.resetButton.grid(row=1, column=0)

            self.quitButton = ttk.Button(
                frame, text="Exit", command=self.destroy,style="Button.TButton")
            self.quitButton.grid(row=1, column=1)

        # count
        self.count = 0

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.grid(row=1)
        button_frame.tkraise()
        # button stringvar
        self.buttonIn1 = tk.StringVar()
        self.buttonIn2 = tk.StringVar()
        self.buttonIn3 = tk.StringVar()
        self.buttonIn4 = tk.StringVar()
        self.buttonIn5 = tk.StringVar()
        self.buttonIn6 = tk.StringVar()
        self.buttonIn7 = tk.StringVar()
        self.buttonIn8 = tk.StringVar()
        self.buttonIn9 = tk.StringVar()

        # XO
        self.moves = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        self.moves_pattern = deque(self.moves)

        # buttons
        self.button_1 = ttk.Button(button_frame, textvariable=self.buttonIn1, padding=(
            10, 40), command=self.buttonOne, style="Button.TButton", cursor="hand2")
        self.button_2 = ttk.Button(button_frame, textvariable=self.buttonIn2, padding=(
            10, 40), command=self.buttonTwo, style="Button.TButton", cursor="hand2")
        self.button_3 = ttk.Button(button_frame, textvariable=self.buttonIn3, padding=(
            10, 40), command=self.buttonThree, style="Button.TButton", cursor="hand2")
        self.button_4 = ttk.Button(button_frame, textvariable=self.buttonIn4, padding=(
            10, 40), command=self.buttonFour, style="Button.TButton", cursor="hand2")
        self.button_5 = ttk.Button(button_frame, textvariable=self.buttonIn5, padding=(
            10, 40), command=self.buttonFive, style="Button.TButton", cursor="hand2")
        self.button_6 = ttk.Button(button_frame, textvariable=self.buttonIn6, padding=(
            10, 40), command=self.buttonSix, style="Button.TButton", cursor="hand2")
        self.button_7 = ttk.Button(button_frame, textvariable=self.buttonIn7, padding=(
            10, 40), command=self.buttonSeven, style="Button.TButton", cursor="hand2")
        self.button_8 = ttk.Button(button_frame, textvariable=self.buttonIn8, padding=(
            10, 40), command=self.buttonEight, style="Button.TButton", cursor="hand2")
        self.button_9 = ttk.Button(button_frame, textvariable=self.buttonIn9, padding=(
            10, 40), command=self.buttonNine, style="Button.TButton", cursor="hand2")

        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)

    # Button Functions
    def restart(self):
        self.destroy()
        self = Game()
        self.mainloop()


    def place_XO(self):
        self.nextUp = self.moves_pattern[0]
        self.moves_pattern.rotate(-1)
        return self.nextUp

    def winCheck(self):
        # one
        if (self.buttonIn1.get() == "X" and self.buttonIn2.get() == "X" and self.buttonIn3.get() == "X") or (self.buttonIn4.get() == "X" and self.buttonIn5.get() == "X" and self.buttonIn6.get() == "X") or (self.buttonIn7.get() == "X" and self.buttonIn8.get() == "X" and self.buttonIn9.get() == "X") or (self.buttonIn1.get() == "X" and self.buttonIn4.get() == "X" and self.buttonIn7.get() == "X") or (self.buttonIn2.get() == "X" and self.buttonIn5.get() == "X" and self.buttonIn8.get() == "X") or self.buttonIn3.get() == "X" and self.buttonIn6.get() == "X" and self.buttonIn9.get() == "X" or (self.buttonIn1.get() == "X" and self.buttonIn5.get() == "X" and self.buttonIn9.get() == "X") or self.buttonIn3.get() == "X" and self.buttonIn5.get() == "X" and self.buttonIn7.get() == "X":

            self.X_or_O.set("X! Won")
            self.win_frame.tkraise()
            return True

        elif (self.buttonIn1.get() == "O" and self.buttonIn2.get() == "O" and self.buttonIn3.get() == "O") or (self.buttonIn4.get() == "O" and self.buttonIn5.get() == "O" and self.buttonIn6.get() == "O") or (self.buttonIn7.get() == "O" and self.buttonIn8.get() == "O" and self.buttonIn9.get() == "O") or (self.buttonIn1.get() == "O" and self.buttonIn4.get() == "O" and self.buttonIn7.get() == "O") or (self.buttonIn2.get() == "O" and self.buttonIn5.get() == "O" and self.buttonIn8.get() == "O") or self.buttonIn3.get() == "O" and self.buttonIn6.get() == "O" and self.buttonIn9.get() == "O" or (self.buttonIn1.get() == "O" and self.buttonIn5.get() == "O" and self.buttonIn9.get() == "O") or (self.buttonIn3.get() == "O" and self.buttonIn5.get() == "O" and self.buttonIn7.get() == "O"):

            self.X_or_O.set("O! Won")
            self.win_frame.tkraise()
            return True

    def drawCheck(self):
        if self.winCheck() == True:
            pass
        else:
            if self.buttonIn1.get() != "" and self.buttonIn2.get() != "" and self.buttonIn3.get() != "" and self.buttonIn4.get() != "" and self.buttonIn5.get() != "" and self.buttonIn6.get() != "" and self.buttonIn7.get() != "" and self.buttonIn8.get() != "" and self.buttonIn9.get() != "":
                self.draw_frame.tkraise()

    def buttonOne(self):
        self.place_XO()
        self.buttonIn1.set(self.nextUp)
        self.button_1["state"] = "disabled"
        self.count += 1
        self.winCheck()
        self.drawCheck()
        return self.count

    def buttonTwo(self):
        self.place_XO()
        self.buttonIn2.set(self.nextUp)
        self.button_2["state"] = "disabled"
        self.count += 1
        self.winCheck()
        self.drawCheck()
        return self.count

    def buttonThree(self):
        self.place_XO()
        self.buttonIn3.set(self.nextUp)
        self.button_3["state"] = "disabled"
        self.count += 1
        self.winCheck()
        self.drawCheck()
        return self.count

    def buttonFour(self):
        self.place_XO()
        self.buttonIn4.set(self.nextUp)
        self.button_4["state"] = "disabled"
        self.count += 1
        self.winCheck()
        self.drawCheck()
        return self.count

    def buttonFive(self):
        self.place_XO()
        self.buttonIn5.set(self.nextUp)
        self.button_5["state"] = "disabled"
        self.count += 1
        self.winCheck()
        self.drawCheck()
        return self.count

    def buttonSix(self):
        self.place_XO()
        self.buttonIn6.set(self.nextUp)
        self.button_6["state"] = "disabled"
        self.count += 1
        self.winCheck()
        self.drawCheck()
        return self.count

    def buttonSeven(self):
        self.place_XO()
        self.buttonIn7.set(self.nextUp)
        self.button_7["state"] = "disabled"
        self.count += 1
        self.winCheck()
        self.drawCheck()
        return self.count

    def buttonEight(self):
        self.place_XO()
        self.buttonIn8.set(self.nextUp)
        self.button_8["state"] = "disabled"
        self.count += 1
        self.winCheck()
        self.drawCheck()
        return self.count

    def buttonNine(self):
        self.place_XO()
        self.buttonIn9.set(self.nextUp)
        self.button_9["state"] = "disabled"
        self.count += 1
        self.winCheck()
        self.drawCheck()
        return self.count

    # /Button functions


app = Game()
app.mainloop()

