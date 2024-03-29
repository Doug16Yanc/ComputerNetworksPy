import socket 
import sys

SERVER_IP = ''
SERVER_PORT = 8000
BUFFER = 1024

def bind_to_the_server():

    tcp_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server = (SERVER_IP, SERVER_PORT)
    tcp_connection.bind(socket_server)
    tcp_connection.listen(1)

    return tcp_connection

def client_confirmation(tcp_connection):
    connection, ip_client = tcp_connection.accept()
    print(f"\nThe client with {ip_client[0]} ip has connected.\n")
    return connection, ip_client


def close_connection(tcp_connection):

    print("Closing the connection and exiting the program.\n")

    tcp_connection.close()

def listening(connection, ip_client):
    print("Starting the chat. Waiting for a message.\n")
    while True:
        recv_message = connection.recv(BUFFER).decode("ascii")

        if recv_message is not None and recv_message != "exit":
            print(f"\nCliente {ip_client[0]} : {recv_message}")

            if recv_message == "exit":
                print("The server side just end the connection. Inform exit to end the connection.\n")
                break

        sending_message = input("You : ")

        if sending_message is not None:
            connection.send(bytes(sending_message, "utf-8"))

            if sending_message == "exit":
                break

    close_connection(connection)



def main():    
    current_connection = bind_to_the_server()
    accept_connection, client = client_confirmation(current_connection)
    listening(accept_connection, client)

    sys.exit()

if __name__ == "__main__":
    main()