import numpy as np
from PIL import Image

#Create 3d numpy array of zeros
data = np.zeros((5, 4, 3), dtype= np.uint8)
data[:]=[255 ,255 , 0]
print(data)
#make red  patach
data[1:4, 1:3]=[255, 200, 233]
data[3:4, 1:4] = [45, 3, 233]
 
img = Image.fromarray(data, 'RGB')
img.save('canvas.png')




