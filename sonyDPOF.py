import os
import shutil

print("Welcome to Kitki30's SONY DPOF Reader")
print("Reads images from DPOF file and copies it to folder on your PC!")
print("Warning all folder / file locations must have '/' instead of '\'")
print("Script tested on Sony Cybershot DSC-H10 camera!")
print("DPOF File path: ")
dpof_file_path = input()
print("Camera / Memory Stick location: ")
sd_card_root = input()
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
