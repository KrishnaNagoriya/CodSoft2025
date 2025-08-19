import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("350x400")

# Global scores
user_score = 0
computer_score = 0

# Game options
options = ["Rock", "Paper", "Scissors"]

# Functions
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(options)
    
    user_choice_label.config(text="You chose: " + user_choice)
    computer_choice_label.config(text="Computer chose: " + computer_choice)

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_label.config(text="Result: " + result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Title label
title = tk.Label(root, text="Rock - Paper - Scissors", font=("Arial", 16, "bold"))
title.pack(pady=20)

# Choice buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Labels to show choices
user_choice_label = tk.Label(root, text="You chose: ", font=("Arial", 12))
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
computer_choice_label.pack(pady=10)

# Result
result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Score
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", width=15)
exit_button.pack(pady=15)

# Run the app
root.mainloop()
