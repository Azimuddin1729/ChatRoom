import socket
import threading 

host='localhost'
port =52000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))


server.listen()#we didnt put any number in the listen function because we want to listen to the connections infinitely
clients=[]
names=[]

def trasmit(message):
    for client in clients:
        client.send(message)

def client_msg_transfer(client):
    while True:
        try:
            message=client.recv(1024)
            trasmit(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            name=names[index]
            trasmit(f"{name} has left the chat!".encode('utf-8'))
            names.remove(name)
            break

def connection_with_client():
    while True:
        print("Server is listening...")
        client,address=server.accept()
        print(f"Connected with {str(address)}")
        client.send("NAME".encode('utf-8'))
        name=client.recv(1024)
        names.append(name)
        clients.append(client)
        print(f"Name of the client is {name}".encode('utf-8'))
        trasmit(f"{name} has joined the chat".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread=threading.Thread(target=client_msg_transfer,args=(client,))
        thread.start()

if(__name__=="__main__"):
    connection_with_client()#this is to call the function to connect with the client
 

