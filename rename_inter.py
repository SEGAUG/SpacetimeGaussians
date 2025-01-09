import os

def rename_folders(root_path, start_index=21):
    """Rename 'interpolated_*' folders to 'camXX' starting from the given index."""
    current_index = start_index

    # 遍历根目录中的文件夹
    for folder_name in sorted(os.listdir(root_path)):
        folder_path = os.path.join(root_path, folder_name)

        # 检查是否是文件夹且以 'interpolated_' 开头
        if os.path.isdir(folder_path) and folder_name.startswith("interpolated_"):
            # 构建新文件夹名称
            new_folder_name = f"cam{current_index:02d}"
            new_folder_path = os.path.join(root_path, new_folder_name)

            # 重命名文件夹
            os.rename(folder_path, new_folder_path)
            print(f"Renamed: {folder_path} -> {new_folder_path}")

            # 更新索引
            current_index += 1

if __name__ == "__main__":
    root_path = "/home/jinhuilin/code/GS/stg/SpacetimeGaussians/log/cook_spinach/test/ours_10000/renders"  # 替换为实际路径
    rename_folders(root_path)
