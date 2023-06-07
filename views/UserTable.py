from tkinter import ttk
import tkinter as tk
from typing import List


class UserTable:
    from entities.EntryOut import EntriesOut
    data: List[EntriesOut] = []

    def __init__(self):

        self.init_data_table()

    def init_data_table(self):
        data_window = tk.Tk()
        data_window.title("数据表格")

        table = ttk.Treeview(data_window)

        table["columns"] = ("1", "2")
        table.column("#0", width=0, stretch=tk.NO)
        table.column("1", width=100, anchor=tk.CENTER)
        table.column("2", width=100, anchor=tk.CENTER)

        table.heading("#0", text="", anchor=tk.CENTER)
        table.heading("1", text="用户", anchor=tk.CENTER)
        table.heading("2", text="角色", anchor=tk.CENTER)

        from entities.User import User
        data: List[User ] = User .select()

        for item in data:
            line = (item.username,
                    item.role)

            table.insert("", tk.END, text="的",
                         values=line)

        table.pack()
