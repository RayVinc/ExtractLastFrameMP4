import tkinter as tk
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        videoplayer.load(file_path)
        videoplayer.play()

root = tk.Tk()
root.title("Video Player")

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.pack(expand=True, fill="both")

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

root.mainloop()
