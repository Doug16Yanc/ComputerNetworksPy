import socket
import sys

SERVER_PORT = 8000 
BUFFER = 1024

def connecting():
    value_ip = input("Enter the ip address to start the communication")
    confirmation = input(f"\nThe destination is : {value_ip}, is that correct?\n" + 
                         " 0 - No\n 1 - Ok\n")
    
    confirmation = False if int(confirmation) == 0 else True

    if confirmation is False:
        print("Exiting the program...\n") 
        sys.exit()
    
    return start_connection(value_ip)

def checking_ip_address(ip_address):
    if len(ip_address) == 9 and ip_address is not None:
        return True
    print("Ending the program...Check if the ip address is correct, please!")
    sys.exit()

def start_connection(ip_address):

    print("Trying to connect to the server")
    checking_ip_address(ip_address)
    tcp_connection = socket.socket(socket.AF_INET,
                               socket.SOCK_STREAM)

    
    try:
        destiny = (ip_address, SERVER_PORT) 
        tcp_connection.connect(destiny)
    except ConnectionError as err:
        print(f"Connection refused. Please, try again!\n Type of error : {type(err)}.\n")

    return tcp_connection

def close_connection(tcp_connection):
    print("Ending tcp connection.")
    tcp_connection.close()

def conversation(tcp_connection):
    print("Starting the chat to computer networks. To exit the conversation press: exit.")

    while True:

        message = input("You : ")

        if message is not None:
            tcp_connection.send(bytes(message, "utf8"))
            if message == "exit":
                break
        recv_message = tcp_connection.recv(BUFFER).decode("ascii") 

        if recv_message is not None:
            print(f"Server message: {recv_message}") 
        if recv_message == 'exit':
            print("The server side just end the connection. Inform exit to end the connection.\n")

    print("Exiting...\n")     
    close_connection(tcp_connection)
    
def main():
    connection = connecting()
    conversation(connection)

    try:
        connection.close()
    except:
        print("The TCP connection is end.\n")

if __name__ == "__main__":
    main()