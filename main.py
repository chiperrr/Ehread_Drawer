from images_funcs import shades_func
from images_funcs import ImgInInt
from images_funcs import DrawingImage
from Mass_funcs import MassMovementToMax
from Mass_funcs import MassMovementToMaxBright
from Mass_funcs import MaxBright
from Mass_funcs import MinBright
from Mass_funcs import BlackAndWhite
picture = str(input('picture:')+".jpg")             #получаем название имя файла картинки
pixels,width,height = shades_func(picture)          #загрузка картинки, получение основных данных
mass = ImgInInt(pixels,width,height)                #переводим заначения пиксилей в двумерный список 0..255 (значение яркости)
mass =MassMovementToMaxBright(mass,width,height,MaxBright(mass,width,height)) #Смещение самого светлого цвета к 255... Зачем?---- хзхзххз
mass = MassMovementToMax(mass,width,height,50,MinBright(mass,width,height))    #Смещение всех оттенков к саомму яркому, самый тусклый 255-фактор
mass = BlackAndWhite(mass,width,height,250)
DrawingImage(mass,width,height,1)




