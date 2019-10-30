from tkinter import *
from tkinter import filedialog
import os
import glob 
import cv2  
import sys
from glob import glob
#import matplotlib.pyplot as plt
#from subprocess import Popen


#Declearing List Names
dirlist = []
des_f = []

#Opening The Gui Main Page
root = Tk()

#Declearing Functions

#Function For Taking The targeted Folder
def OpenFolder():
    filename = filedialog.askdirectory()
    #print(filename)
    dirlist.append(filename)

#Function For Taking The Destination Folder
def OpenFolder1():
    filename = filedialog.askdirectory()
    #print(filename)
    des_f.append(filename)

#Function For Geting All Subdirectory List    
def dirt():
    i=1
    j=len(dirlist)
    #def ms(i):
    while(i<j+1):
        with os.scandir(dirlist[i-1]) as rit:
            for entry in rit:
                if not entry.name.startswith('.') and entry.is_dir():
                    dirlist.append(entry.path)
                    #print(entry.path)
            i=i+1
            j=len(dirlist)

#Function For Detecting Face ,Cutting Face ,Saving 48X48 image file
def Main():
    currentface = 0
    for j in dirlist:
        files = glob(j+'/*.jpg')
        files.extend(glob(j+'/*.png')) 
        for file in files:     
            image = cv2.imread(file)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #For Windows
            faceCascade = cv2.CascadeClassifier("C:\anaconda\data\haarcascades\haarcascade_frontalface_default.xml")
            #For linux
            #faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            #eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")    
            faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))    
           # print("[INFO] Found {0} Faces.".format(len(faces)))
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_color = image[y:y + h, x:x + w]
                #print("[INFO] Object found. Saving locally.")
                #Converting Gray scale image
                gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
                #Resizing 48X48 image
                roi_gray = cv2.resize(gray,(48,48))
                #Saving the image of face
                s = des_f[0]+'/'+str(currentface) + '_faces.jpg'
                cv2.imwrite(s, roi_gray)
                x =( str(currentface) + '_faces.jpg')
                #ploting the image in console
                #plt.imshow(gray, cmap=plt.get_cmap('gray'))
                #plt.show()
                currentface =currentface+1
                
#Function for linking Gui AND other function
def RunMain():
    dirt()
    Main()
    label4=Label(root,
             text='  Operation Completed !!!!!!!!!  ',
             font=('italic',20,'bold'),fg='orange').place(x=90,y=380)

#All Buttons And other things IN GUI
root.geometry("1040x480+0+0")
root.title('Select File ')
heading=Label(root,
              text='Face Recognization Data Storage Tool',
              font=('arial',25,'bold'),
              fg='steelblue').pack(side='top')
label1=Label(root,
             text='Press Browse to select Image Folder  :  ',
             font=('italic',20,'bold'),
             fg='orange').place(x=90,y=140)
b = Button(root,
           text='Browse',
           width=20,
           bg='green',
           command=lambda:OpenFolder()).place(x=300,y=180)
label2=Label(root,
             text='Press Browse to select Saving Folder  :  ',
             font=('italic',20,'bold'),fg='orange').place(x=90,y=220)
c = Button(root,
           text='Browse',
           width=20,
           bg='green',
           command=lambda:OpenFolder1()).place(x=300,y=260)
label3=Label(root,
             text='Press Run To Start The Face Extraction Operation  :  ',
             font=('italic',20,'bold'),fg='orange').place(x=90,y=300)
d = Button(root,
           text='Run',
           width=20,
           bg='green',
           command=lambda:RunMain()).place(x=300,y=340)
e=Button(root, 
         text="Quit",
         width=20,
         bg='red', 
         command=root.destroy).place(x=300,y=440)
root.mainloop()