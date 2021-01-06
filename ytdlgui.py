from __future__ import unicode_literals
import tkinter as tk
import tkinter.filedialog as filedialog
import youtube_dl
import os
# from tkcalendar import Calendar, DateEntry

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.dwnldButton = tk.Button(self)
        self.dwnldButton['text'] = "Download"
        self.dwnldButton['command'] = self.start_download
        self.dwnldButton.grid(row=2, column=1, sticky="NESW")

        self.dwnldLocButton = tk.Button(self)
        self.dwnldLocButton['text'] = "Location"
        self.dwnldLocButton['command'] = self.select_download_loc
        self.dwnldLocButton.grid(row=0)

        self.downloadLoc = tk.Entry(self)
        self.downloadLoc.grid(row=0, column=1, ipadx=80, padx=5)

        self.urlLabel = tk.Label(self, text="URL")
        self.urlLabel.grid(row=1)

        self.urlLoc = tk.Entry(self)
        self.urlLoc.grid(row=1, column=1, ipadx=80)

    def select_download_loc(self):
        download_loc = filedialog.askdirectory()
        self.downloadLoc.insert(tk.INSERT, download_loc)

    def start_download(self):
        print(self.downloadLoc.get())
        print(self.urlLoc.get())
        desiredLoc = str(self.downloadLoc.get())
        if(desiredLoc != ""):
            outputStr = desiredLoc + "\\" + "%(title)s-%(id)s.%(ext)s"
        else:
            outputStr = "%(title)s-%(id)s.%(ext)s"

        ydl_opts = {'outtmpl': outputStr,}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.urlLoc.get()])

root = tk.Tk()
app = Application(master=root)
app.master.title("Basic Youtube-dl GUI")

if os.path.exists("chck.ico"):
    app.master.iconbitmap("chck.ico")


app.mainloop()