# DS提示词：
# 有两个文件夹，一个是“待整理”，一个是“整理完成”。
# “整理完成”里有很多个文件夹，文件夹里面有mp4文件，
# “待整理”里也有很多个文件夹，文件夹里面有srt文件和jpg文件。
# 请帮我写一个python脚本，把“待整理”里的文件夹里的str文件和jpg文件，
# 拷贝到“整理完成”里的含有相同名字命名的mp4文件的文件夹里。

import os
import shutil

# 步骤1: 在目标文件夹中收集所有mp4文件的映射关系 (文件名 -> 所在文件夹路径)
def find_mp4_files(target_dir):
    """
    在目标目录中查找所有的mp4文件，并返回一个映射字典。
    字典的键是文件名（不带扩展名），值是文件所在的目录路径。
    """
    mp4_mapping = {}
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.lower().endswith('.mp4'):
                # 获取不带扩展名的文件名
                filename = os.path.splitext(file)[0]
                # 添加到映射字典 (文件名: 所在文件夹路径)
                mp4_mapping[filename] = root
    # 打印找到的mp4文件
    print(f"在 {target_dir} 总共找到 {len(mp4_mapping)} 个 MP4 文件")
    for name, srcDir in mp4_mapping.items():
        print(f"找到mp4文件，${name} - ${srcDir}")
    return mp4_mapping

# 步骤2: 遍历源文件夹中的所有文件
def find_srt_files_and_copy(source_dir, mp4_mapping):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # 只处理str和jpg文件
            if file.lower().endswith(('.srt', '.jpg')):
                # 获取不带扩展名的文件名
                filename = os.path.splitext(file)[0]
                # 检查目标文件夹中是否有同名mp4
                if filename in mp4_mapping:
                    # 获取源文件完整路径
                    src_path = os.path.join(root, file)
                    # 获取目标文件夹路径
                    dest_dir = mp4_mapping[filename]
                    # 构建目标文件路径
                    dest_path = os.path.join(dest_dir, file)
                    # 执行复制操作
                    shutil.copy2(src_path, dest_path)
                    print(f"已复制: {file} -> {dest_dir}")
                else:
                    print(f"未找到匹配项: {file} (跳过)")

def main():
    print(f"Welcome to the cp_srt_to_mp4_dir script! ")
    # 配置路径
    base_dir = "D:\Project\HiPython\data\cp_srt_to_mp4_dir"  # 基础目录
    source_dir = f"{base_dir}{os.sep}待整理" 
    target_dir = f"{base_dir}{os.sep}整理完成"
    print(f"配置文件夹路径为，待整理：{source_dir} ")
    print(f"配置文件夹路径为，整理完成：{target_dir} ")
    mp4_mapping = find_mp4_files(target_dir)  # 获取mp4文件映射
    find_srt_files_and_copy(source_dir, mp4_mapping)  # 查找并复制srt和jpg文件
    print("文件整理完成!")

if __name__ == '__main__':
    main()
