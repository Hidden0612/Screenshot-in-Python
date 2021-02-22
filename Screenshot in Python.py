import pyautogui
import tkinter as tk
from tkinter.filedialog import *
#=============================#
root=tk.Tk()
canvas1 = tk.Canvas(root,width=300 , height = 300) ; canvas1.pack()

def shot():
    myscreen = pyautogui.screenshot()
    save_path = askopenfilename()
    myscreen.save(save_path + "ـscreen.png")

mybut = tk.Button(text="Take ScreenShot" , command = shot , font=10)
canvas1.create_window(150,150,window=mybut)

root.mainloop()