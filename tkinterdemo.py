#GUI is a Graphical User Interface allows users to interact with electronic devices through graphical icons
# For example, the home screen of my mobile device is a GUI as well is my desktop sceen

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()
mainWindow = tkinter.Tk() # this is kind of like a modal, in the sense that it is a pop up window

mainWindow.title("Window Title") # a header in the middle of the menu bar
mainWindow.geometry('640x480+8+200') # we are passing a string with the geometry method which is unusual

label = tkinter.Label(mainWindow, text="Hello Worlds") # places a header in the top middle of the window
label.grid(row=0, column=0) #enabling grid

leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
leftFrame.grid(row=1, column=1) #enabling grid

# Here we made sure that the canvas would be on the leftside using leftFrame
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)  # here we are creating a small box

canvas.pack(side='left',anchor='n')
# canvas.pack(side='left', fill=tkinter.Y, expand=True)  # and moving it to the left, filling the y-axis 
# canvas.pack(side='top', fill=tkinter.BOTH,expand=True)  # filling both vertically and horizontally

rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', expand=True)
rightFrame.grid(row=1, column=2) #enabling grid

# Here we made sure that the buttons would be on the rightside using rightFrame
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
# button1.pack(side="left", anchor='n') #anchor move the button to either be on TRBL or center
# button2.pack(side="left", anchor='s')
# button3.pack(side="left", anchor='e')
# button1.pack(side="top") #anchor move the button to either be on TRBL or center
# button2.pack(side="top")
# button3.pack(side="top")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.config(relief='sunken', borderwidth=1)
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

mainWindow.mainloop()  # with expand=True, we can fill the X axis as well, b/c of side="left"
# positioning a canvas within a window depends on the side, as well as the fill and expand

