from PIL import Image
im = Image.open("poside.webp").convert("RGB")
im.save("poside.jpg", "jpeg")