# Single-threaded-File-Server-to-implement-file-operations-[File-Server-Upload-File-Download-Client] 

Program Implementation:

Chose the message oriented client-server communication for our project.
For the server side, the following steps were followed in the program to establish connection with client

1) The socket module is imported
2) A port is reserved for the file transfer
3) A socket object is created
4) Use the local machine host and port to bind
5) Listen to client for connection request
6) Once client requests accept the request and service the client by sending and receiving data

For UPDATE, DOWNLOAD, DELETE and RENAME functions, on receiving the request from the client, the server performs the corresponding action and responds back to the client the Success or Error message.

For the client side,
1) The socket module is imported
2) A port is reserved for the file transfer
3) A socket object is created
4) Use the host and port of server to connect with the server machine
5) Once server accepts the request, can ask for service from the server sending and receiving data
For performing functions, the client sends request to server and waits for positive or negative response from the server.
Note: If connection established on different systems, turn off the firewall, and both client as well as server needs to be connected on the same network for single threaded server client communication

Issues Encountered:

1) Code compatibility issues, such different Interpreter versions for Python (2.7 vs 3.5)
2) Version control of code
3) Understanding the functionality of sockets
4) Usage of single threaded server

Learning outcomes:

1. Understanding of client server model.
2. Understanding of message oriented communication between client and server
3. Socket programming
4. Understanding of version control tools
6. Importance of locking
