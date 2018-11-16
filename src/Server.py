import psycopg2 as psycopg2
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def admincheck():
    pass

def search(conn , cursor, value):
    # execute  Query
    temp =  value.upper()

    val ="'" + '%'+temp+'%' + "'"
    cursor.execute(""" SELECT * FROM "Employers" WHERE "Name" LIKE """ + val +
                   """ OR "Last name" LIKE  """ + val +
                   """ OR "ID" LIKE  """ + val)

    # retrieve the records from the database
    records = cursor.fetchall()
    print (records)
    if len(records)==0:
        return "NOT FOUND"
    return records

def insert(conn , cursor, name, lastname, id):
    query = ("""INSERT INTO public."Employers" ("Name", "Last name", "ID") VALUES (%s, %s, %s)""")
    data = (name,lastname,id)
    cursor.execute(query,data)
    conn.commit()


while True:
    #  Wait for next request from client
    try:
        conn = psycopg2.connect("dbname=postgres user=postgres password=gaara host=127.0.0.1")
    except:
        print ("IMPOSSIBLE to connect to the database")

    #Define a cursor for database
    cursor = conn.cursor()

    message = socket.recv()
    message = message.decode("utf-8")
    print("Received request: %s" % message)
    mes = message.lower()
    if mes == "s":
        socket.send_string("Who are you looking for? ")
        message = socket.recv()
        message = message.decode("utf-8")
        answer = search(conn,cursor,message)
    elif mes == 'i':
        socket.send_string("Please insert password: ")
        psw = socket.recv()
        psw = psw.decode("utf-8")

        if psw == "ciao":
            socket.send_string("Please insert name: ")
            nm = socket.recv()
            nm = nm.decode("utf-8")
            name = nm.upper()

            socket.send_string("Please insert last name: ")
            ltnm = socket.recv()
            ltnm = ltnm.decode("utf-8")
            lastname = ltnm.upper()

            socket.send_string("Please insert id: ")
            idi = socket.recv()
            idi = idi.decode("utf-8")
            id = idi.upper()

            insert(conn, cursor, name, lastname, id)
            answer = "employer insert correctly"
        else:
            print("wrong psw")
            answer = "wrong password"

    else:
        answer = ""
    print('sent')
    sent = str(answer)
    # Send reply back to client
    socket.send_string(sent)