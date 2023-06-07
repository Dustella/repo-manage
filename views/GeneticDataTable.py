from tkinter import ttk
import tkinter as tk
from typing import List
from peewee import Model


class GeneticDataTable:
    from entities.EntryOut import EntriesOut
    data: List[EntriesOut] = []

    def __init__(self, model: Model):
        self.model = model
        keys = list(model.__dict__.keys())
        keys = filter(lambda x: not x.startswith("_"), keys)
        self.keys = keys

        self.init_data_table()

    def init_data_table(self):
        data_window = tk.Tk()
        data_window.title("数据表格")

        table = ttk.Treeview(data_window)
        keys = self.keys

        table["columns"] = tuple(keys)

        table.column("#0", width=0, stretch=tk.NO)
        for key in keys:
            table.column(key, width=100, anchor=tk.CENTER)

        table.heading("#0", text="", anchor=tk.CENTER)
        for i in range(len(keys)):
            table.heading(keys[i], text=keys[i], anchor=tk.CENTER)

        data: List[self.model] = self.model.select()

        print(data)

        for item in data:
            line = tuple(map(lambda x: getattr(item, x), keys))

            print(line)
            table.insert("", tk.END, text="的",
                         values=line)

        table.pack()
