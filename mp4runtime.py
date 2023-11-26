import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

class VideoPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Player")
        self.master.geometry("400x200")

        self.label = tk.Label(self.master, text="Select a video file:")
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.master, textvariable=self.entry_var, state='disabled', width=30)
        self.entry.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.browse_button = tk.Button(self.master, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=1, column=2, padx=5, pady=5)

        self.play_button = tk.Button(self.master, text="Get Running Time", command=self.get_running_time)
        self.play_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.running_time_label = tk.Label(self.master, text="")
        self.running_time_label.grid(row=3, column=0, columnspan=3, pady=10)

    def browse_file(self):
        self.reset_gui()
        file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        self.entry_var.set(file_path)
        self.label.config(text="Selected video file:")

    def get_running_time(self):
        try:
            video_clip = VideoFileClip(self.entry_var.get())
            running_time = video_clip.duration
            self.running_time_label.config(text=f"Running Time: {running_time:.2f} seconds")
        except Exception as e:
            self.running_time_label.config(text=f"Error: {str(e)}")

    def reset_gui(self):
        self.entry_var.set("")
        self.label.config(text="Select a video file:")
        self.running_time_label.config(text="")


def main():
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
