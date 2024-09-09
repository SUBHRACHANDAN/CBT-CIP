import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Rock, Paper, Scissors", font=("Helvetica", 18, "bold")).pack(pady=20)

        # Button styles
        button_style = {"font": ("Helvetica", 14), "width": 15, "height": 2}

        # Rock button
        tk.Button(self.root, text="Rock", bg="lightcoral", fg="white", command=lambda: self.play("Rock"), **button_style).pack(pady=10)
        # Paper button
        tk.Button(self.root, text="Paper", bg="lightblue", fg="black", command=lambda: self.play("Paper"), **button_style).pack(pady=10)
        # Scissors button
        tk.Button(self.root, text="Scissors", bg="lightgreen", fg="black", command=lambda: self.play("Scissors"), **button_style).pack(pady=10)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
        else:
            result = "You Lose!"

        result_message = f"You chose: {user_choice}\nComputer chose: {computer_choice}\nResult: {result}"
        self.result_label.config(text=result_message)
        messagebox.showinfo("Game Result", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()



