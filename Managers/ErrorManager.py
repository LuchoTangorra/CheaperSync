import tkinter as tk
from tkinter import ttk


def _copy_to_clipboard(master, msg):
    """
    Auxiliar tkinter function to copy msg to clipboard.
    """
    master.clipboard_clear()
    master.clipboard_append(msg)


def popup_error(msg):
    """
    Show popup error message and let the user copy to clipboard
    whatever error happens.
    """
    #Set messages
    title = f"Unexpected error in CheaperSync :(\n"
    send_to_msg = "    Please press copy and send the copied    \n    message to Luciano Tangorra    "
    message = f"{title}\n{send_to_msg}"

    popup = tk.Tk()
    popup.wm_title("Error in CheaperSync!")
    
    #Define main text
    ttk.Label(popup,
              text=message,
              font=("Arial", 20),
              justify=tk.CENTER) \
        .grid(column=1, row=0, padx=10, pady=10)

    #Define copy to clipboard button
    ttk.Style().configure('my.TButton', font=('Arial', 22))
    ttk.Button(popup,
               text="COPY ERROR",
               style="my.TButton",
               command=_copy_to_clipboard(popup, msg)) \
        .grid(column=1, row=1, padx=10, pady=10)

    popup.mainloop()


def showError(exception):
    """
    Displays a popup with that lets you obtain the exception
    """
    popup_error(str(exception))