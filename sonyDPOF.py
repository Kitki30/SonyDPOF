import os
import shutil

print("Welcome to Kitki30's SONY DPOF Reader")
print("Reads images from DPOF file and copies it to folder on your PC!")
print("Warning all folder / file locations must have '/' instead of '\'")
print("Script tested on Sony Cybershot DSC-H10 camera!")
print("Camera / Memory Stick location: ")
sd_card_root = input()
print("Trying to auto find DPOF File")
# DPOF searching locations
# Please contribute if you have seen other dpof location
dpof_locations = ['MISC/AUTPRINT.MRK']
found = False
dpof_file_path = ""
for loc in dpof_locations:
    if os.path.exists(sd_card_root + loc):
        print("DPOF File found at: "+loc)
        found = True
        dpof_file_path = sd_card_root + loc
        with open(dpof_file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            if line.strip().startswith('GEN CRT'):
                start_idx = line.find('"') + 1
                end_idx = line.rfind('"')
                print("Camera name: " + line[start_idx:end_idx])
if found == False:
    print("DPOF File could not be found automatically! Please enter it manually.")
    print("DPOF File path: ")
    dpof_file_path = input()
    with open(dpof_file_path, 'r') as file:
            lines = file.readlines()
    for line in lines:
        if line.strip().startswith('GEN CRT'):
            start_idx = line.find('"') + 1
            end_idx = line.rfind('"')
            print("Camera name: " + line[start_idx:end_idx])
print("Destination folder:")
destination_folder = input()

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

with open(dpof_file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    if '<IMG SRC =' in line:
        start_idx = line.find('"../') + 4
        end_idx = line.find('">')
        image_path_relative = line[start_idx:end_idx]
        image_path = os.path.join(sd_card_root, image_path_relative)
        try:
            shutil.copy(image_path, destination_folder)
            print(f"Copied: {image_path}")
        except FileNotFoundError:
            print(f"File not found: {image_path}")
        except OSError as e:
            print(f"Error copying {image_path}: {e}")

print("All files copied.")

print("Delete DPOF File? (Y/N)")
if str.lower(input()) == "y":
    print("Removing DPOF File...")
    os.remove(dpof_file_path)
elif str.lower(input()) == "yes":
    print("Removing DPOF File...")
    os.remove(dpof_file_path)
