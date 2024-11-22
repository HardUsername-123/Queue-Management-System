import threading
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image
from db import create_connection
from mysql.connector import Error
from tkinter import messagebox

import socket

# Initialize the queue display window with ttkbootstrap
q_display = ttk.Window(themename="flatly")  # 'superhero' theme for a modern dark design
q_display.title("Queue display")
q_display.iconbitmap("C:\\Users\\QHTF\\OneDrive\\Desktop\\new_queue_system\\QMS-python-gui-main\\old-logo.ico")

# Set the window to fullscreen
q_display.attributes("-fullscreen", True)

# Exit fullscreen with the Escape key
def exit_fullscreen(event):
    q_display.attributes("-fullscreen", False)

q_display.bind("<Escape>", exit_fullscreen)

# Center the window on the screen
window_width = 1100
window_height = 700
screen_width = q_display.winfo_screenwidth()
screen_height = q_display.winfo_screenheight()
x = (screen_width // 3) - (window_width // 3)
y = (screen_height // 3) - (window_height // 3)
q_display.geometry(f"{window_width}x{window_height}+{x}+{y}")

q_display.columnconfigure(0, weight=1)
q_display.columnconfigure(1, weight=1)

q_display.rowconfigure(0, weight=1)
q_display.rowconfigure(1, weight=1)
q_display.rowconfigure(2, weight=1)
q_display.rowconfigure(3, weight=1)

# Header labels with modern design
window_label = ttk.Label(q_display,
                         text='WINDOW',
                         bootstyle="info",
                         anchor='center',
                         font=('Helvetica', 48, 'bold'))
window_label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)


serving_label = ttk.Label(q_display,
                          text='SERVING',
                          bootstyle="info",
                          anchor='center',
                          font=('Helvetica', 48, 'bold'))
serving_label.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

# Sidebar labels with modern design--------------------------------------------------------------------------
cashier_label = ttk.Label(q_display,
                          text='CASHIER 1',
                          
                          anchor='center',
                          font=('Helvetica', 32, 'bold'))
cashier_label.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

cashier_c2 = ttk.Label(q_display,
                          text='CASHIER 2',
                          
                          anchor='center',
                          font=('Helvetica', 32, 'bold'))
cashier_c2.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

promissory_label = ttk.Label(q_display,
                             text='PROMISSORY \nNOTE\nCOORDINATOR',
                             
                             anchor='center',
                             font=('Helvetica', 32, 'bold'))
promissory_label.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

scholarship_label = ttk.Label(q_display,
                              text='SCHOLARSHIP\nCOORDINATOR',
                              
                              anchor='center',
                              font=('Helvetica', 32, 'bold'))
scholarship_label.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)



# Preparing queue number------------------------------------------------------------------------------------
try:
    conn = create_connection()
    cursor = conn.cursor()

    query = "SELECT queue_num FROM queue_display LIMIT 1 OFFSET 1"
    cursor.execute(query)
    get_snum = cursor.fetchone()

    # Set the default value to 0 if no result is found
    get_snum = get_snum[0] if get_snum else 0

    cursor.fetchall()

    query_pnc_prep = "SELECT promisorry_number FROM queue_display_promisorry LIMIT 1 OFFSET 1"
    cursor.execute(query_pnc_prep)
    get_num_pnc_prep = cursor.fetchone()

    # Set the default value to 0 if no result is found
    get_num_pnc_prep = get_num_pnc_prep[0] if get_num_pnc_prep else 0

    cursor.fetchall()

    query_sc_prep = "SELECT queue_sc FROM queue_display_sc LIMIT 1 OFFSET 1"
    cursor.execute(query_sc_prep)
    get_num_sc_prep = cursor.fetchone()

    get_num_sc_prep = get_num_sc_prep[0] if get_num_sc_prep else 0

    cursor.fetchall()

    query_sc2_prep = "SELECT c2_num FROM queue_c2_display LIMIT 1 OFFSET 1"
    cursor.execute(query_sc2_prep)
    get_num_sc2_prep = cursor.fetchone()

    get_num_sc2_prep = get_num_sc2_prep[0] if get_num_sc2_prep else 0
except Error as err:
    print(f"Error: {err}")


# # Set the default value to 0 if no result is found
# get_num_sc_prep = get_num_sc_prep[0] if get_num_sc_prep else 0

#cashier1----------------------------------------------------------------------------------------
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

            print(data)

            # Update the label text in the GUI thread
            update_label_text(data)
    except Exception as e:
        print(f"Error receiving data from server: {e}")
        messagebox.showerror("Connection Error", "Unable to receive data from the server.")

# Function to update the label text (executed in the GUI thread)
def update_label_text(data):
    p_c_number1.config(text=data)  # Update the label with received data
# Start the background thread
def start_receiving():
    thread = threading.Thread(target=receive_data_in_background, daemon=True)
    thread.start()


#cashier 2----------------------------------------------------------------------------------
SERVER_HOST_C2 = "127.0.0.1"
SERVER_PORT_C2 = 5001

# Function to receive data from the server in a loop
def receive_data_in_background_c2():
    try:
        # Create a socket connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST_C2, SERVER_PORT_C2))

        while True:
            # Receive data from the server
            response = client_socket.recv(1024)  # Adjust buffer size as needed
            data = response.decode('utf-8')

            print(data)

            # Update the label text in the GUI thread
            update_label_text_c2(data)
    except Exception as e:
        print(f"Error receiving data from server: {e}")
        messagebox.showerror("Connection Error", "Unable to receive data from the server.")

# Function to update the label text (executed in the GUI thread)
def update_label_text_c2(data):
    p_c_number2.config(text=data)  # Update the label with received data
