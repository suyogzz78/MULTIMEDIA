from PIL import Image

def view_bmp(img_path):
    try:
        img = Image.open(img_path)
        img.show()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    bmp_path = input("Enter the path to the BMP file: ")
    view_bmp(bmp_path)
