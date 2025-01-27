from PIL import Image

try:
    img = Image.open("oasis.jpg")
except IOError:
    print("Error in retrieving image")
    pass

img = img.resize((512,512))
Y_values = []
Cb_values = []
Cr_values = []


for y in range(0,512):
    Y_temp = []
    Cb_temp = []
    Cr_temp = []
    for x in range(0,512):
        r,g,b = img.getpixel((x,y))#For me this gets different values from https://imagecolorpicker.com/ but they are very close. 
        Y_temp.append(int(0.299*r +0.587*g +0.114*b))
        Cb_temp.append(int(-0.168935*r -0.331665*g +0.50059*b)) #From my notes it is a +128 here but not in Johans. https://chalmers.instructure.com/courses/33297/files/3896445?wrap=1
        Cr_temp.append(int(0.499813*r -0.4187*g -0.081282*b))#+128 here as well. 

    Y_values.append(Y_temp)
    Cb_values.append(Cb_temp)
    Cr_values.append(Cr_temp)






    




img.save("changed_oasis.jpg")
