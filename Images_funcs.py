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
            mass[i].append((pixels[i,j][0]*30 + pixels[i,j][1]*59 + pixels[i,j][2]*11)//100 )

    return mass, width, height
def ImageBoolDriving(BoolMas,width,height,name):
    image = Image.new("L",(width,height),0)
    draw = ImageDraw.Draw(image)
    for i in range(width):
        for j in range(height):
            if BoolMas[i][j] == True:
                draw.point((i, j),(255))
            else:
                draw.point((i,j),(0))


    del draw
    image.save(str(name)+".jpg","JPEG")





