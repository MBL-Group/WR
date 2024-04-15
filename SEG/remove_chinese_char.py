import os
import re

def remove_chinese_and_spaces(text):
    pattern = re.compile('[\u4e00-\u9fa5]')
    result = re.sub(pattern, 'x', text)
    # 删除中文字符附近的空格
    result = re.sub(r'\s+', ' ', result).strip()
    # 删除所有空格
    result = result.replace(' ', '')
    return result

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        old_filepath = os.path.join(folder_path, filename)
        if os.path.isfile(old_filepath):
            # Remove Chinese characters and spaces from the filename
            new_filename = remove_chinese_and_spaces(filename)
            
            # Construct the new filepath
            new_filepath = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f'Renamed: {filename} -> {new_filename}')

# 指定文件夹路径
folder_path = 'embryo_images_labelme'

# 调用函数进行重命名
rename_files(folder_path)
