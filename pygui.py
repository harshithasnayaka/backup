# here we write py code for server only
# Import Module
from tkinter import *
import socket
import tqdm
import os

def server():

	# device's IP address
	SERVER_HOST = "0.0.0.0"
	SERVER_PORT = 5001
	# receive 4096 bytes each time
	BUFFER_SIZE = 4096
	SEPARATOR = "<SEPARATOR>"

	# create the server socket
	# TCP socket
	s = socket.socket()
	# bind the socket to our local address
	s.bind((SERVER_HOST, SERVER_PORT))
	# enabling our server to accept connections
	# 5 here is the number of unaccepted connections that
	# the system will allow before refusing new connections
	s.listen(5)
	print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
	# accept connection if there is any
	client_socket, address = s.accept() 
	# if below code is executed, that means the sender is connected
	print(f"[+] {address} is connected.")
	# receive the file info
	# receive using client socket, not server socket
	received = client_socket.recv(BUFFER_SIZE).decode()
	filename, filesize = received.split(SEPARATOR)
	# remove absolute path if there is
	filename = os.path.basename(filename)
	# convert to integer
	filesize = int(filesize)
	# start receiving the file from the socket
	# and writing to the file stream
	progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
	with open(filename, "wb") as f:
		while True:
			bytes_read = client_socket.recv(BUFFER_SIZE)
			if not bytes_read:    
				break
			f.write(bytes_read)
			progress.update(len(bytes_read))
	client_socket.close()
# close the server socket
	s.close()
	return "server"


def gui():
# create root window
	root = Tk()

# root window title and dimension
	root.title("server")
# Set geometry(widthxheight)
	root.geometry('350x200')

# adding a label to the root window
	lbl = Label(root, text = "receive file")
	lbl.grid()

# function to display text when
# button is clicked
	def clicked():
		lbl.configure(text = "file received")

# button widget with red color text
# inside
	btn = Button(root, text = "Click" ,
			fg = "red", command=clicked)
# set Button grid
	btn.grid(column=1, row=0)

# Execute Tkinter
	root.mainloop()
	return "gui"
def default():
	return "error"
		

#def server1(i):
	switcher = {
		0:server,
		1:gui
}
	func = switcher.get(i,lambda:"server")
	print(func())


# Function to convert number into string
# Switcher is dictionary data type here
def one(argument):
	switcher = {
		0: 'server',
		1: 'gui'
		
	}

	# get() method of dictionary data type returns
	# value of passed argument if it is present
	# in dictionary otherwise second argument will
	# be assigned as default value of passed argument
	return switcher.get(argument, 'gui')

# Driver program
if __name__ == "__main__":
	argument=1
	print (one(argument))
