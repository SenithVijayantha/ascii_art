from PIL import Image
import math

# Open image and convert to grayscale
im = Image.open("tony.jpg").convert("L")

# Resize image
im = im.resize((100, 50))

# Define ASCII characters
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ","]


# Iterate through each pixel in the image
for i in range(im.height):
    for j in range(im.width):
        # Get pixel brightness
        pixel = im.getpixel((j, i))
        
        # Replace pixel with corresponding ASCII character
        ascii_char = ascii_chars[int(math.floor(pixel / (256 / len(ascii_chars))))]
        print(ascii_char, end="")
    print()
