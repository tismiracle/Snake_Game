from PIL import Image


for i in range(1, 28):
    image = Image.open(rf"Tongue\Tongue_up\{i}.png")
    image = Image.Image.rotate(image, 180)
    image.save(rf"Tongue\Tongue_down\{i}.png")