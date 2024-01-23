import ctypes

ctypes.windll.user32.MessageBoxW(0, "Hey!!11", "Heyyyyy", 0)
ctypes.windll.user32.MessageBoxW(0, "I have a question...", "Question...", 0)
ctypes.windll.user32.MessageBoxW(0, "A really important one...", "Question...", 0)
ctypes.windll.user32.MessageBoxW(0, "Do you...", "Question...", 0)
ctypes.windll.user32.MessageBoxW(0, "...want to be...", "Question...", 0)
response = ctypes.windll.user32.MessageBoxW(0, "MY VALENTINE???", "Please?", 1)

if response == 1:  # User clicked 'OK'
    ctypes.windll.user32.MessageBoxW(0, "YIPPIE!!!!111", "HappyHappyHappy", 0)
else:  # User clicked 'Cancel'
    ctypes.windll.user32.MessageBoxW(0, "Bollocks.", ":/", 0)
