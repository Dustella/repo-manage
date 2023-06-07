from tkinter import ttk
import tkinter as tk

def init_data_table():
    data_window = tk.Tk()
    data_window.title("数据表格")

    table = ttk.Treeview(data_window)
    table["columns"] = ("1", "2", "3")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("1", width=100, anchor=tk.CENTER)
    table.column("2", width=100, anchor=tk.CENTER)
    table.column("3", width=100, anchor=tk.CENTER)

    table.heading("#0", text="", anchor=tk.CENTER)
    table.heading("1", text="列1", anchor=tk.CENTER)
    table.heading("2", text="列2", anchor=tk.CENTER)
    table.heading("3", text="列3", anchor=tk.CENTER)

    table.insert("", tk.END, text="行1", values=("1A", "1B", "1C"))
    table.insert("", tk.END, text="行2", values=("2A", "2B", "2C"))
    table.insert("", tk.END, text="行3", values=("3A", "3B", "3C"))

    table.pack()
