# DS提示词：帮我写一个python文件。
# 需要根据excel文件的信息
# （第一列为文件名，第二列为pdf的起始页。第三列为结束页），
# 切割整体的pdf文件为多个pdf文件。

import os
from pathlib import Path
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter


def split_pdf_based_on_excel(excel_path, pdf_path, output_folder):
    """
    根据Excel文件切割PDF

    参数:
    excel_path: Excel文件路径
    pdf_path: 原始PDF文件路径
    output_folder: 输出文件夹路径
    """
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 读取Excel文件
    df = pd.read_excel(excel_path, header=None, names=['filename', 'start_page', 'end_page'])

    # 读取原始PDF
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)

        for index, row in df.iterrows():
            filename = row['filename']
            start = row['start_page'] - 1  # 转换为0-based索引
            end = row['end_page']  # 结束页（包含）

            # 验证页码范围
            if start < 0 or end > total_pages or start >= end:
                print(f"⚠️ 跳过 {filename}: 无效页码范围 ({start + 1}-{end})")
                continue

            # 创建PDF写入器
            pdf_writer = PdfWriter()

            # 添加指定页面
            for page_num in range(start, end):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            # 保存切割后的PDF
            output_path = os.path.join(output_folder, f"{filename}.pdf")
            with open(output_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            print(f"✅ 已创建: {filename}.pdf (页码: {start + 1}-{end})")


if __name__ == "__main__":
    # 配置路径
    root_dir = Path(__file__).parent.parent.parent  # 工程所在目录
    data_dir = f"{root_dir.absolute()}{os.sep}data{os.sep}split_pdf"  # 数据目录
    excel_file = f"{data_dir}{os.sep}testPdf100.xlsx"  # Excel文件路径
    source_pdf = f"{data_dir}{os.sep}testPdf100.pdf"  # 原始PDF文件路径
    output_dir = f"{data_dir}{os.sep}split_results"  # 输出文件夹

    # 执行切割操作
    split_pdf_based_on_excel(excel_file, source_pdf, output_dir)
    print("\nPDF切割完成！")