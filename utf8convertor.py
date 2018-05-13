import os
import time
import codecs

from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.directory =  filedialog.askdirectory(initialdir = "/home/ilyas/Downloads/",title = "Select Directory")

def edit(src):
	if os.path.isfile(src):
		doc = codecs.open(src, 'r', 'windows-1254')
		docContent = doc.read()
		doc.close()
		os.remove(src)
		newDoc = open(src, 'w')
		newDoc.write(docContent)
		newDoc.close()
		print('Edited: ', src)
	else:
		for dir in os.listdir(src):
			print(src + '/' + dir)
			edit(src + '/' + dir)

edit(root.directory)
