import tkinter  as tk
import pyautogui

class Main:
    def __init__ (self,root):
        self.root = root
        self.root.title("Mouse Point")
        self.root.geometry("222x222")


if __name__ == '__main__':
    root = tk.Tk()

    Title = tk.Label(text="Mouse Point:")
    Title.pack()

    XLabel = tk.Label(text="X:")
    XLabel.pack()

    YLabel = tk.Label(text="Y:")
    YLabel.pack()


    obj = Main(root)

    def some_func():
        p = pyautogui.position()
        XLabel["text"] = "X: " + str(p.x)
        YLabel["text"] = "Y: " + str(p.y)

        # call this function again in 1 second
        root.after(100, some_func)

    some_func()

    root.mainloop()