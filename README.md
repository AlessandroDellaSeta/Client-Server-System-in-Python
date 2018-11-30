# Client-Server-System-in-Python

INTRODUCTION:

This project aims to develop one of the most basic network programming.
In fact, it consists in creating an application for performing socket functions by implementing a Client-Server system. 
This system performs both the functions of client and server in order to promote the information sharing between them.
It allows the clients to have access to the same database at the same time, and the database will store all the information.

The main objective of this project is to create a network client that talks to a server via a socket connection and to implement
a server that listens for socket connections. 
The server is unique, it has direct access to the database and it accomplishes the task to perform operations according to 
the client requests. On the contrary, the client can be either “user” or “administrator”. If the client is a “user”,
it can only ask the server to show the information on the database. If the client is “administrator”, it can modify the
database information too. The client must know the username and the password in order to become “administrator”.

The connection protocol used for this project is a socket communication similar to TCP(Transmission Control Protocol). 

![alt text](http://www.h3c.com.hk/res/200812/31/20081231_709864_image002_624110_57_0.png)

The library used to reach this objective is ZeroMQ a faster version of TCP. ZeroMQ is an innovative library that reduce the latency to Zero.
The server wait the request from the Client, on the other hand 
the Client is ready to send all the request to the Server.

![alt text](https://github.com/imatix/zguide/raw/master/images/fig2.png)

The Database used is PostgresSQL. The library adopted is Psycopg2 since it converts automatically a PostgreSQL array data
type to a Python list. 

The System contains also a function to read from a file all the sensitive information to make the connection to the Database
private and secure. The file name is "setting.ini"

INSTRUCTION HOW TO RUN: 

The project consists of two class. Server.py and Client.py
These two class must be run separately possibly in two different  machine
to simulate an Client-Server in a Real World Scenario.
The file setting.ini contains all the information about 
database, username and password.

FUTURE WORKS:

- Make the Server able to handle multiple connection with different Clients at the same time.
- Debugging of Delete operation to remove values from the Database.
- Implement Update function to change already existing values in the  Database Table.
- Implement GUI for Client side to make the program user-friendly.


