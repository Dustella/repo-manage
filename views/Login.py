import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



class LoginWindow():
    def __init__(self):
        self.init_login_window()

    def authen(self,username,password):
        username_text = username.get()
        password_text = password.get()
        from entities.User import User
        try:
            user = User.authenticate(username_text, password_text)
            return True
        except ValueError as e:
            messagebox.showerror("错误", e)
            return False
        
        
    def login(self):
            # if authen(username,password):
        if True:
            from views.EntryTable import init_data_table
            self.login_window.destroy()
            init_data_table()
            

        else:
            messagebox.showerror("错误", "密码错误！")
        

    def init_login_window(self):
        login_window = tk.Tk()
        self.login_window = login_window
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
        self.username = username
        username.pack()

        password_label = tk.Label(login_window, text="密码：")
        password_label.pack()

        password = tk.Entry(login_window, show="*", **font_config )
        self.password = password
        password.pack(pady=30)

        login_button = tk.Button(login_window, text="登陆", command=self.login,**font_config)
        login_button.pack()
        login_window.mainloop()
