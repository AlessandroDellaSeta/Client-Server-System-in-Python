# -*- coding: utf-8 -*-

import zmq

context = zmq.Context()

#  Socket to talk to server
# print("Connecting to  server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


while(True):

	#Select operation:
	name = input("What operation? (i=insert; s=search) ")
	socket.send_string(name)
	message = socket.recv()
	message = message.decode("utf-8")
	print(message)

	if name == 's':
		name = input("")
		socket.send_string(name)
		mess = socket.recv()
		mess = mess.decode("utf-8")
		print("Received reply %s " % mess)
	elif name == 'i':
		psw = input("")
		socket.send_string(psw)
		mess = socket.recv()
		mess = mess.decode("utf-8")
		print(mess)


		if mess != "wrong password":
			name = input("")
			socket.send_string(name)
			mess = socket.recv()
			mess = mess.decode("utf-8")
			print(mess)
			lastname = input("")
			socket.send_string(lastname)
			mess = socket.recv()
			mess = mess.decode("utf-8")
			print(mess)
			id = input("")
			socket.send_string(id)
			mess = socket.recv()
			mess = mess.decode("utf-8")
			print(mess)
		else:
			continue
	else:
		print("Wrong command. ")



	inp = input("Continue? (y/n) ")
	if inp != 'y':
		break
