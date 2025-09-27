from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")
filtered_img = img.filter(ImageFilter.BLUR)


# print(img)
# for attr in img.__dir__():
#     if not attr.startswith("_"):
#         print(attr)
print("#################")
print(img.filename)
print(img.layer)
print(img.format)
print(img.format_description)
print(img.size)
print(img.mode)
img.show()

