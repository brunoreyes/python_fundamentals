import math

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parabola(page, size): # a parabola is x^2, eventually coming up with enough x's to make a curved line like: U
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


    # Previous Steps
    # y = x * x / 100 # Making the y value not go off the stream
    # return y

def circle(page, radius, g, h): # plotting out a circle
    for x in range(g, g + radius):
        y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2))) 
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page): # draw_axes creates the x & y axis lines, page is actually the canvas. 
    page.update() # need to call to have access to the x and y origin values
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    # print(locals()) # Just showing us the plot points for each axes

def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parobola")
mainWindow.geometry("640x480")
canvas = tkinter.Canvas(mainWindow, width=640, height=480) # changed width from 320 to 640 bc only 1 axis now
canvas.grid(row=0, column=0)

# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
# canvas2.grid(row=0, column=1) # On the second column

# print(repr(canvas), repr(canvas2)) # repr shows the representation of an object
draw_axes(canvas)  # calling the function
# draw_axes(canvas2)

# Previous Steps
# for x in range(-100, 100):
#     y = parabola(x)
#     plot(canvas, x,-y)
parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainWindow.mainloop()