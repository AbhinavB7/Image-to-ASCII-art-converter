#the code is not yet complete
#image to ASCII 

from PIL import Image, ImageDraw, ImageFont
from sys import argv

WIDTH_OF_REGION = 1
HEIGHT_OF_REGION = int(WIDTH_OF_REGION * 2)

char_map = {}

#Convert image to chars

def char_image(char):
    font = ImageFont.truetype("Monaco", 40)
    image = Image.new('RGB', (50, 50), (255, 255, 255))
    drawer = ImageDraw.Draw(image)
    drawer.text((0, 0), char, font=font, fill=(0, 0, 0))
    image = image.convert('1')
    return image

#adding gray value to image

def avg_gray_value(image):
    
    width, height = image.size
    total_pixels_value = width * height * 255
    gray_value = 0
    for x in range(0, width):
        for y in range(0, height):
            gray_value += image.getpixel((x, y))
    return int(gray_value/total_pixels_value*10000)
