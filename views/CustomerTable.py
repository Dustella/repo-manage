from tkinter import ttk
import tkinter as tk
from typing import List


class CustomerTable:

    def __init__(self):

        self.init_data_table()

    def init_data_table(self):
        data_window = tk.Tk()
        data_window.title("数据表格")

        table = ttk.Treeview(data_window)
        table["columns"] = ("1", "2", "3", "4")
        table.column("#0", width=0, stretch=tk.NO)
        table.column("1", width=100, anchor=tk.CENTER)
        table.column("2", width=100, anchor=tk.CENTER)
        table.column("3", width=100, anchor=tk.CENTER)
        table.column("4", width=100, anchor=tk.CENTER)

        table.heading("#0", text="", anchor=tk.CENTER)
        table.heading("1", text="用户", anchor=tk.CENTER)
        table.heading("2", text="电话", anchor=tk.CENTER)
        table.heading("3", text="地址", anchor=tk.CENTER)
        table.heading("4", text="备注", anchor=tk.CENTER)

        from entities.Customer import Customer
        data: List[Customer] = Customer.select()
        
        for item in data:
            line = (item.name,
                    item.phone,
                    item.address,
                    item.note)
            table.insert("", tk.END, text="的",
                         values=line)

        table.pack()
