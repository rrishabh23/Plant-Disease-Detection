
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import pandas as pd
import Classifier

File = "testimage/grape_black_rot.jpg"
text = File
img = cv2.imread(File)
img = cv2.resize(img,(256,256))
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

channel = imgHSV[:,:,0]
mask = cv2.inRange(channel, 40, 80)
leaf = cv2.bitwise_and(img,img, mask= mask)
defect = cv2.bitwise_and(img,img, mask= ~mask)

histr = cv2.calcHist([channel],[0],None,[16],[0,256])
histv = list(map(int,histr))
plt.plot(histr,color = 'g')
plt.xlim([0,16])
#plt.ylim([0,4000])
plt.show()


colors =["#000000","#ff8f00","#ffef00","#afff00","#50ff00","#00ff10","#00ff70","#00ffcf","#00cfff","#0070ff","#0010ff","#5000ff","#af00ff","#ff00ef","#ff008f","#ffffff"]
titles=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
plt.bar(titles, histv, color=colors)
#,edgecolor='black')
plt.show()


cv2.imshow('Leaf',leaf)
cv2.imshow('Defect',defect)

cv2.waitKey(0)
cv2.destroyAllWindows()

histv.pop(0)
tot=sum(histv)
y=round(100*(histv[0]+histv[1])/tot,5)
g=round(100*(histv[2]+histv[3]+histv[4])/tot,5)
c=round(100*(histv[5]+histv[6]+histv[7])/tot,5)
b=round(100*(histv[8]+histv[9]+histv[10])/tot,5)
m=round(100*(histv[11]+histv[12]+histv[13])/tot,5)

print('Composition of image - \nYellow  : ',y,'%\nGreen   : ',g,'%\nCyan    : ',c,'%\nBlue    : ',b,'%\nMagenta : ',m,'%')



n = input("\nDo you want to test this image? (Y/N):")
directory = 'featuredataset'
filename = directory+'/test.csv'
imgid = text.split('/')[1][:-4][:5]

if  n == 'y'or'Y':
   	fieldnames = ['imgid', 'Yellow', 'Green', 'Cyan', 'Blue', 'Magenta']
   	print ('Appending to ' + str(filename.split('/')[1])+ '...')

   	try:
   		log = pd.read_csv(filename)
   		L = [imgid, str(y), str(g), str(c), str(b), str(m)]
   		my_df = pd.DataFrame([L])
   		my_df.to_csv(filename, mode='a', index=False, header=False)
   		print ('\nFile ' + str(filename.split('/')[1])+ ' updated!' )

   	except IOError:
   		if directory not in os.listdir():
   			os.system('mkdir ' + directory)

   		foldnum = 0
   		L = [imgid, str(y), str(g), str(c), str(b), str(m)]
   		my_df = pd.DataFrame([fieldnames, L])
   		my_df.to_csv(filename, index=False, header=False)
   		print ('\nFile ' + str(filename.split('/')[1])+ ' updated!' )

   	print("\n================================\nChecking for this image...\n================================\n\n")
   	Classifier.test_image()

else :
   	print ('File not updated! \nSuccessfully terminated!')

