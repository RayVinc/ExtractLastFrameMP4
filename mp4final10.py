import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip

class VideoExtractorApp:
    def __init__(self, master):
        self.master = master
        master.title("Video Extractor")

        self.file_path = tk.StringVar()

        self.label = tk.Label(master, text="Select MP4 Video:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.extract_button = tk.Button(master, text="Extract Last 10 Seconds", command=self.extract_video)
        self.extract_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        self.file_path.set(file_path)

    def extract_video(self):
        input_file = self.file_path.get()

        if not input_file:
            tk.messagebox.showerror("Error", "Please select a valid MP4 file.")
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])

        if output_file:
            with VideoFileClip(input_file) as video:
                duration = video.duration
                start_time = max(0, duration - 10)
                video_clip = video.subclip(start_time, duration)
                video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

            tk.messagebox.showinfo("Success", f"Extraction completed successfully. Output saved as {output_file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoExtractorApp(root)
    root.mainloop()
