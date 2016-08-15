from PIL import Image, ImageDraw

def ImageLoad (name):
    image = Image.open(str(name)+".jpg")
    width = image.size[0]
    height = image.size[1]
    pixels = image.load()
    mass = []



    for i in range(width):
        mass.append([])
        for j in range(height):
            mass[i].append((pixels[i,j][0]*30 + pixels[i,j][1]*59 + pixels[i,j][2]*11)/100 )

    return mass, width, height







