import Images_funcs
import Mass_funcs
imageInt,width,height = Images_funcs.ImageLoad(2324)
print(width,height)
print(imageInt[100][100])
BoolImg = Mass_funcs.IntMassToBool(imageInt,width,height,100)
print(BoolImg[100][100])
Images_funcs.ImageBoolDriving(BoolImg,width,height,123)
