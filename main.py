from PIL import Image
import os

def convert_jpg_to_webp(input_path, output_path):
    image = Image.open(input_path)
    image.save(output_path, 'webp')

def batch_convert_jpg_to_webp(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        # if filename.endswith('.jpg'):
        # Construct the input and output paths
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + '.webp'
        output_path = os.path.join(output_folder, output_filename)

        # Convert JPG to WebP
        convert_jpg_to_webp(input_path, output_path)
        print(f'Converted {input_path} to {output_path}')

# Example usage
input_folder = './input'
output_folder = './output'

batch_convert_jpg_to_webp(input_folder, output_folder)
