import yt_dlp
import tkinter as tk
from tkinter import messagebox

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL")
        return

    options = {'outtmpl': '%(title)s.%(ext)s', 'format': 'best'}

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {e}")

app = tk.Tk()
app.title("Video Downloader")
tk.Label(app, text="Enter Video URL:").pack()
url_entry = tk.Entry(app, width=50)
url_entry.pack()
tk.Button(app, text="Download", command=download_video).pack()
app.mainloop()