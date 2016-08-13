from images_funcs import shades_func
from images_funcs import ImgInInt
from images_funcs import DrawingImage
picture = str(input('picture:')+".jpg")             #получаем название имя файла картинки
pixels,width,height = shades_func(picture)          #загрузка картинки, получение основных данных
mass = ImgInInt(pixels,width,height)                #переводим заначения пиксилей в двумерный список 0..255 (значение яркости)
print (str(mass[370-1][429-1]))
DrawingImage(mass,width,height)



