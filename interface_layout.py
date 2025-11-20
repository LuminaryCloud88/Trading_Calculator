# Graphical User Interface to input data
# TO-DO make it so you can only enter certain values and handle errors that come with it
# Add secondary window that displays output instead of displaying in the terminal and save button
# Possibly add a trade set-up section, so you know what you entered on: break-out , contiuation etc. 
# Keep track of metrics for those?
# Add 'trade' dictionary to hold all the values of a single trade
from tkinter import ttk, messagebox
import tkinter
from calculations import *
from constants import Trade, help_text


def submit_data(capital_entry, fees_entry, leverage_entry, entry_entry, exit_entry, direction_combobox, risk_label_entry):
    try:
        capital = float(capital_entry.get())
        fees = float(fees_entry.get())
        entry = float(entry_entry.get())  
        exit = float(exit_entry.get())
        direction = direction_combobox.get().lower()
        leverage = float(leverage_entry.get() or 1)
        risk_input_str = risk_label_entry.get()

        if risk_input_str == "":
            risk = float(capital * leverage)
        else:
            risk = float(risk_input_str)
            if risk <= 0:
                raise ValueError("Risk must be greater than zero.")
        
        if direction not in ["long", "short"]:
            raise ValueError("Direction must be 'long' or 'short'.")
            
        trade = Trade(
            capital=capital,
            fees=fees,
            entry=entry,
            exit=exit,
            direction=direction,
            leverage=leverage,
            risk=risk
        )

        trade = basic_metrics(trade)

        results_window = tkinter.Toplevel()
        results_window.title("Trade Summary")

        ttk.Label(results_window, text="--- Your Trade Summary ---", font=("Arial", 14, "bold")).pack(pady=10)
        ttk.Label(results_window, text=f"Position Size: ${trade.position_size:,.2f}").pack(pady=5)
        ttk.Label(results_window, text=f"PnL: ${trade.pnl:,.2f}").pack(pady=5)
        ttk.Label(results_window, text=f"R-Multiple: {trade.r_multiple:.2f}").pack(pady=5)

        ttk.Button(results_window, text="Close", command=results_window.destroy).pack(pady=15)

    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")

def free_metrics_window():
    window = tkinter.Tk()
    window.title("Trading Entry") #Use App Name Later?

    frame = tkinter.Frame(window)
    frame.pack()

    #Saving User Information
    user_info_frame = tkinter.LabelFrame(frame, text="Your Trade Summary")
    user_info_frame.grid(row=0, column=0, padx=20, pady=20)

    capital_label = tkinter.Label(user_info_frame, text="Enter Capital:")
    capital_label.grid(row=0, column=0)
    capital_entry = tkinter.Entry(user_info_frame)
    capital_entry.grid(row=0, column=1)

    fees_label = tkinter.Label(user_info_frame, text="Enter fees (as %):")
    fees_label.grid(row=1, column=0)
    fees_entry = tkinter.Entry(user_info_frame)
    fees_entry.grid(row=1, column=1)

    leverage_label = tkinter.Label(user_info_frame, text="Enter leverage. If none, use 1:")
    leverage_label.grid(row=2,column=0)
    leverage_entry = tkinter.Entry(user_info_frame)
    leverage_entry.grid(row=2, column=1)

    entry_label = tkinter.Label(user_info_frame, text="Enter your entry price:")
    entry_label.grid(row=3,column=0)
    entry_entry = tkinter.Entry(user_info_frame)
    entry_entry.grid(row=3, column=1)

    exit_label = tkinter.Label(user_info_frame, text="Enter your exit price:")
    exit_label.grid(row=4,column=0)
    exit_entry = tkinter.Entry(user_info_frame)
    exit_entry.grid(row=4, column=1)

    direction_label = tkinter.Label(user_info_frame, text="Direction:")
    direction_label.grid(row=5,column=0)
    direction_combobox = ttk.Combobox(user_info_frame, values=["short","long"])
    direction_combobox.grid(row=5, column=1)

    risk_label = tkinter.Label(user_info_frame, text="Risk or Stop:")
    risk_label.grid(row=6,column=0)
    risk_label_entry = tkinter.Entry(user_info_frame)
    risk_label_entry.grid(row=6, column=1)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    submit_button = tkinter.Button(frame, text="Submit",command=lambda: submit_data(
        capital_entry, fees_entry, leverage_entry, entry_entry, exit_entry, direction_combobox, risk_label_entry))
    submit_button.grid(row=1,column=0, sticky="e", padx=20,pady=20)

    help_button = tkinter.Button(frame, text="Help", command=lambda: help_window(help_text))
    help_button.grid(row=1, column=0, sticky="w", padx=20,pady=20)

    window.mainloop()

'''def login_window():
    window = tkinter.Tk()
    window.title("Login") 

    frame = tkinter.Frame(window)
    frame.pack()

    username = username_entry.get()
    password = password_entry.get()

    user = get_user(username, password)
    if user:
        root.destroy()  # close login window
        if user['subscribed']:
            open_subscriber_window(user)
        else:
            free_metrics_window(user)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

    root = tk.Tk()
    root.title("Login")

    tk.Label(root, text="Username:").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Login", command=login).pack()

def show_trades_window():
    window = tkinter.Tk()
    window.title("Trade Log") 

    frame = tkinter.Frame(window)
    frame.pack()

    cursor.excute("SELECT * FROM trades WHERE user=?", (current_user,))
    rows = cursor.fetchall()

    history_window = tk.Toplevel()
    history_window.title("Trade History")

    tree = ttk.Treeview(history_window, columns=(trade), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)

    for row in rows:
        tree.insert("", "end", values=row[2:])
'''   

# def csv_input_window():
def help_window(help_text):
    window = tkinter.Tk()
    window.title("Help") 

    frame = tkinter.Frame(window)
    frame.pack()

    help_text_frame = tkinter.LabelFrame(frame, text="Help")
    help_text_frame.grid(row=0, column=0, padx=20, pady=20)

    help_label = tkinter.Label(help_text_frame, text=help_text, justify="center", wraplength=350)
    help_label.grid(padx=20, pady=20)