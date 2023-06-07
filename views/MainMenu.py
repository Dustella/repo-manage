import tkinter as tk
from tkinter import messagebox


class MenuWindow:
    from entities.User import User

    def __init__(self, user: User):
        self.user = user
        self.init_menu()

    def open_entry_in_window(self):

        pass

    def open_entry_out_window(self):
        if self.user.role == "超级管理员" or self.user.role == "销售员":
            from views.GeneticDataTable import GeneticDataTable
            from entities.EntryOut import EntriesOut
            GeneticDataTable(EntriesOut)
        else:
            messagebox.showerror("错误", "您没有权限进行此操作！")

    def open_item_table_window(self):

        from views.EntryInTable import init_data_table
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
        label1 = tk.Label(menu, text="欢迎您，" +
                          self.user.username, **font_config)
        label1.pack()

        label2 = tk.Label(menu, text="您的权限是：" + self.user.role, **font_config)
        label2.pack()

        label3 = tk.Label(menu, text="请选择您要进行的操作：", **font_config)
        label3.pack()
        # add four buttons
        button1 = tk.Button(
            menu, text="录入", command=self.open_entry_in_window, **font_config)
        button1.pack()

        button2 = tk.Button(
            menu, text="出库", command=self.open_entry_out_window, **font_config)
        button2.pack()

        button3 = tk.Button(menu, text="商品表格",
                            command=self.open_item_table_window, **font_config)
        button3.pack()

        # 管理用户
        button4 = tk.Button(menu, text="管理用户",
                            command=self.open_user_table_window, **font_config)
        button4.pack()

        # 管理客户
        button5 = tk.Button(
            menu, text="管理客户", command=self.open_customer_manage_window, **font_config)
        button5.pack()

        button6 = tk.Button(
            menu, text="退出", command=menu.destroy, **font_config)
        button6.pack()
