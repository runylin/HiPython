import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import os
import platform
import subprocess
from .core import split_pdf_based_on_excel

class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF文件切割工具")
        self.root.geometry("650x300")
        
        # 设置样式
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6)
        self.style.configure("TLabel", padding=6)
        self.style.configure("Info.TLabel", font=('Arial', 10), foreground="#333333")
        
        # 创建主框架
        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 添加说明文本 - 在控件上方
        instruction_text = "根据Excel文件的信息（第一列为文件名，第二列为PDF的起始页，第三列为结束页）\n切割选择的PDF文件为多个PDF文件。"
        instruction_label = ttk.Label(
            main_frame, 
            text=instruction_text,
            wraplength=550,  # 设置换行宽度
            style="Info.TLabel"
        )
        instruction_label.grid(row=0, column=0, columnspan=3, pady=(0, 15), sticky=tk.W)
        
        # Excel文件选择
        ttk.Label(main_frame, text="Excel 文件:").grid(row=1, column=0, sticky=tk.W)
        self.excel_path = tk.StringVar()
        excel_entry = ttk.Entry(main_frame, textvariable=self.excel_path, width=50)
        excel_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(
            main_frame, 
            text="浏览...", 
            command=lambda: self.select_file(self.excel_path, filetypes=[("Excel文件", "*.xlsx *.xls")])
        ).grid(row=1, column=2, padx=5)
        
        # PDF文件选择
        ttk.Label(main_frame, text="PDF 文件:").grid(row=2, column=0, sticky=tk.W)
        self.pdf_path = tk.StringVar()
        pdf_entry = ttk.Entry(main_frame, textvariable=self.pdf_path, width=50)
        pdf_entry.grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(
            main_frame, 
            text="浏览...", 
            command=lambda: self.select_file(self.pdf_path, filetypes=[("PDF文件", "*.pdf")])
        ).grid(row=2, column=2, padx=5)
        
        # 输出文件夹选择
        ttk.Label(main_frame, text="输出文件夹:").grid(row=3, column=0, sticky=tk.W)
        self.output_dir = tk.StringVar()
        output_entry = ttk.Entry(main_frame, textvariable=self.output_dir, width=50)
        output_entry.grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(
            main_frame, 
            text="浏览...", 
            command=lambda: self.select_directory(self.output_dir)
        ).grid(row=3, column=2, padx=5)
        
        # 处理按钮 - 白底黑字
        self.process_btn = ttk.Button(
            main_frame, 
            text="开始处理", 
            command=self.process_files
        )
        self.process_btn.grid(row=4, column=1, pady=20)
        
        # 设置按钮样式为白底黑字
        self.style.configure("Process.TButton", 
                             foreground="black", 
                             background="white",
                             font=('Arial', 10, 'bold'))
        self.process_btn.configure(style="Process.TButton")
    
    def select_file(self, path_var, filetypes):
        """打开文件选择对话框"""
        file_path = filedialog.askopenfilename(
            title="选择文件",
            filetypes=filetypes
        )
        if file_path:
            path_var.set(file_path)
    
    def select_directory(self, path_var):
        """打开文件夹选择对话框"""
        dir_path = filedialog.askdirectory(
            title="选择输出文件夹"
        )
        if dir_path:
            path_var.set(dir_path)

    def open_directory(self, path):
        """使用系统默认方式打开文件夹"""
        try:
            # 根据不同操作系统使用不同方法打开文件夹
            system = platform.system()
            if system == "Windows":
                os.startfile(path)
            elif system == "Darwin":  # macOS
                subprocess.Popen(["open", path])
            else:  # Linux
                subprocess.Popen(["xdg-open", path])
            return True
        except Exception as e:
            print(f"无法打开文件夹: {e}")
            return False
    
    def process_files(self):
        """处理文件函数（示例）"""
        excel = self.excel_path.get()
        pdf = self.pdf_path.get()
        output = self.output_dir.get()
        
        if not excel or not pdf or not output:
            print("请先选择所有文件和输出目录！")
            return

        # 这里添加实际处理逻辑
        print(f"Excel文件: {excel}")
        print(f"PDF文件: {pdf}")
        print(f"输出目录: {output}")
        print("文件处理中...")
        split_pdf_based_on_excel(excel, pdf, output)
        
        # 显示完成消息
        response = messagebox.askyesno(
            "处理完成",
            "文件处理已完成！\n\n是否打开输出文件夹？",
            icon="info"
        )
        if response:
            if os.path.exists(output):
                self.open_directory(output)
            else:
                messagebox.showerror("错误", f"输出文件夹不存在:\n{output}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()