import psycopg2 as psycopg2
import zmq
import os


# function to read private infromation from setting.ini
def readFile(key):
    separator = "="
    try:
        script_dir = os.path.dirname(__file__)  # absolute dir
        rel_path = "../setting.ini"
        abs_file_path = os.path.join(script_dir, rel_path)  # absolute path

        with open(abs_file_path) as f:

            for line in f:
                if separator in line:
                    # Find the name and value by splitting the string
                    name, val = line.split(separator, 1)

                    if name.strip() == key:
                        return val
        return 0
    except:
        print("cannot open file")

#function to check if the user is an Admin
def admincheck(user, password):
    psw = readFile("password").strip()
    usr = readFile("username").strip()
    if password == psw and user == usr:
        print("Valid Admin")
        return True
    print("Wrong user or psw")
    return False

#function to search Employee in the database
def search(conn, cursor, value):
    temp = value.upper()

    val = "'" + '%' + temp + '%' + "'"
    query = (""" SELECT * FROM "Employee" WHERE "Name" LIKE """ + val +
             """ OR "Last name" LIKE  """ + val +
             """ OR "SSN" LIKE  """ + val +
             """ OR "Job" LIKE """ + val)
    cursor.execute(query)

    # retrieve the records from the database
    records = cursor.fetchall()
    print(records)
    if len(records) == 0:
        return "NOT FOUND"
    return records

#function to isert new Employee in the database
def insert(conn, cursor, name, lastname, SSN, job, pay):
    salary = "$" + pay
    query = ("""INSERT INTO "Employee" ("Name", "Last name", "SSN", "Job", "Salary") VALUES (%s, %s, %s, %s, %s)""")
    data = (name, lastname, SSN, job, salary)
    cursor.execute(query, data)
    conn.commit()
    return True

#TODO class still NOT WORKING
def delete(conn, cursor, id):
    val = "'" + '%' + id + '%' + "'"

    query = ("""DELETE FROM "Employee" WHERE "SSN" = """ + val)
    cursor.execute(query, id)
    conn.commit()
    print(cursor.rowcount, "record(s) deleted")

#function for standard communication with client
def communication():
    message = socket.recv()
    message = message.decode("utf-8")
    return message


def connected(socket):
    admin = False #the admin valus is set as standard to False
    count = 0
    #fist communication handshake with the Clients
    greating = communication()
    print(greating)

    #check if the user is an Admin
    socket.send_string("Are you admin y/n")
    message = communication()

    while message == 'y':
        socket.send_string("Please insert Username: ")
        user = communication()

        socket.send_string("Please insert Password: ")
        psw = communication()

        check = admincheck(user, psw)
        print(admin)
        if check:
            admin = True
            break
        else:
            if count < 3:
                count += 1
                socket.send_string("Wrong psw, try again y/n ")
                message = communication()
            else:
                socket.send.string("Too many tries!! Press Enter to continue")
                communication()
                break
    database = readFile("database")

    while True:
        try:

            conn = psycopg2.connect(database)

        except:
            print("IMPOSSIBLE to connect to the database")
            break

        # Define a cursor for database
        cursor = conn.cursor()

        socket.send_string("What operation do you want to perform? (i=insert; s=search; d=delete) "
                           "\n NOTE: only admin can INSERT or DELETE ")
        message = communication()
        mes = message.lower()

        if mes == "s":
            socket.send_string("Who are you looking for? ")
            message = communication()
            try:
                answer = search(conn, cursor, message)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                answer = error

        elif mes == 'i':

            if admin:
                socket.send_string("Please insert name: ")
                nm = communication()
                name = nm.upper()

                socket.send_string("Please insert last name: ")
                ltnm = communication()
                lastname = ltnm.upper()

                socket.send_string("Please insert SSN: ")
                idi = communication()
                SSN = idi.upper()

                socket.send_string("Please insert job: ")
                j = communication()
                job = j.upper()

                socket.send_string("Please insert salary: ")
                pay = communication()
                salary = pay.upper()

                try:
                    ins = insert(conn, cursor, name, lastname, SSN, job, salary)
                    answer = "\033[1;32;40m New Employee inserted correctly \x1b[0m"
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                    answer = error
            else:
                answer = "\033[1;31;40m Permission denied \x1b[0m"
        elif mes == "d":
            if admin:
                socket.send_string("Please insert SSN employee you want delete: ")
                delete = communication()
                try:
                    print(delete)
                    delete(conn, cursor, delete)
                    answer = "Employee deleted. "
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                    answer = "\033[1;31;40m Impossible delete employee account, please check SSN and try again.\x1b[0m"
            else:
                answer = "\033[1;31;40m Permission denied \x1b[0m"
        else:
            answer = "\033[1;31;40mWrong command.\x1b[0m "

        send = str(answer)
        # Send reply back to client and ask him if want to perform other action
        socket.send_string(send + '\n' + "Do you want continue y/n: ")
        mess = communication()

        if mess == 'y':
            continue
        else:
            socket.send_string("close")
            socket.close()


#  Wait for next connection request from client
if __name__ == "__main__":
    readFile("admin")

    while True:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5555")
        try:
            connected(socket)
        except:
            continue
