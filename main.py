import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from db import User, EntriesIn, EntriesOut, db

db.connect()
db.create_tables([User ,EntriesIn, EntriesOut])

def authen():
    username_text = username.get()
    password_text = password.get()
    try:
        user = User.authenticate(username_text, password_text)
        return True
    except ValueError as e:
        messagebox.showerror("错误", e)
        return False
    
    
def login():
    if authen():
        login_window.destroy()
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

    else:
        messagebox.showerror("错误", "密码错误！")

login_window = tk.Tk()
login_window.title("登陆")
# set its geometry to 900x800
login_window.geometry("900x400")

font_config = {
    "width" : 100,
    "font"  :("Microsoft Yahei",14),
    # margin
    # "padx"  : (10,10),
}

username_label = tk.Label(login_window, text="用户名：")
username_label.pack()


username = tk.Entry(login_window, **font_config)
username.pack()

password_label = tk.Label(login_window, text="密码：")
password_label.pack()

password = tk.Entry(login_window, show="*", **font_config )
password.pack(pady=30)

login_button = tk.Button(login_window, text="登陆", command=login,**font_config)
login_button.pack()

login_window.mainloop()
