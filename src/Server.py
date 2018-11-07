import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
database = {"name" : ["Alessandro", "Jack"],
            "last name" : ["Della Seta", "Black" ],
            "ID" : ["10429777","21223933"]}

def search(dict, value):
    for k in dict:
        count = 0
        for v in dict[k]:
            if value in v:
                return [dict['name'][count],dict['last name'][count],dict['ID'][count]]
            count += 1

    return None

while True:
    #  Wait for next request from client
    message = socket.recv()
    message = message.decode("utf-8")
    print("Received request: %s" % message)

    #  Do some 'work'
    answer = search(database,message)
    sent = str(answer)
    # Send reply back to client
    socket.send_string(sent)