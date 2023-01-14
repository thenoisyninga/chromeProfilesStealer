import os
import shutil


def get_subdirectories_path(folder_path):
    directories_list = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isdir(file_path):
            directories_list.append(file_path)
    return directories_list

def get_path_for_files_in_dir(folder_path):
    files_list = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if not os.path.isdir(file_path):
            files_list.append(file_path)
    return files_list

def copy_file(file_path):
    print(f"Copying File {file_path.split('/')[-1]}")
    current_dir = os.getcwd()
    shutil.copy2(file_path, current_dir)

def copy_folder(orig_folder_path):
    parent_dir = os.getcwd()
    if orig_folder_path[-1] == "/":
        folder_name = orig_folder_path.split("/")[-2]
    else:
        folder_name = orig_folder_path.split("/")[-1]
    print(f"Copying folder {folder_name}.")

    new_folder_path = os.path.join(parent_dir, folder_name)
    print("new_folder_path : " + new_folder_path)
    os.mkdir(new_folder_path)
    print(f"Changin dir to {new_folder_path}")
    os.chdir(new_folder_path)
    print(f"Currently in {os.getcwd()}")

    # copy files
    file_list = get_path_for_files_in_dir(orig_folder_path)
    for file in file_list:
        copy_file(file)

    for folder in get_subdirectories_path(orig_folder_path):
        copy_folder(os.path.join(orig_folder_path, folder))

    os.chdir(parent_dir)

