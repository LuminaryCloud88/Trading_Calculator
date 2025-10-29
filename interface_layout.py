#Graphical User Interface to input data
# TO-DO make it so you can only enter certain values and handle errors that come with it
# Add secondary window that displays output instead of displaying in the terminal and save button
from tkinter import ttk, messagebox
import tkinter
from calculations import *

def submit_data():
    try:
        capital = float(capital_entry.get())
        fees = float(fees_entry.get())
        entry = float(entry_entry.get())  
        exit = float(exit_entry.get())
        direction = direction_combobox.get().lower()
        leverage = float(leverage_entry.get())
        risk_input_str = risk_label_entry.get()

        if risk_input_str == "":
            risk = float(capital * leverage)
        else:
            risk = float(risk_input_str)
            if risk <= 0:
                raise ValueError("Risk must be greater than zero.")
        
        if direction not in ["long", "short"]:
            raise ValueError("Direction must be 'long' or 'short'.")
            

        pnl, position_size, r_multiple = calculate_pnl(
            capital, fees, entry, exit, direction, leverage, risk
        )

        results_Window = tkinter.Toplevel(window)
        results_Window.title("Trade Summary")

        ttk.Label(results_Window, text="--- Your Trade Summary ---", font=("Arial", 14, "bold")).pack(pady=10)
        ttk.Label(results_Window, text=f"Position Size: ${position_size:,.2f}").pack(pady=5)
        ttk.Label(results_Window, text=f"PnL: ${pnl:,.2f}").pack(pady=5)
        ttk.Label(results_Window, text=f"R-Multiple: {r_multiple:.2f}").pack(pady=5)

        ttk.Button(results_Window, text="Close", command=results_Window.destroy).pack(pady=15)
        print("Returning:", pnl, position_size, r_multiple)
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")

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

submit_button = tkinter.Button(frame, text="Submit", command= submit_data)
submit_button.grid(row=1,column=0, sticky="news", padx=20,pady=20)


window.mainloop()