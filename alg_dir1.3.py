import os
import shutil

target_dir = "pics"
files = os.listdir(target_dir)

jpg_files = [file for file in files if file.endswith('.jpg')]
data_list = []
for file_name in jpg_files:
    name_camera = file_name[:36]
    date_shoot = file_name[36:41]
    time_shoot = file_name[41:50]
    format_shoot = file_name[50:54]
    data_list.append((name_camera, date_shoot, time_shoot, format_shoot))

for data in data_list:
    destination_folder_date = os.path.join(target_dir, data[1])
    if not os.path.exists(destination_folder_date):
        os.makedirs(destination_folder_date)

    destination_folder_camera = os.path.join(destination_folder_date, data[0])
    if not os.path.exists(destination_folder_camera):
        os.makedirs(destination_folder_camera)

    source_path = os.path.join(target_dir, f"{data[0]}{data[1]}{data[2]}{data[3]}")
    destination_path = os.path.join(destination_folder_camera, f"{data[0]}{data[1]}{data[2]}{data[3]}")

    shutil.move(source_path, destination_path)

print("зайбизон")
