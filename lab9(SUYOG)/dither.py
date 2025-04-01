from PIL import Image

#read the input image
img=Image.open('C:\\Users\\N I T R O\\multimedia\\lab9(SUYOG)\\selena.jpg')
dither_matrix=[[0, 128],[192, 64]]
#convert the image into gray scale
binary_img=Image.new('1', img.size)
for x in range(img.width):
    for y in range(img.height):
     intensity=sum(img.getpixel((x,y)))/3
     threshold=dither_matrix[x%2][y%2]
     if intensity>threshold:
            binary_img.putpixel((x,y), 255)
binary_img.show()