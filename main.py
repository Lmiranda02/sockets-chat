# main.py

from tkinter import Tk, messagebox
from cliente import GUI
from servidor import ChatServer
import threading

def start_client():
    root = Tk()
    gui = GUI(root)
    root.protocol("WM_DELETE_WINDOW", gui.on_close_window)
    root.mainloop()

def start_server():
    server = ChatServer()

if __name__ == '__main__':
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    threading.Event().wait(1)

    start_client()
