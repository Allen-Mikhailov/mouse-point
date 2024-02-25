import tkinter  as tk
import pyautogui
from pynput import keyboard
import getpixelcolor

class Main:
    def __init__ (self,root):
        self.root = root
        self.root.title("Mouse Point")
        self.root.geometry("222x280")

frozen = False

def on_press(key):
    try:
        global frozen
        if (key.char == "s"):
            frozen = not frozen
            if (frozen):
                print("Frozen")
            else:
                print("Unfrozen")
            # print("Frozen: " + str(frozen))

    except AttributeError:
        pass

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
        if (not frozen):
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

    listener = keyboard.Listener(
        on_press=on_press,
        )
    listener.start()

    root.mainloop()

