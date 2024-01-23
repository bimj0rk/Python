from tkinter import Tk
from tkinter import messagebox, simpledialog

root = Tk()
root.withdraw()

userInput = simpledialog.askstring("PASSWORD: ", "PASSWORD: ")

if userInput == "teiubesc":

    messagebox.showinfo("Heyyyyy", "Hey!!11",)
    messagebox.showinfo("Question...", "I have a question...")
    messagebox.showinfo("Question...", "A really important one...")
    messagebox.showinfo("Question...", "Do you...")
    messagebox.showinfo("Question...", "...want to be...")
    response = messagebox.askyesno("Please?", "MY VALENTINE???")

    if response:  # User clicked 'OK'
        messagebox.showinfo("HappyHappyHappy", "YIPPIE!!!!111 Check the card")
    else:  # User clicked 'Cancel'
        messagebox.showinfo(":/", "Bollocks.")

else:
    messagebox.showinfo("Nuh Uh", "Wrong password...")