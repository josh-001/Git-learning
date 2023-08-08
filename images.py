import os
from PIL import Image

def is_image_readable(image_path):
    try:
        with Image.open(image_path) as img:
            img.verify()
            return True
    except:
        return False

def move_readable_images(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if is_image_readable(file_path):
            destination_path = os.path.join(destination_folder, filename)
            os.rename(file_path, destination_path)
            print(f"Moved readable image: {filename}")

if __name__ == "__main__":
    source_folder = "/home/bhanu/Documents/Image"  # Replace with the path to your source folder
    destination_folder = "/home/bhanu/Documents/readimg"  # Replace with the path to your destination folder

    move_readable_images(source_folder, destination_folder)

