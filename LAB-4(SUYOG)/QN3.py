from PIL import Image

img = Image.open(r"C:\Users\N I T R O\multimedia\LAB-4(SUYOG)\sung.jpg")
grayscale_img = Image.new('L', img.size)
for x in range(img.width):
    for y in range(img.height):
        r, g, b = img.getpixel((x, y))
        grayscale = int(0.299 * r + 0.587 * g + 0.114 * b)
        grayscale_img.putpixel((x, y), grayscale)
threshold = 128
binary_img = Image.new('1', img.size)
for x in range(grayscale_img.width):
    for y in range(grayscale_img.height):
        intensity = grayscale_img.getpixel((x, y))
        if intensity >= threshold:
            binary_img.putpixel((x, y), 1)
        else:
            binary_img.putpixel((x, y), 0)
binary_img.show()
