import os
import time
import codecs

from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.directory =  filedialog.askdirectory(initialdir = "./",title = "Select Directory")

i = 0

def edit(src):
	global i
	if os.path.isfile(src):
		doc = open(src, encoding='utf-8')
		docContent = ""
		try:
			docContent = doc.read()
			os.remove(src)
			newDoc = open(src, 'w')
			newDoc.write(docContent)
			newDoc.close()
			print('Edited: ', src)
		except: 
			doc.close()
			doc = open(src, encoding='windows-1254') 
			try:
				docContent = doc.read()
				os.remove(src)
				newDoc = open(src, 'w')
				newDoc.write(docContent)
				newDoc.close()
				print('Edited: ', src)
			except: 
				doc.close()
				doc = open(src, encoding='windows-1252')
				try:
					docContent = doc.read()
					os.remove(src)
					newDoc = open(src, 'w')
					newDoc.write(docContent)
					newDoc.close()
					print('Edited: ', src)
				except: 
					i += 1
					os.system('tput setaf 1; echo "\nFile path : ' + src + '"; echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! File can\'t read !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"; tput sgr0;')
	else:
		for dir in os.listdir(src):
			print(src + '/' + dir)
			edit(src + '/' + dir)


edit(root.directory)
os.system('tput setaf 1; echo ' + str(i) + '" File can\'t read!"')
