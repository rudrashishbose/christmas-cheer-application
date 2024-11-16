"""
Christmas Cheer Application 🎄✨

This script creates a cheerful GUI application to spread holiday joy. The application includes:
- A "Cheers" button that, when clicked:
  - Plays a festive tune.
  - Shows a pop-up wishing a Merry Christmas.
- A text-to-speech greeting to enhance the festive experience.

Modules Used:
--------------
1. `time`: To manage delays if required for the tune or other operations.
2. `tkinter`: For creating the graphical user interface.
3. `messagebox` (from tkinter): For displaying the pop-up message.
4. `winsound`: To play the cheerful melody.
5. `pyttsx3`: For text-to-speech functionality.

How It Works:
-------------
1. Clicking the "Cheers" button:
   - Plays the "Jingle Bells" tune using `winsound.Beep`.
   - Displays a pop-up message: "Merry Christmas!".
   - Uses `pyttsx3` to say "Merry Christmas!" aloud.

Requirements:
-------------
- Python 3.7 or later.
- The `pyttsx3` module for text-to-speech.

Run the script:
---------------
1. Install dependencies if required (`pip install pyttsx3`).
2. Execute the script in a Python environment.
3. Enjoy the festive cheer!

Author: [Rudrashish Bose]
Version: 1.0
"""

import time
import tkinter as tk
from tkinter import messagebox
import winsound
import pyttsx3

# Text-to-speech initialization
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

# Notes and their frequencies
notes = {
    'C': 261,
    'D': 294,
    'E': 329,
    'F': 349,
    'G': 392,
    'A': 440,
    'B': 494,
}

# Jingle Bells melody
melody = [
    ('E', 400), ('E', 400), ('E', 800),
    ('E', 400), ('E', 400), ('E', 800),
    ('E', 400), ('G', 400), ('C', 400), ('D', 400), ('E', 800),
    ('F', 400), ('F', 400), ('F', 400), ('F', 400),
    ('F', 400), ('E', 400), ('E', 400), ('E', 400),
    ('E', 400), ('D', 400), ('D', 400), ('E', 400), ('D', 800),
]

# Function to play the melody
def play_melody(tune):
    """
    Plays a melody using the `winsound.Beep` function.

    The melody is defined as a sequence of tuples, where each tuple contains:
    - `note`: A string representing the note (e.g., 'C', 'D', 'E'). 
                Use a space `' '` for a rest.
    - `duration`: An integer representing the duration of the note in milliseconds.

    If the note is a space (' '), the function pauses for the specified duration 
    to simulate a rest. Otherwise, it plays the corresponding note frequency 
    using `winsound.Beep`.

    Parameters:
    -----------
    tune : list of tuples
        A list where each tuple contains:
        - `note` (str): The musical note to be played or `' '` for a rest.
        - `duration` (int): The duration of the note/rest in milliseconds.

    Example:
    --------
    notes = {'C': 261, 'D': 294, 'E': 329}
    melody = [('C', 500), ('D', 500), ('E', 500), (' ', 300), ('C', 700)]
    play_melody(melody)

    Notes:
    ------
    - This function relies on the `notes` dictionary being predefined, mapping 
        note names to their frequencies in Hz.
    - The `winsound.Beep` function only works on Windows.

    Raises:
    -------
    KeyError:
        If a note in the melody is not found in the `notes` dictionary.
    """
    for note, duration in tune:
        if note == ' ':
            time.sleep(duration / 1000)  # Rest
        else:
            winsound.Beep(notes[note], duration)

# Function triggered by the button
def on_cheers_click():
    """
    Function triggered when the "Cheers" button is clicked.

    This function performs the following actions:
    1. Displays a pop-up message box with the title "Cheers!" and the message "Merry Christmas! 🎄✨".
    2. Plays the festive melody by calling the `play_melody` function with the predefined melody.
    3. Uses the `pyttsx3` engine to speak the message "Ho ho ho! Merry Christmas!" aloud.

    The purpose of this function is to spread holiday cheer with a visual message, a festive tune, 
    and a voice greeting when the user interacts with the "Cheers" button.

    Parameters:
    -----------
    None

    Example:
    --------
    on_cheers_click()  # This will show the pop-up, play the melody, and speak the greeting.
    """
    messagebox.showinfo("Cheers!", "Merry Christmas! 🎄✨")
    play_melody(melody)
    engine.say("Ho ho ho! Merry Christmas!")
    engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("Christmas Cheer")
root.geometry("300x200")

# Add a button
cheers_button = tk.Button(root, text="Cheers", font=("Helvetica", 16), command=on_cheers_click)
cheers_button.pack(expand=True)

# Run the GUI event loop
root.mainloop()
