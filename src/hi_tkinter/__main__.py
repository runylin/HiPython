from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

if __name__ == "__main__":
    # 启动应用
    app = Application()
    app.master.title('Hello World')
    app.master.geometry('300x200')  # 设置窗口大小
    app.mainloop()