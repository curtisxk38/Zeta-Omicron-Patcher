import os
import shutil
import sys

def replace_patch_name(patch_folder):
    patch_folder = patch_folder.replace("Copy into Graphics_", "")
    return patch_folder

def find_files(folder):
    files = [x for x in os.listdir(folder)]
    return files

def move_file(path, files, dest):
    for entry in files:
        entry = os.path.join(path, entry)
        try:
            shutil.copy(entry, dest)
        except:
            print( "error in moving " + entry + " to " + dest)

def print_move_info(source, files, dest):
    print("\nCopying: ")
    text = "\t"
    for x in range(len(files)):
        text += files[x]
        if x != len(files) - 1:
            text += ", "
    print(text)
    print("From " + source + " to " + dest)

base_dir = os.getcwd()
print("Put this file in a folder with the main Omicron/Zeta folder and the patch folder you want to use")
if len(sys.argv) == 3:
    patch_dir = sys.argv[1]
    main_dir = sys.argv[2]
else:
    patch_dir = os.path.join(base_dir, input("Enter the patch folder name: ")) #Omicron 1.2.14
    main_dir = os.path.join(base_dir, input("Enter the main game folder: ")) #Pokemon Omicron (Win)

patch_folder_name = []
for root, dirs, files in os.walk(patch_dir):
    for folder in dirs:
        patch_folder_name.append(folder)
    break

for entry in patch_folder_name:
    entry_path = os.path.join(patch_dir, entry)
    files = find_files(entry_path)
    main_dest_path = os.path.join(main_dir, "Graphics", replace_patch_name(entry))
    print_move_info(entry_path, files, main_dest_path)
    move_file(entry_path, files, main_dest_path)

rgssad = "Game.rgssad"
print("\nCopying " + os.path.join(patch_dir, rgssad) + " to " + main_dir)
try:
    shutil.copy(os.path.join(patch_dir, rgssad), main_dir)
except:
    print("error in moving " + rgssad)

if len(sys.argv) != 3:
    input()
