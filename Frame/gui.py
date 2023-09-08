from tkinter import messagebox
import customtkinter
import threading

class Threads:
    def hideWindow(window_name : str):
        window_name.withdraw()

class Window:
    def __init__(self, name : str | None="Window", geometry : int | None="250x250") -> None:
        self.name = name
        self.size = geometry

    def createWindow(self, bg_color = None, **kwargs):
        kwargs.setdefault("fg_color","white")
        root = customtkinter.CTk()
        if bg_color != None:
            root.config(bg=bg_color)
        root.title(self.name)
        if self.size != "" and type(self.size) is tuple:
            self.size = str(self.size).replace("(","").replace(")","").replace("'","").replace(" ","").replace(",","x")
            root.geometry(self.size)
        elif self.size != "" and type(self.size) is list:
            root.update_idletasks()
            width = root.winfo_width()
            frm_width = root.winfo_rootx() - root.winfo_x()
            win_width = width + 2 * frm_width
            height = root.winfo_height()
            titlebar_height = root.winfo_rooty() - root.winfo_y()
            win_height = height + titlebar_height + frm_width
            x = root.winfo_screenwidth() // 2 - win_width // 2
            y = root.winfo_screenheight() // 2 - win_height // 2
            root.geometry('{}x{}+{}+{}'.format(width, height, self.size[0], self.size[1]))
            root.deiconify()
        global hide
        hide = threading.Thread(target=Threads.hideWindow,args=(root,))
        root.mainloop()
    
    def hide_window(self):
        hide.start()
        
ScreenWindow = Window(geometry=["250","300"])
root = ScreenWindow.createWindow()