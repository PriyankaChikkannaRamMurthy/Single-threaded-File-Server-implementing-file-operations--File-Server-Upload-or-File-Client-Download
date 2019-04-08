import os
import socket
import threading

userResponse = 0

def retrFile(name, sock):
    userResponse = sock.recv(1024)
    print (userResponse[:2])
    if userResponse[:2] == '2':
        # Get filename from the user
        filename = sock.recv(1024)
        # If the file exists and is a file
        if os.path.isfile('server/' +filename):
            sock.send("EXISTS" + str(os.path.getsize('server/'+ filename)))
            userResponse = sock.recv(1024)
            if userResponse[:2] == 'OK':
                # Assuming the user wants to read the file
                with open('server/'+ filename, 'rb') as f:
                    # Bytes to be sent
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
                    # If file size is greater than 1024 then we get more bytes to send
                    while bytesToSend != "":
                        bytesToSend = f.read(1024)
                        sock.send(bytesToSend)
        else:
            sock.send("ERROR")

    elif userResponse[:2] == '3':
        sock.sendall('OK'.encode('utf-8'))
        # Get filename from the user
        filename = sock.recv(1024)
        # If the file exists and is a file
        if os.path.isfile('server/' + filename):
            sock.send("EXISTS" +str(os.path.getsize('server/' + filename)))
            os.remove('server/' +filename)
            print("File removed successfully!")
        else:
            sock.send("ERROR")



    elif userResponse[:2] == '4':
        # Get filename from the user
        filename = sock.recv(1024)
        # If the file exists and is a file
        if os.path.isfile('server/' + filename):
            sock.send("EXISTS" + str(os.path.getsize('server/' + filename)))
            new_filename = sock.recv(1024)
            print(new_filename)
            os.rename('server/' +filename, 'server/' +new_filename)
            sock.send("SUCCESS")
            save_path = 'C:\\Priyanka\\Desktop\\Distributed\\Client-Server\\server'
            new_filetxt = new_filename
            print(new_filetxt)
            reName = os.path.join(save_path, new_filetxt)
            print("reName")
        else:
            sock.send("ERROR")

    else:
        sock.send("ERROR")


    sock.close()

def Main():
    host = '127.0.0.1'
    port = 5050

    # Creating a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))

    # Server listening for connections
    s.listen(5)
    print("Server started, waiting for client to accept request")
    while True:
        # Get the connection socket
        c, addr = s.accept()
        print ("Client connected to ip:<", str(addr), ">")
        t = threading.Thread(target=retrFile, args=("retrThread", c))
        # Starting thread
        t.start()

    s.close()

if __name__ == '__main__':
    Main()