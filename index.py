import tkinter  as tk
import pyautogui
import getpixelcolor

class Main:
    def __init__ (self,root):
        self.root = root
        self.root.title("Mouse Point")
        self.root.geometry("222x280")


if __name__ == '__main__':
    root = tk.Tk()

    Title = tk.Label(text="Mouse Point:")
    Title.pack()

    XLabel = tk.Label(text="X:")
    XLabel.pack()

    YLabel = tk.Label(text="Y:")
    YLabel.pack()

    HexColorLabel = tk.Label(text="Color: ")
    HexColorLabel.pack()

    RGBColorLabel = tk.Label(text="R: G: B: ")
    RGBColorLabel.pack()

    colorFrame = tk.Frame(master=root, width=100, height=100, bg="red")
    colorFrame.pack()


    obj = Main(root)

    def some_func():
        p = pyautogui.position()
        XLabel["text"] = "X: " + str(p.x)
        YLabel["text"] = "Y: " + str(p.y)

        (r, g, b) = getpixelcolor.pixel(p.x, p.y)
        hexRepresentation = '#%02x%02x%02x' % (r, g, b)

        colorFrame["bg"] = hexRepresentation
        HexColorLabel["text"] = hexRepresentation
        RGBColorLabel["text"] = "R: %d, G: %d, B: %d" % (r, g, b)


        # call this function again in 1 second
        root.after(100, some_func)

    some_func()

    root.mainloop()