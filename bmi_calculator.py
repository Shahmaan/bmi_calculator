import customtkinter as ctk
from settings import *
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class App(ctk.CTk):
    def __init__(self):
        # window setup
        super().__init__(fg_color=GREEN)
        self.title('')
        self.geometry('400x400')
        self.resizable(False, False)
        self.change_title_bar_color()
        
        self.mainloop()
        
    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR  
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except Exception as e:
            print("Error changing title bar color:", e)
            # Handle the error appropriately (e.g., logging)
            pass
        
        
        
if __name__ == '__main__':
    App()


#https://www.youtube.com/watch?v=mop6g-c5HEY&t=25905s