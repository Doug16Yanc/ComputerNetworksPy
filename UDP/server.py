import socket 
import sys

SERVER_IP = ''
SERVER_PORT = 5000
BUFFER = 1024

def bind_to_the_server():
    udp_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_server = (SERVER_IP, SERVER_PORT)
    udp_connection.bind(socket_server)
    return udp_connection

def close_connection(udp_connection):
    print("Closing the connection and exiting the program.\n")
    udp_connection.close()

def listening(udp_connection):
    print("Starting the chat. Waiting for a message.\n")
    while True:
        recv_message, client_address = udp_connection.recvfrom(BUFFER)
        if recv_message.decode("ascii") != "exit":
            print(f"\nCliente {client_address[0]} : {recv_message.decode('ascii')}")
            if recv_message.decode("ascii") == "exit":
                print("The server side just end the connection. Inform exit to end the connection.\n")
                break
        sending_message = input("You : ")
        if sending_message != "":
            udp_connection.sendto(bytes(sending_message, "utf-8"), client_address)
            if sending_message == "exit":
                break
    close_connection(udp_connection)


def main():    
    current_connection = bind_to_the_server()
    listening(current_connection)

    sys.exit()

if __name__ == "__main__":
    main()