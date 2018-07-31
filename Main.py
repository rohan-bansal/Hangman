import tkinter as tk
import random, sys, time


countries = ["United States", "United Kingdom", "India", "Russia", "China", "Brazil", "Scotland", "Switzerland", "Egypt", "Japan"]
things = ["clock", "jazz", "hangman", "grapes", "cushion", "foot", "quadrupeds", "beetle", "lamp post", "pigment", "dictionary", "java", "dragon", "pixel art", "development", "laptop"]
beforeNafter = ["Glass of Water Buffalo", "A Long Shot in the Dark", "Air Force One in a Million", "Bundle of Joy to the World", "Cake Batter Up", "Cat Food for Thought"]
BookTitles = ["Wrhinkle in Time", "Catching Fire", "Harry Potter", "Maze Runner", "Percy Jackson", "Divergent", "Insurgent", "Allegiant", "Call of the Wild", "Geronimo Stilton", "Owly"]
RhymeTime = ["A Locket in Your Pocket", "Snail and a Whale", "Beat the Heat", "Double Trouble", "Fat Cat", "Hocus Pocus", "Snail Mail", "Monster Mash"]

choices = [
    "Countries",
    "Things",
    "Before and After",
    "Book Titles",
    "RhymeTime"
]

class playGame():
    def __init__(self, category, root, displayLabel, announcer, canvas, destroyB):
        self.category = category
        self.announcer = announcer
        self.canvas = canvas
        self.destroy = destroyB
        self.word = self.getWord()
        self.displayLabel = displayLabel
        self.letters = []
        self.used = []
        self.misses = 0
        self.displayWord()

    def getWord(self):
        if(self.category == 0):
            self.announcer.config(text = "Remember to Capitalize the first letter of each word!\n(except for 'of, in, the, a, to, for, and')")
            return random.choice(countries)
        elif(self.category == 1):
            return random.choice(things)
        elif(self.category == 2):
            self.announcer.config(text = "Remember to Capitalize the first letter of each word!\n(except for 'of, in, the, a, to, for, and')")
            return random.choice(beforeNafter)
        elif(self.category == 3):
            self.announcer.config(text = "Remember to Capitalize the first letter of each word!\n(except for 'of, in, the, a, to, for, and')")
            return random.choice(BookTitles)
        elif(self.category == 4):
            self.announcer.config(text = "Remember to Capitalize the first letter of each word!\n(except for 'of, in, the, a, to, for, and')")
            return random.choice(RhymeTime)

    def displayWord(self):
        for x in range(len(self.word)):
            if(self.word[x] == " "):
                self.letters.append("    ")
            else:
                self.letters.append("_ ")
        self.displayLabel.config(text = "".join(self.letters))

    def guessLetter(self, letter):
        if(letter in self.used):
            self.announcer.config(text = "You already used this letter!", fg = "red")
            return
        if(len(letter) > 1):
            if(letter == self.word):
                self.displayLabel.config(text = self.word)
                self.announcer.config(text = "You Won! Restart the app to play again.", fg = "green")
            else:
                self.announcer.config(text = "Guess Incorrect.", fg = "red")
                self.used.append(letter)
                self.misses += 1
                self.drawHangman()
                return
        else:
            if(letter in self.word):
                for element in range(len(self.word)):
                    if(self.word[element] == letter):
                        self.letters[element] = self.word[element] + " "
                self.displayLabel.config(text = "".join(self.letters))  
                if("".join("".join(self.letters).split(" ")) == self.word):
                    self.displayLabel.config(text = self.word)
                    self.announcer.config(text = "You Won! Restart the app to play again.", fg = "green")
                else:
                    self.announcer.config(text = "Successful Guess!", fg = "green") 
                    self.used.append(letter)
                    return
            else:    
                self.announcer.config(text = "Guess Incorrect.", fg = "red")
                self.used.append(letter)
                self.misses += 1
                self.drawHangman()
                return

    def drawHangman(self):
        if self.misses == 1:
            self.canvas.create_oval(160, 60, 210, 105, width = 5, fill = "burlywood") #head
        elif self.misses == 2:
            self.canvas.create_line(185, 107, 185, 170, width = 10, fill = "black") #body
        elif self.misses == 3:
            self.canvas.create_line(185, 165, 165, 190, 160, 210, width = 10, fill = "black") #left leg
        elif self.misses == 4:
            self.canvas.create_line(185, 165, 190, 190, 200, 210, width = 10, fill = "black") # right leg
        elif self.misses == 5:
            self.canvas.create_line(185, 130, 165, 132, 160, 152, width = 10, fill = "black") # left arm
        elif self.misses == 6:
            self.canvas.create_line(185, 130, 205, 132, 210, 152, width = 10, fill = "black") # right arm
        elif self.misses == 7:
            self.canvas.create_oval(170, 80, 172, 82, width = 3, fill = "blue") # left eyeball
            self.announcer.config(text = "Last Guess...", fg = "yellow")
        elif self.misses == 8:
            self.canvas.create_oval(200, 80, 198, 78, width = 3, fill = "blue") # right eyeball
            canvas.create_line(185, 25, 185, 60, fill = "maroon", width = 10)
            self.announcer.config(text = "You used up all your guesses! Restart the app to play again.", fg = "red")
            self.displayLabel.config(text = self.word)
            self.destroy.destroy()

window = tk.Tk()
window.title("Hangman")
window.geometry("500x500")
window.resizable(False, False)

choose = tk.Toplevel(window)
choose.title("Choose a Category")
choose.geometry("300x500")
choose.resizable(False, False)
category = tk.Label(choose, text = "Choose a Category: ", font = ("Comic Sans", 20)).grid(row = 0, column = 0)
v = tk.IntVar()
v2 = tk.StringVar()
word = ""

canvas = tk.Canvas(window, width = 450, height = 350)
canvas.place(x = 25, y = 10)
canvas.create_rectangle(10, 10, 435, 330, fill = "dark olive green")
canvas.create_line(50, 20, 50, 320, fill = "black", width = 10)
canvas.create_line(45, 320, 230, 320, fill = "black", width = 15)
canvas.create_line(45, 20, 190, 20, fill = "black", width = 10)
canvas.create_line(185, 25, 185, 60, fill = "grey", width = 10) # x = 185, y = 60

mystery = tk.Label(window, text = "", font = ("Comic Sans", 15))
mystery.place(relx = 0.5, rely = 0.8, anchor = "center")

announcetext = tk.Label(window, text = "")
announcetext.place(relx = 0.5, rely = 0.9, anchor = "center")

def callback1(e):
    try:
        hangman.guessLetter(e.get())
        v2.set("")
    except Exception:
        announcetext.config(text = "Select a Category!", fg = "red")

letter = tk.Entry(window, textvariable = v2)
ok = tk.Button(window, text = "Guess", command = lambda: callback1(letter))
ok.place(x = 330, y = 466)
letter.place(x = 160, y = 470)

def gameLoop(choice):
    global hangman 
    hangman = playGame(choice, window, mystery, announcetext, canvas, ok)

def getCategory(word):
    choose.destroy()
    word = v.get()
    gameLoop(word)
    



placeX = 60
for val, choice in enumerate(choices):
    tk.Radiobutton(choose, text=choice, variable=v, command=lambda: getCategory(word), value=val).place(x = 20, y = placeX)
    placeX += 30


window.mainloop()
