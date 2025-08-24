from rembg import remove
from PIL import Image

def remove_background(input_image):
    input = Image.open(input_image)
    output = remove(input)
    
    return output