import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp

def extract_audio():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    
    if file_path:
        video = mp.VideoFileClip(file_path)
        audio = video.audio
        audio.write_audiofile("extracted_audio.mp3")
        audio.close()
        video.close()
        status_label.config(text="Audio extraction complete!")

# Create the main application window
app = tk.Tk()
app.title("MP4 Audio Extractor")

# Create and configure widgets
instruction_label = tk.Label(app, text="Select an MP4 file to extract audio:")
instruction_label.pack(pady=10)

extract_button = tk.Button(app, text="Extract Audio", command=extract_audio)
extract_button.pack()

status_label = tk.Label(app, text="")
status_label.pack(pady=10)

# Start the tkinter main loop
app.mainloop()
