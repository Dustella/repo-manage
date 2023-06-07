import tkinter as tk
from tkinter import messagebox


class MenuWindow:
    from entities.User import User
    def __init__(self,user:User):
        self.init_menu()
        self.user = user

    def open_entry_in_window(self):
        pass

    def open_entry_out_window(self):
        pass

    def open_item_table_window(self):
        
        from views.EntryTable import init_data_table
        pass

    def open_user_table_window(self):
        pass

    def open_customer_manage_window(self):
        pass

    def init_menu(self):
        menu = tk.Tk()
        menu.title("主菜单")

        font_config = {
            "width": 100,
            "font": ("Microsoft Yahei", 14),
            # margin
        }
        # add welcome message
        label1 = tk.Label(menu, text="欢迎您，" + self.user.username, **font_config)
        label1.pack()

        # add four buttons
        button1 = tk.Button(menu, text="录入", command=self.open_entry_in_window, **font_config)
        button1.pack()

        button2 = tk.Button(menu, text="出库", command=self.open_entry_out_window, **font_config)
        button2.pack()

        button3 = tk.Button(menu, text="商品表格", command=self.open_item_table_window, **font_config)
        button3.pack()

        # 管理用户
        button4 = tk.Button(menu, text="管理用户", command=self.open_user_table_window , **font_config)
        button4.pack()

        # 管理客户
        button5 = tk.Button(menu, text="管理客户", command=self.open_customer_manage_window, **font_config)
        button5.pack()

        button6 = tk.Button(menu, text="退出", command=menu.destroy, **font_config)
        button6.pack()
