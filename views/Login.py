import tkinter as tk
from tkinter import messagebox
from tkinter import ttk




class LoginWindow():
    def __init__(self):
        self.init_login_window()

    def authen(self,):
        username_text = self.username.get()
        password_text = self.password.get()
        from entities.User import User
        try:
            user = User.authenticate(username_text, password_text)
            return user
        except ValueError as e:
            messagebox.showerror("错误", e)
            return False
        
        
    def login(self):
        from entities.User import User
        res = self.authen()
        if isinstance(res, User):
        # if True:
            from views.MainMenu import MenuWindow
            self.login_window.destroy()
            MenuWindow(res)
            

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
