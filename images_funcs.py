from tkinter import *
from PIL import *
from PIL import Image
from PIL import ImageDraw

def shades_func(image0):
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

def ImgInStr(pixels,width,height):
    mass = [[],[]]
    for i in range (width):
        for j in range (height):
            mass[i][j] = pixels[i,j][0]