# Start the background thread
def start_receiving_c2():
    thread = threading.Thread(target=receive_data_in_background_c2, daemon=True)
    thread.start()

#promisorry note coordinator---------------------------------------------------------------------------
SERVER_HOST_C3 = "127.0.0.1"
SERVER_PORT_C3 = 3030

# Function to receive data from the server in a loop
def receive_data_in_background_C3():
    try:
        # Create a socket connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST_C3, SERVER_PORT_C3))

        while True:
            # Receive data from the server
            response = client_socket.recv(1024)  # Adjust buffer size as needed
            data = response.decode('utf-8')

            print(data)

            # Update the label text in the GUI thread
            update_label_text_C3(data)
    except Exception as e:
        print(f"Error receiving data from server: {e}")
        messagebox.showerror("Connection Error", "Unable to receive data from the server.")

# Function to update the label text (executed in the GUI thread)
def update_label_text_C3(data):
    p_sc_number3.config(text=data)  # Update the label with received data
# Start the background thread
def start_receiving_C3():
    thread = threading.Thread(target=receive_data_in_background_C3, daemon=True)
    thread.start()

#scholar coordinator----------------------------------------------------------------------
SERVER_HOST_C4 = "127.0.0.1"
SERVER_PORT_C4 = 4001

# Function to receive data from the server in a loop
def receive_data_in_background_C4():
    try:
        # Create a socket connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST_C4, SERVER_PORT_C4))

        while True:
            # Receive data from the server
            response = client_socket.recv(1024)  # Adjust buffer size as needed
            data = response.decode('utf-8')

            print(data)

            # Update the label text in the GUI thread
            update_label_text_C4(data)
    except Exception as e:
        print(f"Error receiving data from server: {e}")
        messagebox.showerror("Connection Error", "Unable to receive data from the server.")

# Function to update the label text (executed in the GUI thread)
def update_label_text_C4(data):
   p_pnc_number4.config(text=data)  # Update the label with received data
# Start the background thread
def start_receiving_C4():
    thread = threading.Thread(target=receive_data_in_background_C4, daemon=True)
    thread.start()

p_c_number1 = ttk.Label(q_display,
                       text="0",
                       bootstyle="danger",
                       anchor='center',
                       font=('Helvetica', 80, 'bold'))
p_c_number1.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)

p_c_number2 = ttk.Label(q_display,
                       text="0",
                       bootstyle="danger",
                       anchor='center',
                       font=('Helvetica', 80, 'bold'))
p_c_number2.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)

p_sc_number3 = ttk.Label(q_display,
                        text="0",
                        bootstyle="danger",
                        anchor='center',
                        font=('Helvetica', 80, 'bold'))
p_sc_number3.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)

p_pnc_number4 = ttk.Label(q_display,
                         text="0",
                         bootstyle="danger",
                         anchor='center',
                         font=('Helvetica', 80, 'bold'))
p_pnc_number4.grid(row=4, column=1, sticky='nsew', padx=10, pady=10)

start_receiving()
start_receiving_c2()
start_receiving_C3()
start_receiving_C4()

# # Serving queue number--------------------------------------------------------------------------------
# try:
#     query = "SELECT queue_num FROM queue_display"
#     cursor.execute(query)
#     get_num = cursor.fetchone()

#     # Set the default value to 0 if no result is found
#     get_num = get_num[0] if get_num else 0

#     cursor.fetchall()  # This ensures all rows are processed (even if no more rows are there)

#     # Second query: Fetch promisorry number for the second label
#     query_pnc_serve = "SELECT promisorry_number FROM queue_display_promisorry"
#     cursor.execute(query_pnc_serve)
#     get_num_pnc_serve = cursor.fetchone()

#     # Set the default value to 0 if no result is found
#     get_num_pnc_serve = get_num_pnc_serve[0] if get_num_pnc_serve else 0

#     cursor.fetchall() 

#     query_sc_serve = "SELECT queue_sc FROM queue_display_sc"
#     cursor.execute(query_sc_serve)
#     get_num_sc_serve = cursor.fetchone()

#     # Set the default value to 0 if no result is found
#     get_num_sc_serve = get_num_sc_serve[0] if get_num_sc_serve else 0

#     cursor.fetchall()

#     query_sc2_serve = "SELECT c2_num FROM queue_c2_display"
#     cursor.execute(query_sc2_serve)
#     get_num_c2_serve = cursor.fetchone()


#     get_num_c2_serve = get_num_c2_serve[0] if get_num_c2_serve else 0

# except Error as err:
#     print(f"Error: {err}")

    

# # Now proceed with the labels
# s_c_number1 = ttk.Label(q_display,
#                        text="0",
#                        bootstyle="warning",
#                        anchor='center',
#                        font=('Helvetica', 80, 'bold'))
# s_c_number1.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)

# s_c_number = ttk.Label(q_display,
#                        text=str(get_num_c2_serve),
#                        bootstyle="warning",
#                        anchor='center',
#                        font=('Helvetica', 80, 'bold'))
# s_c_number.grid(row=2, column=2, sticky='nsew', padx=10, pady=10)

# s_sc_number = ttk.Label(q_display,
#                         text=str(get_num_sc_serve),
#                         bootstyle="warning",
#                         anchor='center',
#                         font=('Helvetica', 80, 'bold'))
# s_sc_number.grid(row=3, column=2, sticky='nsew', padx=10, pady=10)

# s_pnc_number = ttk.Label(q_display,
#                          text=str(get_num_pnc_serve),
#                          bootstyle="warning",
#                          anchor='center',
#                          font=('Helvetica', 80, 'bold'))
# s_pnc_number.grid(row=4, column=2, sticky='nsew', padx=10, pady=10)


q_display.mainloop()
