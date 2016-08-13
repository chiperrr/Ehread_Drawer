from images_funcs import shades_func
from images_funcs import ImgInInt
picture = str(input('picture:')+".jpg")

pixels,width,height = shades_func(picture)
mass = ImgInInt(pixels,width,height)
print (str(mass[100][100]))


