from tkinter.ttk import *

class Application(Frame):
    def __init__(self, master=None):
        # 在Tkinter中，Frame组件是复杂布局的基本组织单元。
        # Frame是一个矩形区域，可以包含其他组件。
        Frame.__init__(self, master)
        # pack()方法是Tkinter中用于布局管理的一个方法。
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

if __name__ == "__main__":
    app = Application()
    app.master.title('Hello World')
    app.master.geometry('300x200')  # 设置窗口大小
    app.mainloop() # 启动应用