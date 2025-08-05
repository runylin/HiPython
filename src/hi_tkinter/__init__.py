# 官方文档：https://docs.python.org/zh-cn/3.13/library/tk.html
# https://www.pytk.net/tkinter/1657853591.html

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # 创建应用程序变量。
        self.contents = tk.StringVar()
        # 将其设为特定的值。
        self.contents.set("this is a variable")
        # 告诉输入控件监视此变量。
        self.entrythingy["textvariable"] = self.contents

        # 定义一个回调在用户按下回车时调用。
        # 它将打印变量的当前值。
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()