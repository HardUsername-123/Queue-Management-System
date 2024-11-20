import tkinter as tk
import customtkinter as ctk
from PIL import Image

from center_window import center_window

# Initialize the main window
root = ctk.CTk()  # Use customtkinter's window for CTk elements
root.title("Queue Management System")
root.iconbitmap("C:\\Users\\QHTF\\OneDrive\\Desktop\\new_queue_system\\QMS-python-gui-main\\old-logo.ico")
center_window(800, 500, root)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# Create the main frame that will contain the boxes and the title
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill=tk.BOTH)

# Create a title frame and place it at the top of main_frame
title_frame = tk.Frame(main_frame)
title_frame.pack(pady=(20, 50))  # Add padding to position it higher

# Load and display the logo image in the title_frame
logo_icon = ctk.CTkImage(light_image=Image.open("C:\\Users\\QHTF\\OneDrive\\Desktop\\new_queue_system\\QMS-python-gui-main\\old-logo.png"),
                         dark_image=Image.open("C:\\Users\\QHTF\\OneDrive\\Desktop\\new_queue_system\\QMS-python-gui-main\\old-logo.png"),
                         size=(100, 100))  # Resize to 60x60 pixels


# Create a sub-frame for centering the boxes within it
center_frame = tk.Frame(main_frame)
center_frame.pack(expand=True, pady=(0, 50))

logo_ncmc = ctk.CTkLabel(center_frame, image=logo_icon, text="")
logo_ncmc.pack(pady=(0, 5))  # Add some padding below the image

# Create the welcome label in the title_frame and center it
welcome_label = tk.Label(center_frame, text="Welcome to NCMC Queue Management System", font=("Helvetica", 20, "bold"))
welcome_label.pack(pady=(0,60))

# Create a frame for each box and label
box1_frame = tk.Frame(center_frame)
box1_frame.pack(side=tk.LEFT, padx=(50, 0), pady=10)

box2_frame = tk.Frame(center_frame)
box2_frame.pack(side=tk.LEFT, padx=(50, 0), pady=10)

box3_frame = tk.Frame(center_frame)
box3_frame.pack(side=tk.LEFT, padx=(50, 0), pady=10)

admin_icon = ctk.CTkImage(light_image=Image.open("C:\\Users\\QHTF\\OneDrive\\Desktop\\new_queue_system\\QMS-python-gui-main\\admin.png"),
                     dark_image=Image.open("C:\\Users\\QHTF\\OneDrive\\Desktop\\new_queue_system\\QMS-python-gui-main\\admin.png"),
                     size=(100, 100))  # Resize to 24x24 pixels

user_icon = ctk.CTkImage(light_image=Image.open("C:\\Users\\QHTF\\OneDrive\\Desktop\\new_queue_system\\QMS-python-gui-main\\user.png"),
                     dark_image=Image.open("C:\\Users\\QHTF\\OneDrive\\Desktop\\new_queue_system\\QMS-python-gui-main\\user.png"),
                     size=(100, 100))  # Resize to 24x24 pixels


display_icon = ctk.CTkImage(light_image=Image.open("C:\\Users\\QHTF\\OneDrive\\Desktop\\new_queue_system\\QMS-python-gui-main\\display.png"),
                     dark_image=Image.open("C:\\Users\\QHTF\\OneDrive\\Desktop\\new_queue_system\\QMS-python-gui-main\\display.png"),
                     size=(100, 100))  # Resize to 24x24 pixels

# Create three boxes (labels) and pack them inside their respective frames
box1 = ctk.CTkLabel(box1_frame, image=admin_icon, text="")
box1.pack()

box2 = ctk.CTkLabel(box2_frame, image=user_icon, text="")
box2.pack()

box3 = ctk.CTkLabel(box3_frame, image=display_icon, text="")
box3.pack()

def admin():
    root.destroy()
    import admin_operator_main

def user():
    root.destroy()
    import user_queue_entry_main

def display():
    root.destroy()
    import queue_display_main

# Add descriptive labels under each box
btn1 = ctk.CTkButton(box1_frame, text="Admin & Operators\nInterface", font=("Helvetica", 12),
                         fg_color="#d68b26",
                         hover_color="#a45e14",
                         command=admin)
btn1.pack(pady=10)

btn2 = ctk.CTkButton(box2_frame, text="User Interface", font=("Helvetica", 12),
                           fg_color="#d68b26",
                           hover_color="#a45e14",
                           command=user)
btn2.pack(pady=10)

btn3 = ctk.CTkButton(box3_frame, text="Queue display", font=("Helvetica", 12),
                           fg_color="#d68b26",
                           hover_color="#a45e14",
                           command=display)
btn3.pack(pady=10)

# Run the main loop
root.mainloop()
