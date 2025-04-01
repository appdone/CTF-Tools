from PIL import Image
import os, sys

def convert_images_to_webp(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_folder, file)
            img = Image.open(img_path)
            webp_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".webp")
            img.save(webp_path, "WEBP", quality=80)
            print(f"+ {file} > {os.path.basename(webp_path)}")

convert_images_to_webp(sys.argv[1], sys.argv[2])
