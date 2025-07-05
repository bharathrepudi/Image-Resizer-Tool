import os
from PIL import Image
import sys

# Set default resize size or take from command-line arguments
resize_to = (800, 800)
if len(sys.argv) == 3:
    try:
        resize_to = (int(sys.argv[1]), int(sys.argv[2]))
    except ValueError:
        print("Invalid dimensions provided. Using default 800x800.")

# Define input and output directories
input_folder = 'images'
output_folder = 'output'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in input folder
for filename in os.listdir(input_folder):
    try:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Preserve aspect ratio while resizing
            img.thumbnail(resize_to)

            # Change format to PNG
            base_filename = os.path.splitext(filename)[0]
            new_filename = f"{base_filename}.png"
            output_path = os.path.join(output_folder, new_filename)

            # Avoid overwriting existing files
            if os.path.exists(output_path):
                print(f"{new_filename} already exists, skipping.")
                continue

            # Save resized image
            img.save(output_path, format='PNG')
            print(f"Resized and saved: {new_filename}")
        else:
            print(f"Skipped non-image file: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
