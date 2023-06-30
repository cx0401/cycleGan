import os

# 指定文件夹路径
folder_path = '/data3/wgw/pytorch-CycleGAN-and-pix2pix-master/datasets/maps/testB'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否是图片文件
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # 去除文件名中的"T1"
        new_filename = filename.replace('_B', '')
        
        # 构建旧文件路径和新文件路径
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)
        
        # 重命名文件
        os.rename(old_filepath, new_filepath)