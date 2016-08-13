from images_funcs import shades_func
from images_funcs import ImgInStr
picture = str(input('picture:')+".jpg")

pixels,width,height = shades_func(picture)
mass = ImgInStr(pixels,width,height)
print (str(mass[100,100]))


