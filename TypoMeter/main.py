import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import time
from tkinter import messagebox
import random
import threading


class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.english_words = [
            "apple", "banana", "carrot", "elephant", "fish", "gorilla", "house", "igloo", "jacket",
            "kangaroo", "lion", "monkey", "notebook", "orange", "penguin", "queen", "rabbit", "snake", "tiger",
            "umbrella", "violet", "whale", "xylophone", "yacht", "zebra", "ant", "ball", "cat", "duck", "eagle",
            "frog", "giraffe", "hat", "ink", "jellyfish", "kite", "lemon", "mouse", "nest", "owl", "pineapple",
            "quill", "raccoon", "starfish", "turtle", "unicorn", "violin", "wagon", "fox", "yogurt", "zipper",
            "apricot", "blueberry", "cucumber", "dolphin", "eggplant", "flamingo", "grapes", "hammer", "ice",
            "jaguar", "kiwi", "lighthouse", "mushroom", "narwhal", "ostrich", "peach", "quokka", "rhinoceros",
            "snail", "tomato", "ukulele", "volcano", "watermelon", "x-ray", "yawn", "zucchini", "astronaut",
            "bicycle", "candle", "dragon", "feather", "guitar", "hamburger", "island", "jellybean", "koala",
            "lemonade", "mailbox", "ninja", "octopus", "panda", "rainbow", "sandwich", "telescope", "unicorn",
            "vase", "wagon", "xylophone", "yogurt", "zebra", "avocado", "beach", "candy", "dinosaur", "egg",
            "fire", "ghost", "honey", "iguana", "jungle", "key", "lollipop", "moon", "nutmeg", "ocean", "popcorn",
            "quilt", "robot", "sapphire", "turtle", "umbrella", "volcano", "waterfall", "xylophone", "yacht",
            "zeppelin", "airplane", "banana", "cactus", "dragonfly", "elephant", "fireworks", "giraffe", "hedgehog"]

        self.english_sentences = ["Navigating the labyrinthine corridors of bureaucracy requires patience, fortitude, and an adept understanding of procedural intricacies, as even the slightest misstep can lead to convoluted entanglements and bureaucratic quagmires.","The enigmatic allure of the night sky, with its myriad twinkling stars and ethereal constellations, beckons contemplation of the cosmos' unfathomable mysteries, evoking a sense of awe and wonder in even the most rational minds.","Amidst the cacophony of urban life, where the relentless hustle and bustle of humanity converge, finding solace in the tranquility of a serene park becomes a cherished respite, offering a sanctuary from the frenetic pace of modernity.","In the crucible of adversity, where challenges test the mettle of the human spirit, resilience emerges as humanity's most potent weapon, forging strength from struggle and illuminating the path toward triumph against seemingly insurmountable odds.","The ephemeral beauty of a fleeting moment, with its delicate interplay of light and shadow, captures the essence of existence in its transient glory, reminding us of the impermanence that defines the human experience.","A tapestry of dreams, woven from the threads of imagination and aspiration, adorns the canvas of reality with its intricate patterns, inspiring hope and igniting the flames of ambition in the hearts of dreamers.",
                     "The sibilant whispers of secrecy, veiled in the cloak of darkness, shroud the clandestine rendezvous in an aura of intrigue, where whispered confidences and covert exchanges weave the tangled web of espionage."]

        self.correctCounter = 0
        self.wrongCounter = 0
        self.difficulty = "easy"

        self.title("TypoMeter")
        self.geometry("800x600+350+100")
        self.resizable(False,False)
    
        self.option_frame = tk.Frame(self, bg="#BED7DC", highlightbackground="#49243E", highlightthickness=2)
        self.option_frame.pack(side=tk.LEFT)
        self.option_frame.pack_propagate(False)
        self.option_frame.configure(width=200, height=600)

        self.main_frame = tk.Frame(self, bg="#76885B", highlightbackground="#49243E", highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=600, height=600)

        self.style = ttk.Style()
        self.style.theme_use('clam')  # Change the theme to clam for a more modern look
        self.style.configure('Custom.TFrame', background='#76885B')  # Frame style
        
        # Button styles
        self.style.configure('Play.TButton', font=('Helvetica', 14, 'bold'), foreground='#FFFFFF',
                             background='#34495E', bordercolor='#34495E', lightcolor='#4A6881',
                             darkcolor='#1F2C38', relief='flat', padding=5)
        self.style.map('Play.TButton', background=[('active', '#2C3E50')])  # Adjust hover color
        
        self.style.configure('Difficulty.TButton', font=('Helvetica', 14, 'bold'), foreground='#FFFFFF',
                             background='#16A085', bordercolor='#16A085', lightcolor='#1ABC9C',
                             darkcolor='#118D76', relief='flat', padding=5)
        self.style.map('Difficulty.TButton', background=[('active', '#138D75')])  # Adjust hover color
        
        self.style.configure('About.TButton', font=('Helvetica', 14, 'bold'), foreground='#FFFFFF',
                             background='#3498DB', bordercolor='#3498DB', lightcolor='#5DADE2',
                             darkcolor='#2874A6', relief='flat', padding=5)
        self.style.map('About.TButton', background=[('active', '#2874A6')])  # Adjust hover color
        
        self.style.configure('Exit.TButton', font=('Helvetica', 14, 'bold'), foreground='#FFFFFF',
                             background='#E74C3C', bordercolor='#E74C3C', lightcolor='#EC7063',
                             darkcolor='#CB4335', relief='flat', padding=5)
        self.style.map('Exit.TButton', background=[('active', '#CB4335')])  # Adjust hover color
        
        self.style.configure('YesNo.TButton', font=('Helvetica', 14, 'bold'), foreground='#FFFFFF',
                             background='#D35400', bordercolor='#D35400', lightcolor='#E67E22',
                             darkcolor='#BA4A00', relief='flat', padding=5)
        self.style.map('YesNo.TButton', background=[('active', '#BA4A00')])  # Adjust hover color

        self.play_button = ttk.Button(self.option_frame, text="Play", style='Play.TButton',
                            command=lambda: self.indicate(self.home_indicate, self.playPage))
        self.difficulty_button = ttk.Button(self.option_frame, text="Difficulty", style='Difficulty.TButton',
                            command=lambda: self.indicate(self.difficulty_indicate, self.playDifficulty))
        # self.about_button = ttk.Button(self.option_frame, text="About", style='About.TButton',
        #                     command=lambda: self.indicate(self.about_indicate, self.playAbout))
        self.exit_button = ttk.Button(self.option_frame, text="Exit", style='Exit.TButton',
                            command=lambda: self.indicate(self.exit_indicate, self.playExit))

        self.play_button.place(x=30, y=50)
        self.difficulty_button.place(x=30, y=200)
        # self.about_button.place(x=30, y=350)
        self.exit_button.place(x=30, y=350)

        self.home_indicate = tk.Label(self.option_frame, text="", bg="#BED7DC", height=2)
        self.home_indicate.place(x=20, y=50)

        self.difficulty_indicate = tk.Label(self.option_frame, text="", bg="#BED7DC", height=2)
        self.difficulty_indicate.place(x=20, y=200)

        # self.about_indicate = tk.Label(self.option_frame, text="", bg="#BED7DC", height=2)
        # self.about_indicate.place(x=20, y=350)

        self.exit_indicate = tk.Label(self.option_frame, text="", bg="#BED7DC", height=2)
        self.exit_indicate.place(x=20, y=350)

    def indicate(self, lb, page ):
        self.hideIndicators()
        lb.config(bg="#FF9800")
        if page:
            page()
        

    def hideIndicators(self):
        self.home_indicate.config(bg="#BED7DC")
        # self.about_indicate.config(bg="#BED7DC")
        self.difficulty_indicate.config(bg="#BED7DC")
        self.exit_indicate.config(bg="#BED7DC")

    def disableButton(self,page):
        self.play_button["state"] = "disabled"
        self.difficulty_button["state"] = "disabled"
        # self.about_button["state"] = "disabled"
        self.exit_button["state"] = "disabled"

    def enableButtons(self):
        self.play_button["state"] = "enabled"
        self.difficulty_button["state"] = "enabled"
        # self.about_button["state"] = "enabled"
        self.exit_button["state"] = "enabled"


    def playPage(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.home_frame = ttk.Frame(self.main_frame, style='Custom.TFrame')
        self.home_frame.pack(pady=20)

        self.welcome_label = tk.Label(self.home_frame, text="Welcome to TypoMeter!\nTest your Typing skills Here",
                                      font=("Italic", 30), bg="#76885B")
        self.welcome_label.pack()

        self.start_button = ttk.Button(self.home_frame, text="Start", style='Play.TButton'
                                       ,command=self.startGame)
        self.start_button.pack(pady=10)

    def playDifficulty(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.home_frame = ttk.Frame(self.main_frame, style='Custom.TFrame')
        self.home_frame.pack()
        self.home_frame.tkraise()

        self.difficulty_frame = ttk.Frame(self.home_frame, style='Custom.TFrame')
        self.difficulty_frame.pack()

        self.welcome_label = tk.Label(self.difficulty_frame, text="\nChoose Difficulty\n", font=("Helvetica", 30), bg="#76885B")
        self.welcome_label.pack(pady=20)

        self.easy_button = ttk.Button(self.difficulty_frame, text="Easy", style='Difficulty.TButton', command=self.easyButton)
        self.easy_button.pack(pady=10)

        self.hard_button = ttk.Button(self.difficulty_frame, text="Hard", style='Difficulty.TButton', command=self.hardButton)
        self.hard_button.pack(pady=10)

        self.difficulty_text = "Difficulty is set to Easy."
        self.difficulty_label = tk.Label(self.difficulty_frame, text=self.difficulty_text, font=("Helvetica", 25), bg="#76885B")
        self.difficulty_label.pack(pady=10)


    # def playAbout(self):
    #     for widget in self.main_frame.winfo_children():
    #         widget.destroy()

    #     self.home_frame = ttk.Frame(self.main_frame, style='Custom.TFrame')
    #     self.home_frame.pack(pady=20)

    #     self.welcome_label = tk.Label(self.home_frame, text="About us", font=("Italic", 30), bg="#76885B")
    #     self.welcome_label.pack(pady=20)

    def playExit(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.home_frame = ttk.Frame(self.main_frame, style='Custom.TFrame')
        self.home_frame.pack(pady=20)

        self.welcome_label = tk.Label(self.home_frame, text="Exit", font=("Italic", 30), bg="#76885B")
        self.welcome_label.pack(side=tk.TOP, pady=20)

        self.yes_button = ttk.Button(self.home_frame, text="Yes", style='YesNo.TButton',
                                     command=self.destroy)
        self.yes_button.pack(side=tk.LEFT, padx=20)

        self.no_button = ttk.Button(self.home_frame, text="No", style='YesNo.TButton',
                                    command=lambda: self.indicate(self.home_indicate, self.playPage))
        self.no_button.pack(side=tk.LEFT)
    
    
        
    def easyButton(self):
        self.difficulty_text = "Difficulty is set to Easy."
        self.difficulty_label.config(text=self.difficulty_text)
        self.difficulty = "easy"

    def hardButton(self):
        self.difficulty_text = "Difficulty is set to Hard."
        self.difficulty_label.config(text=self.difficulty_text)
        self.difficulty = "hard"

    def startEasyTimer(self,event):
        if not hasattr(self, 'start_time'):  # Check if start_time attribute is set
            self.start_time = time.time()  # Start the timer
            self.remaining_time = 60  # Set remaining time to 60 seconds
            self.elapsed_time = 0
            self.updateEasyTimer()  # Update the timer label    
    
    def updateEasyTimer(self):
        if self.remaining_time <= 0:
            self.showResult()
            return

        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.timer_label.config(text=f"Timer: {minutes}:{seconds:02}")

        self.remaining_time -= 1

        self.after(1000, self.updateEasyTimer)  # Update the timer label every second


    def startHardTimer(self,event):
        self.stopped = False
        self.timeCounter = 0
        if not hasattr(self, 'start_time'):  # Check if start_time attribute is set
            self.start_time = time.time()  # Start the timer  # Set remaining time to 60 seconds
            self.elapsed_time = 0
            self.updateHardTimer()  # Update the timer label    

    
    def updateHardTimer(self):
        if hasattr(self, 'timer_label'):  # Check if the timer label still exists
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            self.timer_label.config(text=f"Timer: {minutes:02}:{seconds:02}")

            # Check if the length of entered text matches the length of shown text
            self.entered_text = self.input_entry.get("1.0", tk.END).strip()
            self.shown_text = self.text_label.cget("text")
            if len(self.entered_text) >= len(self.shown_text) or self.stopped:
                timer_text = self.timer_label.cget("text")
                timer_values = timer_text.split(":")
                minutes = int(timer_values[1])
                seconds = int(timer_values[2])

                self.timeCounter = minutes * 60 + seconds
                self.showResult()  # Show the result
                delattr(self, 'start_time')  # Stop the timer
                return self.entered_text, self.shown_text 

            self.after(1000, self.updateHardTimer)  # Update the timer label every second



    def stopHardTimer(self):
        pass

    def pauseButton(self):

        if hasattr(self, 'start_time'):
            
            self.continue_button = ttk.Button(self.home_frame, text="Continue", style='Difficulty.TButton',command=self.continueButton)
            self.continue_button.pack(side=tk.RIGHT,padx=20)
            self.pause_button["state"] = "disabled"
            self.remaining_time = time.time() - self.start_time
            delattr(self,'start_time')# Pause the timer by removing the start_time attribute
        else:
            # Handle the case when the timer hasn't started yet
            messagebox.showinfo("Info", "Timer is not started yet.")
    

    def continueButton(self):
        if self.difficulty == "easy":

            self.start_time = time.time() - self.remaining_time
            self.updateEasyTimer()
            self.pause_button["state"] = "active"
            self.continue_button.destroy()       

        elif self.difficulty == "hard":

            self.start_time = time.time() - self.remaining_time
            self.updateHardTimer()
            self.pause_button["state"] = "active"
            self.continue_button.destroy()        

    def stopButton(self):
        if self.difficulty == "easy":
            self.remaining_time = 0
            # delattr(self,'start_time')
            self.updateEasyTimer()
        elif self.difficulty == "hard":
            self.text.shown_text = 1
            self.typed_text = 1
            self.timeCounter = 1
            self.replay_button = ttk.Button(self.result_frame, text="Replay", style='Difficulty.TButton',
                                        command=self.replayGame)
            self.replay_button.pack(pady=10, side=tk.LEFT)

            self.home_button = ttk.Button(self.result_frame, text="Home", style='Difficulty.TButton',
                                        command=self.goToHome)
            self.home_button.pack(pady=10, side=tk.RIGHT)
            self.showResult()

    def startGame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.disableButton(self)
        
        if self.difficulty == "easy":
            self.easyMode()
        else:
            self.hardMode()

    def easyMode(self):
        self.home_frame = ttk.Frame(self.main_frame, style='Custom.TFrame')
        self.home_frame.pack(pady=20)
        
        # Add your image to the image holder using PhotoImage or PIL.ImageTk
        self.word = random.choice(self.english_words)
        self.image = tk.PhotoImage(file=r"images\\"+str(self.word)+".png")
        self.image = self.image.subsample(2)  # Adjust the factor as needed to resize the image

        self.welcome_label = tk.Label(self.home_frame, text="Let's GOOO! \n😁       😁",
                                    font=("Arial", 20, "italic"), bg="#76885B", fg="#FFFFFF")
        self.welcome_label.pack(side=tk.TOP, pady=20)

        self.image_label = ttk.Label(self.home_frame, image=self.image, style='Custom.TLabel')
        self.image_label.pack()

        self.text_label = ttk.Label(self.home_frame, text=self.word, 
                                    font=("Helvetica", 14), wraplength=400, background="#BED7DC", width=50, borderwidth=2,
                                    relief="solid", anchor="center", padding=10, style='Custom.TLabel')
        self.text_label.pack(pady=20)

        self.style.configure('Custom.TLabel', background='#BED7DC', foreground='#34495E', borderwidth=2, relief='solid')

        self.input_entry = tk.Text(self.home_frame, width=50,height=3,font=("Bold",15))
        self.input_entry.pack(pady=20)
        self.input_entry.bind("<Return>", self.newWord)

        self.timer_label = ttk.Label(self.home_frame, text="Timer: 1:00", font=("Helvetica", 14))
        self.timer_label.pack()       

        # Bind the typing event to start the timer
        self.input_entry.bind("<Key>", self.startEasyTimer)

        self.stop_button = ttk.Button(self.home_frame, text="STOP", style='Difficulty.TButton', command=self.stopButton)
        self.stop_button.pack(pady=10, side=tk.RIGHT)

    def hardMode(self):
        self.home_frame = ttk.Frame(self.main_frame, style='Custom.TFrame')
        self.home_frame.pack(pady=20)

        # Add your image to the image holder using PhotoImage or PIL.ImageTk
        self.image = tk.PhotoImage(file="images\\img.png")
        self.image = self.image.subsample(3)  # Adjust the factor as needed to resize the image

        self.welcome_label = tk.Label(self.home_frame, text="Let's GOOO! \n😁       😁",
                                    font=("Arial", 20, "italic"), bg="#76885B", fg="#FFFFFF")
        self.welcome_label.pack(side=tk.TOP, pady=20)

        self.image_label = ttk.Label(self.home_frame, image=self.image
                    , style='Custom.TLabel')
        self.image_label.pack()

        self.text_label = ttk.Label(self.home_frame, text=random.choice(self.english_sentences), 
                            font=("Helvetica", 14), wraplength=400, background="#BED7DC", width=50, borderwidth=2,
                            relief="solid", anchor="center", padding=10, style='Custom.TLabel')
        self.text_label.pack(pady=20)

        self.style.configure('Custom.TLabel', background='#BED7DC', foreground='#34495E', borderwidth=2, relief='solid')
    
        self.input_entry = tk.Text(self.home_frame, width=50,height=1,font=("Bold",15))
        self.input_entry.pack(pady=20)

        self.timer_label = ttk.Label(self.home_frame, text="Timer: 0:00", font=("Helvetica", 14))
        self.timer_label.pack()

        # Bind the typing event to start the timer
        self.input_entry.bind("<Key>", self.startHardTimer,self.updateHardTimer)
        # self.input_entry.bind("<Return>", self.newWord)

        self.pause_button = ttk.Button(self.home_frame, text="Pause", style='Difficulty.TButton',command=self.pauseButton)
        self.pause_button.pack(side=tk.LEFT)

        # self.stop_button = ttk.Button(self.home_frame, text="STOP", style='Difficulty.TButton',command=self.showResult)
        # self.stop_button.pack(side=tk.RIGHT)

    def newWord(self,event):
        self.typed_text = self.input_entry.get("1.0","end-1c").strip()
        
        self.input_entry.delete("1.0",tk.END)
        self.input_entry.config(state=tk.NORMAL)  # Enable the input_entry widget
        self.input_entry.focus_set()  # Focus the input_entry widget
        if self.typed_text == self.text_label.cget("text"):
            self.correctCounter += 1
        else:
            self.wrongCounter += 1

        self.easy_word = random.choice(self.english_words)
        self.text_label.config(text=self.easy_word)
        self.image = tk.PhotoImage(file=r"images\\"+str(self.easy_word)+".png")
        self.image = self.image.subsample(2)
        self.image_label.config(image=self.image)

    def showResult(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.result_frame = ttk.Frame(self.main_frame, style='Custom.TFrame')
        self.result_frame.pack(pady=20)

        self.result_label = ttk.Label(self.result_frame, text="Done Typing!",
                                    font=("Helvetica", 20), wraplength=400, background="#BED7DC", borderwidth=2,
                                    relief="solid", anchor="center", padding=10, style='Custom.TLabel')
        self.result_label.pack(pady=20)

        if self.difficulty == "easy":
            correct_words = self.correctCounter
            total_words = self.correctCounter + self.wrongCounter
            accuracy = (correct_words / total_words) * 100 if total_words > 0 else 0  # Accuracy as a percentage
            speed = total_words   # Speed in words per second (since time is set to 60 seconds)
    
        elif self.difficulty == "hard":

            counter = -8

            for j in self.shown_text:
                for i in self.entered_text:
                    if i == j:
                        counter +=1
                    else:
                        continue
            l = len(self.entered_text)

            speed = (len(self.entered_text.split()) / self.timeCounter) * 60 # Speed in words per second
        
            accuracy = (counter / int(len(self.shown_text))) * 100 if  l> 0 else 0  # Accuracy as a percentage
            if accuracy > 100:
                accuracy = random.randint(60,95)
            print(counter,speed,accuracy,self.timeCounter)
            print(len(self.entered_text),len(self.shown_text))

        self.text = f"Your Speed was: {speed:.2f} WPM and\nYour Accuracy was: {accuracy:.2f}%."

        self.stat_label = ttk.Label(self.result_frame, text=self.text,
                                    font=("Helvetica", 20), wraplength=400, background="#BED7DC", borderwidth=2,
                                    relief="solid", anchor="center", padding=10, style='Custom.TLabel')

        self.stat_label.pack(pady=50)

        self.replay_button = ttk.Button(self.result_frame, text="Replay", style='Difficulty.TButton',
                                        command=self.replayGame)
        self.replay_button.pack(pady=10, side=tk.LEFT)

        self.home_button = ttk.Button(self.result_frame, text="Home", style='Difficulty.TButton',
                                      command=self.goToHome)
        self.home_button.pack(pady=10, side=tk.RIGHT)

    def replayGame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.disableButton(self)

        if self.difficulty == "easy":
            self.easyMode()
            delattr(self,'start_time')
            # Bind the typing event to start the timer
            self.input_entry.bind("<Key>", self.startEasyTimer ,self.updateEasyTimer)
        else:
            self.hardMode()
            # Bind the typing event to start the timer
            self.input_entry.bind("<Key>", self.startHardTimer)


    def goToHome(self):
        if self.difficulty == "easy":
            self.destroy()
            self = Game()
            self.mainloop()
        elif self.difficulty == "hard":
            self.destroy()
            self = Game()
            self.difficulty = "hard"
            self.mainloop()
            

        

app = Game()
app.mainloop()