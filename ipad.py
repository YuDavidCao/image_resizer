import os
from PIL import Image

def resize_image(input_image_path, output_image_path, new_size):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(new_size, Image.Resampling.LANCZOS)
    resized_image.save(output_image_path)

def resize_jpg_images(directory, new_size):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            input_image_path = os.path.join(directory, filename)
            output_image_path = os.path.join(directory, "resized_" + filename)
            resize_image(input_image_path, output_image_path, new_size)
            print(f"Resized {filename} successfully.")

current_directory = os.getcwd()
new_size = (2048, 2732)
  # Change to your desired dimensions
resize_jpg_images(current_directory, new_size)
