from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\N I T R O\multimedia\LAB-4(SUYOG)\sung.jpg")

img_array = np.array(img)

if img_array.ndim == 2:
    cropped_array = img_array[100:600, 100:600]
else:
    cropped_array = img_array[100:600, 100:600, :]

cropped_img = Image.fromarray(cropped_array)
cropped_img.show()
