import socket
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Server details
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345

# Function to receive data from the server in a loop
def receive_data_in_background():
    try:
        # Create a socket connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        while True:
            # Receive data from the server
            response = client_socket.recv(1024)  # Adjust buffer size as needed
            data = response.decode('utf-8')

            # Split the data into two pieces (assuming data is separated by a comma or other delimiter)
            data_parts = data.split(",")  # Assuming the data is separated by a comma
            
            if len(data_parts) >= 2:
                s_c_data = data_parts[0].strip()  # First piece of data for s_c_number1
                p_c_data = data_parts[1].strip()  # Second piece of data for p_c_number1

                # Update the labels with the respective data (safely in the GUI thread)
                update_label_text(s_c_data, p_c_data)
            else:
                print("Received data format is incorrect")
    except Exception as e:
        print(f"Error receiving data from server: {e}")
        messagebox.showerror("Connection Error", "Unable to receive data from the server.")

# Function to update the label texts (executed in the GUI thread)
def update_label_text(s_c_data, p_c_data):
    # Use Tkinter's after() to schedule the GUI update safely
    q_display.after(0, lambda: s_c_number1.config(text=s_c_data))  # Update s_c_number1 label
    q_display.after(0, lambda: p_c_number1.config(text=p_c_data))  # Update p_c_number1 label

# Start the background thread
def start_receiving():
    thread = threading.Thread(target=receive_data_in_background, daemon=True)
    thread.start()

# Initialize the main window
root = tk.Tk()
q_display = ttk.Frame(root)
q_display.grid(row=0, column=0)

# Labels for displaying data
p_c_number1 = ttk.Label(q_display,
                         text="0",
                         bootstyle="danger",
                         anchor='center',
                         font=('Helvetica', 80, 'bold'))
p_c_number1.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)

s_c_number1 = ttk.Label(q_display,
                         text="0",
                         bootstyle="warning",
                         anchor='center',
                         font=('Helvetica', 80, 'bold'))
s_c_number1.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)

# Start receiving data in the background
start_receiving()

# Run the Tkinter event loop
root.mainloop()
