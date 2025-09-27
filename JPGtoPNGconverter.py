import sys
import os
from PIL import Image


def jpg_to_png_convertor(target_dir, destination_dir):
    """Function to convert JPG files to PNG files"""

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    for filename in os.listdir(target_dir):
        file = filename.strip()
        f, e = file.split(".")
        outfile = f + ".png"
        if filename != outfile:
            try:
                with Image.open(f"{target_dir}\\{filename}") as img:
                    print(
                        f"Saving {target_dir}\\{filename} to {destination_dir}\\{outfile}")
                    img.save(f"{destination_dir}\\{outfile}")
            except OSError as e:
                print("Cannot convert", filename, e)


if __name__ == '__main__':
    target_dir = sys.argv[1]
    destination_dir = sys.argv[2]

    jpg_to_png_convertor(target_dir, destination_dir)