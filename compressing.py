from PIL import Image
import numpy as np
import math
from scipy.fftpack import dct

try:
    img = Image.open("oasis.jpg")
except IOError:
    print("Error in retrieving image")
    pass

img = img.resize((16,16))
width, height = img.size
Y_values = []
Cb_values = []
Cr_values = []

for y in range(0,height):
    Y_temp = []
    Cb_temp = []
    Cr_temp = []
    for x in range(0,width):
        r,g,b = img.getpixel((x,y))#For me this gets different values from https://imagecolorpicker.com/ but they are very close. 
        Y_temp.append(int(0.299*r +0.587*g +0.114*b))
        Cb_temp.append(int(-0.168935*r -0.331665*g +0.50059*b)) #From my notes it is a +128 here but not in Johans. https://chalmers.instructure.com/courses/33297/files/3896445?wrap=1
        Cr_temp.append(int(0.499813*r -0.4187*g -0.081282*b))#+128 here as well. 

    Y_values.append(Y_temp)
    Cb_values.append(Cb_temp)
    Cr_values.append(Cr_temp)

transformed = dct(dct(Y_values,norm='ortho').T, norm='ortho') #The ortho makes it multiple with the scaling factor. 
print(transformed)

#result += Y_values[y][x]*math.cos((((2*x+1)*x*math.pi)/16)) *math.cos((((2*y+1)*y*math.pi)/16))




#img.save("changed_oasis.jpg")
