import customtkinter as ctk
import tkinter as tk
from PIL import Image

root = ctk.CTk()
root.title("example")
root.geometry("400x400")

def open():
    root.destroy()
    import admin_dashboard

btn = ctk.CTkButton(master=root, text="Click", command=open)
btn.pack()

root.mainloop()