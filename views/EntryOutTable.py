from tkinter import ttk, messagebox
import tkinter as tk
from typing import List

class EntryOutTable:

    def select_item(self,event):
        self.seleted= []

        selected = self.table.focus()
        item = self.table.item(selected,"text")
        self.seleted.append(item)

    def delete_item(self):
        if len(self.seleted) == 0:
            messagebox.showinfo("No selection")
        else:
            from entities.EntryOut import EntriesOut
            EntriesOut.delete_by_id(int(self.seleted[0]))
            self.table.pack_forget()
            self.button.pack_forget()
            self.add_table()
    def add_table(self):
        self.seleted= []
        table = ttk.Treeview(self.data_window)
        self.table = table
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
        for item in data:
            line = (item.user.username,
                    item.time,
                    item.item.name,
                    item.amount,
                    item.quantity)

            table.insert("", tk.END, text=f"{item.id}",
                         values=line)
        table.bind('<<TreeviewSelect>>',self.select_item)
        table.pack()
        button = tk.Button( self.data_window,text="删除",command=self.delete_item)
        button.pack()
        self.button = button



    def __init__(self):
        data_window = tk.Tk()
        data_window.title("数据表格")
        self.data_window = data_window
        self.add_table()

