from PIL import Image
with Image.open("hopper.jpg") as im:
    im.rotate(45).show()