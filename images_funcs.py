from tkinter import *
from PIL import *
from PIL import Image
from PIL import ImageDraw

def shades_func(image0):                                #функция загружает изображение и переводит в оттенки серого
    image = Image.open(image0)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = ((a * 30 + b * 59 + c * 11) // 100)
            pix[i, j] = S, S, S
    image.save("ans.jpg", "JPEG")
    assert isinstance(draw, object)
    del draw
    return (pix,width,height)

def ImgInInt(pixels,width,height):                  #первод списка пикселей в богоприятный двумерный список
    mass = []
    for r in range(width):
        mass.append([])
        for c in range(height):
            mass[r].append(0)
    for i in range (width):
        for j in range (height):
            mass[i][j] = pixels[i,j][0]
    return (mass)

def DrawingImage(shades,width,height):                 #создание изображения из числового массива
    image = Image.new("L",(width,height),0)
    draw = ImageDraw.Draw(image)
    for i in range(width):
        for j in range(height):
            draw.point((i,j),(shades[i][j]))
    image.save("answer.jpg","JPEG")
    del draw









