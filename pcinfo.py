import os
try:
	import platform
	import tkinter
	from tkinter import *
	import tkinter as tk
	from tkinter import messagebox
	import urllib, json
	from requests import get
	import urllib.request
	import socket
	import os.path
except:
	os.system('pip install requests')
	os.system('python pcinfo.py')
try:

	#--------------------------

	if os.path.exists('log.txt'):
		pass
	else:
		f= open("log.txt","w+")
		f.close()
		pass

	log_file = open('log.txt', 'r+')
	log_file.truncate()
	#list all platform variables
	try:	
		external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
	except:
		pass
	
	#--------------------
	#define buttons
	#---------------------
	
	log_file.write(platform.system()+('\n'))
	log_file.write(platform.platform()+('\n'))
	log_file.write(platform.machine()+('\n'))
	
	log_file.write(platform.node()+('\n'))
	log_file.write(platform.processor()+('\n'))
	log_file.write(os.getcwd()+'\n')
	log_file.write('private IP: '+ socket.gethostbyname(socket.gethostname())+'\n')
	try:
		log_file.write('public IP: '+ (str(external_ip)))
		
	except:
		pass




	

	

	



	log_file.close()

except:

	root = tk.Tk()

	root.after(1500, root.destroy)
	l = Label(root, text='ERROR', fg='red', font='verdena 100')
	l.pack()

	root.mainloop()

