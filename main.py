from tkinter import *
import time

window = Tk()
window.title("Typing Speed Test")
window.minsize(width=700, height=500)
window.config(bg="#f0f0f0")


def onClick(event=None):
    curr_time = time.time()
    countdown(curr_time)
    if posttext.get("1.0", "end-1c") == "Start typing...":
        posttext.delete("1.0", "end")


def offClick():
    if posttext.get("1.0", "end-1c") == " ":
        posttext.insert("1.0", "Start typing...")


def countdown(curr_time):
    time_left = (curr_time + 60) - time.time()
    if time_left > 0:
        timer.config(text=str(int(time_left)))
        window.after(1000, countdown,curr_time)
    else:
        timer.config(text="Time's Up")
        speed()

def highlight_error(event=None):
    entered_text = posttext.get("1.0","end-1c").split()
    pretext_text = pretext.split()

    textbox.tag_remove("current_word", "1.0", "end")
    textbox.tag_remove("error", "1.0", "end")

    correct = 0

    for i,(entered_word,correct_word) in enumerate(zip(entered_text,pretext_text)):
        word_start = f"{posttext.search(entered_word,'1.0','end')}"
        word_end = f"{word_start}+{len(entered_word)}c"

        if entered_word == correct_word:
            correct+=1
        else:
            posttext.tag_add("error",word_start,word_end)
            posttext.tag_config("error", background="red", foreground="white")




def speed():
    entered_text = posttext.get("1.0", "end-1c").split()
    posttext.delete("1.0", "end-1c")
    correct = 0
    for i, j in zip(entered_text, pretext.split()):
        if i == j:
            correct += 1

    typing_speed = correct / 1

    user_speed.config(text=f"Your speed = {typing_speed} WPM")


# Header
header = Label(text="Typing Speed Test", font=('Arial', 24, 'bold'), bg="#f0f0f0")
header.grid(row=0, column=0, padx=10, pady=20)

# Timer
timer = Label(text="60", font=('Arial', 20, 'bold'), bg="#f0f0f0", fg="#d9534f")
timer.grid(row=1, column=0, padx=10, pady=10)

# Instructions
instructions = Label(text="Type the text below to start the timer.", font=('Arial', 14), bg="#f0f0f0")
instructions.grid(row=2, column=0, padx=10, pady=10)

# Textbox for predefined text
textbox = Text(height=8, width=100, font=('Calibri', 13), bg="#ffffff", wrap="word")
textbox.grid(row=3, column=0, padx=10, pady=10)

pretext = "Began where war both write point before more class me unit ten house at red object complete late eat think four way nine fine between canany front remember behind once is land pound beauty cover form ready laugh north you has never sound plane box"
textbox.insert('1.0', pretext)
textbox.config(state=DISABLED)  # Make it read-only

# Textbox for user input
posttext = Text(height=8, width=100, font=('Arial', 13), bg="#ffffff", wrap="word")
posttext.grid(row=4, column=0, padx=10, pady=10)
posttext.insert("1.0", "Start typing...")

# Bind focus events
posttext.bind("<FocusIn>", onClick)
posttext.bind("<FocusOut>", offClick)
posttext.bind("<space>", highlight_error)


# User speed display
user_speed = Label(height=2, width=30, font=('Arial', 16, 'bold'), bg="#f0f0f0", fg="#5bc0de")
user_speed.grid(row=5, column=0, padx=10, pady=20)

# Predefined text for typing
pretext = "Began where war both write point before more class me unit ten house at red object complete late eat think four way nine fine between canany front remember behind once is land pound beauty cover form ready laugh north you has never sound plane box"

# Start the tkinter main event loop
window.mainloop()