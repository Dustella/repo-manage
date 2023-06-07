from tkinter import messagebox, ttk
import tkinter as tk
from typing import List


class UserTable:
    def add_table(self):
        
        table = ttk.Treeview(self.data_window)

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

    def add_user(self):
        from entities.User import User
        user = User()
        user.username = self.entry_username.get()
        user.password = self.entry_password.get()
        user.role = self.role_string.get()
        res=  user.save()
        self.add_table()
        if res:
            messagebox.showinfo("提示", "添加成功")
        else:
            messagebox.showinfo("提示", "添加失败")

    def __init__(self):
        data_window = tk.Tk()
        data_window.title("数据表格")
        self.data_window = data_window
        self.add_table()

        # form for add new user
        title = tk.Label(data_window, text="添加用户")
        title.pack()

        label_username = tk.Label(data_window, text="用户名")
        label_username.pack()

        entry_username = tk.Entry(data_window)
        entry_username.pack()
        self.entry_username = entry_username

        label_password = tk.Label(data_window, text="密码")
        label_password.pack()
        
        entry_password = tk.Entry(data_window)
        entry_password.pack()
        self.entry_password = entry_password

        label_role = tk.Label(data_window, text="角色")
        label_role.pack()

        role_string = tk.StringVar()
        role_string.set("管理员")
        entry_role = tk.OptionMenu(data_window, role_string, "管理员", "销售员","采购员")
        entry_role.pack()
        self.role_string = role_string

        button_add = tk.Button(data_window, text="添加", command=self.add_user)
        button_add.pack()

