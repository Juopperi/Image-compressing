from PIL import Image
import numpy as np
from scipy.fftpack import dct
import os

def zigzag(array):
    lst = []
    direction = "down"
    x,y = 0

    while(x,y != len(array)): 
        while(x > 0 or y > 0):
            match direction:
                case "down":
                    x -= 1
                    y += 1
                case "up":
                    x += 1
                    y -= 1
                case _:
                    print("error in direction")
            lst.append(array[y][x])
        
        if direction == "down":
            y += 1
            direction = "up"
        elif direction == "up":
            x += 1
            direction = "down"
        lst.append(array[y][x])
    
    return lst
        



quantTable = np.array([[16,	11,	10,	16,	24,	40,	51,	61], 
                       [12,	12,	14,	19,	26,	58,	60,	55],
                       [14,	13,	16,	24,	40,	57,	69,	56],
                       [14,	17,	22,	29,	51,	87,	80,	62],
                       [18,	22,	37,	56,	68,	109,103,77],
                       [24,	35,	55,	64,	81,	104,113,92],
                       [49, 64,	78,	87,	103,121,120,101],
                       [72, 92,	95,	98,	112,100,103,99]])
#https://www.sciencedirect.com/topics/computer-science/quantization-table

try:
    img = Image.open("oasis.png")
except IOError:
    print("Error in retrieving image")
    pass
os.path.getsize("oasis.png")

img = img.resize((512,512))
width, height = img.size
Y_values = []
Cb_values = []
Cr_values = []
Quant_values = []

for y in range(0,height):
    Y_temp = []
    Cb_temp = []
    Cr_temp = []
    for x in range(0,width):
        pixel = img.getpixel((x,y))#For me this gets different values from https://imagecolorpicker.com/ but they are very close. 
        r,g,b = pixel[0],pixel[1],pixel[2]
        Y_temp.append(int(0.299*r +0.587*g +0.114*b))
        Cb_temp.append(int(-0.168935*r -0.331665*g +0.50059*b)) #From my notes it is a +128 here but not in Johans. https://chalmers.instructure.com/courses/33297/files/3896445?wrap=1
        Cr_temp.append(int(0.499813*r -0.4187*g -0.081282*b))#+128 here as well. 
    Y_values.append(Y_temp)
    Cb_values.append(Cb_temp)
    Cr_values.append(Cr_temp)

transformed = dct(dct(Y_values,norm='ortho').T, norm='ortho') #The ortho makes it multiple with the scaling factor. 

for y in range(0,height,8):
    Quant_temp = []
    for x in range(0,width,8):
        Quant_temp.append(np.dot(transformed[x:x+8,y:y+8],np.linalg.inv(quantTable)))
    Quant_values.append(Quant_temp)

print(zigzag(quantTable))

