from tkinter import messagebox, ttk
import tkinter as tk
from typing import List


class ItemTable:
    def add_table(self):

        table = ttk.Treeview(self.data_window)
        table["columns"] = ("1", "2", "3", "4")
        table.column("#0", width=0, stretch=tk.NO)
        table.column("1", width=100, anchor=tk.CENTER)
        table.column("2", width=100, anchor=tk.CENTER)
        table.column("3", width=100, anchor=tk.CENTER)
        table.column("4", width=100, anchor=tk.CENTER)

        table.heading("#0", text="", anchor=tk.CENTER)
        table.heading("1", text="商品名字", anchor=tk.CENTER)
        table.heading("2", text="价格", anchor=tk.CENTER)
        table.heading("3", text="供应商", anchor=tk.CENTER)
        table.heading("4", text="备注", anchor=tk.CENTER)

        from entities.Item import Item
        data: List[Item] = Item.select()
        print(data)

        for item in data:
            line = (item.name,
                    item.price,
                    item.supplier,
                    item.note)

            print(line)
            table.insert("", tk.END, text="的",
                         values=line)

        table.pack()

    def add_item(self):
        from entities.Item import Item
        item = Item()
        item.name = self.input_name.get()
        item.price = self.input_price.get()
        item.supplier = self.input_supplier.get()
        item.note = self.input_note.get()
        result = item.save()
        if result:
            messagebox.showinfo("提示", "添加成功")
        else:
            messagebox.showinfo("提示", "添加失败")


    def __init__(self):

        data_window = tk.Tk()
        data_window.title("数据表格")
        self.data_window = data_window
        self.add_table()

        title = tk.Label(data_window, text="添加商品",font=("Arial", 12))
        title.pack()

        # add Input for Item
        label1 = tk.Label(data_window, text="商品名字")
        label1.pack()

        input_name = tk.Entry(data_window)
        input_name.pack()
        self.input_name = input_name

        label2 = tk.Label(data_window, text="价格")
        label2.pack()

        input_price = tk.Entry(data_window)
        input_price.pack()
        self.input_price = input_price

        label3 = tk.Label(data_window, text="供应商")
        label3.pack()

        input_supplier = tk.Entry(data_window)
        input_supplier.pack()
        self.input_supplier = input_supplier

        label4  = tk.Label(data_window, text="数量")
        label4 .pack()
        
        input_num = tk.Entry(data_window)
        input_num.pack()
        self.input_num = input_num

        label5 = tk.Label(data_window, text="备注")
        label5.pack()

        input_note = tk.Entry(data_window)
        input_note.pack()
        self.input_note = input_note

        # add sumbit button
        button = tk.Button(data_window, text="添加记录", command=self.add_item)
        button.pack()
