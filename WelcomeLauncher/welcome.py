import os
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk, ImageSequence

root = Tk()
b_width = 30
cval = 0
root.title('Welcome')
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
icon = tk.PhotoImage(file="./Assets/icon.png")
root.iconphoto(False, icon)

class AnimatedLoader(tk.Label):
    def __init__(self, master, gif_path, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.gif = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(self.gif)]
        self.frame_index = 0
        self.animate = True
        self.update_gif()

    def update_gif(self):
        if self.animate:
            self.configure(image=self.frames[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.after(100, self.update_gif)

    def stop(self):
        self.animate = False

def open_folder():
    folder_path = "Games"
    if folder_path:
        os.system(f'open "{folder_path}"')

def credits_page():
    global cval
    if cval == 0:
        cval = 1
        credits.pack()
    else:
        cval = 0
        credits.pack_forget()

def comp_pack():
    l1.pack()
    info.pack()
    open_button.pack(pady=5)
    credits_button.pack(pady=5)
    exit_button.pack(pady=5)   

def comp_forg():
    l1.pack_forget()
    info.pack_forget()
    open_button.pack_forget()
    credits_button.pack_forget()
    exit_button.pack_forget()

def cont_swap():
    loader.stop()
    loader.pack_forget()
    comp_pack()

def runtime():
    loader.pack()
    root.after(2000, cont_swap)
    
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Quit', command=root.quit)

loader = AnimatedLoader(root, "./Assets/loader.gif")
l1 = Label(root, text='Welcome to PiStation!', font=("Arial", 40, "bold"), pady=5, padx=20)
info = Label(root, text='\nUser password: game123', font=("Arial", 16), pady=20)
credits = Label(root, text='Credits:\nCanonical - Ubuntu Desktop arm64\nEvan Alger - Lead Game Developer and Best Friend\nSam Bullock - Systems Engineer',font=("Arial", 12), pady="15",padx="20")
open_button = tk.Button(root, text="Play Games!", height=int(b_width/15), width=b_width,command=open_folder)
exit_button = tk.Button(root, text='Exit', height=int(b_width/15), width=b_width,command=root.destroy)
credits_button = tk.Button(root, text="Toggle Credits", height=int(b_width/15), width=b_width, command=credits_page)

#Light 'er Up Boi
runtime()
root.mainloop()