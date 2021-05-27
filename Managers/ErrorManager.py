import tkinter as tk
from tkinter import ttk


def _copy_to_clipboard(master, msg):
    """
    Auxiliar tkinter function to copy msg to clipboard.

    Params:
        - master (tk): parent tkinker display.
        - msg (string): msg to be copied to clipboard.
    """
    master.clipboard_clear()
    master.clipboard_append(msg)


def _popup_error(msg, let_copy):
    """
    Show popup error message and let the user copy to clipboard
    whatever error happens.

    Params:
        - msg (string): msg to be set to copy button or show in popup.
        - let_copy: if true set copy button, otherwise shows error. 
    """
    #Set messages
    title = f"Unexpected error in CheaperSync :(\n"
    if let_copy:
        send_to_msg = "    Please press copy and send the copied    \n    message to Luciano Tangorra    "
        message = f"{title}\n{send_to_msg}"
    else:
        send_to_msg = "    Please check the json for invalid value    "
        message = f"{title}\n{send_to_msg}\n{msg}"

    popup = tk.Tk()
    popup.wm_title("Error in CheaperSync!")
    
    #Define main text
    ttk.Label(popup,
              text=message,
              font=("Arial", 20),
              justify=tk.CENTER) \
        .grid(column=1, row=0, padx=10, pady=10)

    if let_copy:
        #Define copy to clipboard button
        ttk.Style().configure('my.TButton', font=('Arial', 22))
        ttk.Button(popup,
                text="COPY ERROR",
                style="my.TButton",
                command=_copy_to_clipboard(popup, msg)) \
            .grid(column=1, row=1, padx=10, pady=10)

    popup.mainloop()


def showError(exception, let_copy=True):
    """
    Displays a popup with that lets you obtain the exception.

    Params:
        - exception (string): exception to be displayed.
    """
    popup_error(exception, let_copy)