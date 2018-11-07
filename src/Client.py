import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to  server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


while(True):
	name = input("What is your name? ")

	print("Sending request %s …")
	socket.send_string(name)

	#  Get the reply.
	message = socket.recv()
	message = message.decode("utf-8")

	print("Received reply %s " % (message))
	inp = input("Continue? (y/n) ")
	if inp != 'y':
		break