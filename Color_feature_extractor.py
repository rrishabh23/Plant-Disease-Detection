
import cv2
import os
import pandas as pd




in_dir = 'img1/Apple___Apple_scab/'

print ("\n*********************\nImage Directory : " + in_dir + "\n*********************")
filepath = [x for x in os.listdir(in_dir) if x.endswith(".jpg") or x.endswith(".JPG") or x.endswith(".JPEG") or x.endswith(".jpeg") or x.endswith(".png") or x.endswith(".PNG")]


for Fid in range(len(filepath)):
    print ("\nImage: " + str(filepath[Fid]))
    text = str(filepath[Fid])

    img = cv2.imread(in_dir+filepath[Fid])
    img = cv2.resize(img,(256,256))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    channel = imgHSV[:,:,0]
    histr = cv2.calcHist([channel],[0],None,[16],[0,256])
    histv = list(map(int,histr))

    histv.pop(0)
    tot=sum(histv)
    
    y=round(100*(histv[0]+histv[1])/tot,5)
    g=round(100*(histv[2]+histv[3]+histv[4])/tot,5)
    c=round(100*(histv[5]+histv[6]+histv[7])/tot,5)
    b=round(100*(histv[8]+histv[9]+histv[10])/tot,5)
    m=round(100*(histv[11]+histv[12]+histv[13])/tot,5)
    
    print('Composition of image - \nYellow  : ',y,'%\nGreen   : ',g,'%\nCyan    : ',c,'%\nBlue    : ',b,'%\nMagenta : ',m,'%')


    directory = 'featuredataset'
    filename = directory+'/Color_Apple_scab.csv'
    imgid = text.split('/')[-1][:-4][-6:]
    
    
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