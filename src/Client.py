import getpass
import zmq

# function for communication between client and the server
def communication(name):
    socket.send_string(name)
    message = socket.recv()
    message = message.decode("utf-8") #decode the char format from Server
    return message


if __name__ == "__main__":

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # first message handshake with the Server
    operation = input("Press Start to begin...")
    message = communication(operation)
    print(message)

    try:
        while (True):
            if message == "Please insert password: ":  # iff the server ask a password the client uses the hidden input mode
                operation = getpass.getpass()
            else:
                operation = input("")

            message = communication(operation)

            if message == "close":  # iff the server communicate that the connection is closed the client stops
                socket.close()
                print("Connection closed")
                break
            else:
                print(message)

    except:
        print("Impossible communicate with the Server. ")
