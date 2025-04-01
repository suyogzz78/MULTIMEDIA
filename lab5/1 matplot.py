import matplotlib.pyplot as plt
from PIL import Image
img = Image.open('C:\\Users\\N I T R O\\multimedia\\lab5\\lenna.jpg')
img = img.convert('L')
pixels = list(img.getdata())
plt.hist(pixels, bins=256, range=(0, 255), color='gray', alpha=0.8)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram of Lenna.jpg')
plt.show()