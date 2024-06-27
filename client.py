import socket
import threading 

name=input("Enter your name: ")

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('localhost',52000))



def msg_send_to_server():
    while True:
        message=f"{name}: {input()}"
        client.send(message.encode('utf-8'))
        

def obtained_msg_from_server():
    while True:
        try:
            message=client.recv(1024).decode('utf-8')
            if message=='NAME':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break



obtained_thread=threading.Thread(target=obtained_msg_from_server)
obtained_thread.start()

send_thread=threading.Thread(target=msg_send_to_server)
send_thread.start()



