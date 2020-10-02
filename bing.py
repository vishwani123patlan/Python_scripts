from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import datetime as dt
import os
import ctypes
from ctypes import wintypes

img_url=requests.get("https://www.bing.com/")
soup=BeautifulSoup(img_url.text,'lxml')

img_box=soup.find('div',{'class':'img_cont'})

img=img_box['style'][22:-14]

#set Image  url
img_link="https://www.bing.com"+img

#download image
urllib.request.urlretrieve(img_link,'desktop.jpg')
print("Image download successfull!")



#set as desktopbackground

drive = "F:\\"
folder = "scripts"
image = "desktop.jpg"
image_path = os.path.join(drive, folder, image)
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path , 0)
print(image_path)