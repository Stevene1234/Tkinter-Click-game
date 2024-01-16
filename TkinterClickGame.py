import tkinter as tk
import time
import threading

class ClickCounter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Click Counter")
        self.root.geometry('200x200')

        self.click_count = 0
        self.high_score = 0
        self.initials = ""

        self.initials_label = tk.Label(self.root, text="Initials:")
        self.initials_label.pack()

        self.initials_entry = tk.Entry(self.root, width=3)
        self.initials_entry.pack()

        self.label = tk.Label(self.root, text="Clicks: 0")
        self.label.pack()

        self.button = tk.Button(self.root, text="Click me!", command=self.increment_click_count)
        self.button.pack()

        self.timer = tk.Label(self.root, text="10")
        self.timer.pack()

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again)
        self.play_again_button.pack()

        self.high_score_label = tk.Label(self.root, text=f"High Score: {self.high_score}")
        self.high_score_label.pack()

        self.start_countdown()

    def increment_click_count(self):
        self.click_count += 1
        self.label.config(text=f"Clicks: {self.click_count}")

    def start_countdown(self):
        def countdown():
            for i in range(10, -1, -1):
                self.timer.config(text=str(i))
                time.sleep(1)

            self.game_over()

        thread = threading.Thread(target=countdown)
        thread.start()

    def game_over(self):
        self.button.config(state=tk.DISABLED)
        self.label.config(text=f"Your score: {self.click_count}")

        if self.click_count > self.high_score:
            self.high_score = self.click_count
            self.high_score_label.config(text=f"High Score: {self.high_score}")

            if self.click_count > self.high_score:
                message = tk.Message(self.root, text="WOW! New high score!", font=("Arial", 24), bg="green")
                message.pack()

            self.initials = self.initials_entry.get()
            self.high_score_label.config(text=f"High Score: {self.high_score} ({self.initials})")

    def play_again(self):
        self.click_count = 0
        self.label.config(text="Clicks: 0")
        self.button.config(state=tk.NORMAL)
        self.start_countdown()

click_counter = ClickCounter()
click_counter.root.mainloop()