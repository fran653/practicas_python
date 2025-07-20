from PIL import Image
im = Image.open("hopper.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")

