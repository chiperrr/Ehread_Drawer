from images_funcs import shades_func
from images_funcs import ImgInInt
from images_funcs import DrawingImage
import  Mass_funcs
picture = str(input('picture:')+".jpg")             #получаем название имя файла картинки
pixels,width,height = shades_func(picture)          #загрузка картинки, получение основных данных
mass = ImgInInt(pixels,width,height)                #переводим заначения пиксилей в двумерный список 0..255 (значение яркости)
Mass_funcs.MassMovement(mass,width,height,Mass_funcs.MaxBright(mass,width,height))
DrawingImage(mass,width,height)




