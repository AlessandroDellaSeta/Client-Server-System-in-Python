# Client-Server-System-in-Python
This project aims to develop one of the most basic network programming. In fact, it consists in creating an application for performing socket functions by implementing a Client-Server system. This system performs both the functions of client and server in order to promote the information sharing between them. It allows the clients to have access to the same database at the same time, and the database will store all the information.

The main objective of this project is to create a network client that talks to a server via a socket connection and to implement a server that listens for socket connections. The server is unique, it has direct access to the database and it accomplishes the task to perform operations according to the client requests. On the contrary, the client can be either “user” or “administrator”. If the client is a “user”, it can only ask the server to show the information on the database. If the client is “administrator”, it can modify the database information too. The client must know the username and the password in order to become “administrator”.

INSTRUCTION: 
The project consist of two class. Server.py and Client.py
These two class must be run separately.
The file setting.ini contains all the information about 
database, username and password.