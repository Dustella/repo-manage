from tkinter import ttk
import tkinter as tk
from typing import List
from entities.Item import Item

from entities.User import User


class EntryOutTable:
    from entities.EntryOut import EntriesOut
    data: List[EntriesOut] = []

    def __init__(self):

        self.init_data_table()

    def init_data_table(self):
        data_window = tk.Tk()
        data_window.title("数据表格")

        table = ttk.Treeview(data_window)
        table["columns"] = ("1", "2", "3", "4", "5")
        table.column("#0", width=0, stretch=tk.NO)
        table.column("1", width=100, anchor=tk.CENTER)
        table.column("2", width=100, anchor=tk.CENTER)
        table.column("3", width=100, anchor=tk.CENTER)
        table.column("4", width=100, anchor=tk.CENTER)
        table.column("5", width=100, anchor=tk.CENTER)

        table.heading("#0", text="", anchor=tk.CENTER)
        table.heading("1", text="用户", anchor=tk.CENTER)
        table.heading("2", text="时间", anchor=tk.CENTER)
        table.heading("3", text="商品", anchor=tk.CENTER)
        table.heading("4", text="数量", anchor=tk.CENTER)
        table.heading("5", text="金额", anchor=tk.CENTER)

        from entities.EntryOut import EntriesOut
        data: List[EntriesOut] = EntriesOut.select()

        print(data)

        for item in data:
            line = (item.user.username,
                    item.time,
                    item.item.name,
                    item.amount,
                    item.quantity)

            print(line)
            table.insert("", tk.END, text="的",
                         values=(item.user.username,
                                 item.time,
                                 item.item.name,
                                 item.amount,
                                 item.quantity))

        table.pack()
