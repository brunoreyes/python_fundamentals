import sqlite3
try:
    import tkinter
except ImportError: # for python 2
    import Tkinter

conn = sqlite3.connect('music.sqlite')

mainWindow = tkinter.Tk('Music DB Browser')
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ====== labels ======
tkinter.Label(mainWindow, text="Artist").grod(row=0, column=0)
tkinter.Label(mainWindow, text ="Albums").grod(row=0, column=1)
tkinter.Label(mainWindow, text ="Songs").grod(row=0, column=2)

# ====== artists listbox ======
artistList = tkinter.Listbox(mainWindow)
artistList.grid()
artistList.config()

# ====== albums listbox ======
albumLV = tkinter.Variable(mainWindow)
albumLV.set(())
albumList = tkinter.Listbox(mainWindow)
albumList.grid()
albumList.config()

# ====== albums listbox ======
songLV = tkinter.Variable(mainWindow)
songLV.set(())
songList = tkinter.Listbox(mainWindow)
songList.grid()
songList.config()

# ====== Main Loop ======
mainWindow.mainloop()
print("closing database connection")