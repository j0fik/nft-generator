from PIL import Image
import os

def combine_images(base_image, layers, output_path):
    combined_image = base_image.copy()
    for layer in layers:
        combined_image.paste(layer, (0, 0), layer)
    combined_image.save(output_path)

def get_images_from_folder(folder_path):
    return [Image.open(os.path.join(folder_path, f)) for f in os.listdir(folder_path) if f.endswith('.png')]

def main():
    base_image_path = "D:\\Videá\\xyz\\xyz.jpg"
    base_image = Image.open(base_image_path)
    folders = ["dvere", "komin", "obloha", "stena", "strecha"]
    images = [get_images_from_folder(f"D:\\Videá\\xyz\\{folder}") for folder in folders]
    
    output_folder = "D:\\Videá\\xyz\\z-final"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    counter = 0
    for dvere in images[0]:
        for komin in images[1]:
            for obloha in images[2]:
                for stena in images[3]:
                    for strecha in images[4]:
                        output_path = os.path.join(output_folder, f"final{counter}.jpg")
                        combine_images(base_image, [dvere, komin, obloha, stena, strecha], output_path)
                        counter += 1

if __name__ == "__main__":
    main()
