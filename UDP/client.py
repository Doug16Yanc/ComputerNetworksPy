import socket
import sys

SERVER_PORT = 5000
BUFFER = 1024

def connecting():
    value_ip = input("Enter the IP address to start the communication: ")
    confirmation = input(f"\nThe destination is: {value_ip}, is that correct?\n" + 
                         "0 - No\n1 - Ok\n")
    
    confirmation = False if int(confirmation) == 0 else True

    if not confirmation:
        print("Exiting the program...\n") 
        sys.exit()
    
    return start_connection(value_ip)

def checking_ip_address(ip_address):
    if len(ip_address.split('.')) == 4:
        return True
    print("Ending the program...Check if the IP address is correct, please!")
    sys.exit()

def start_connection(ip_address):
    print("Trying to connect to the server")
    checking_ip_address(ip_address)
    udp_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return udp_connection

def close_connection(udp_connection):
    print("Ending UDP connection.")
    udp_connection.close()

def conversation(udp_connection):
    print("Starting the chat for computer networks. To exit the conversation, press: exit.")

    while True:
        message = input("You: ")

        if message.strip():
            udp_connection.sendto(bytes(message, "utf-8"))
            if message == "exit":
                break

        recv_message, addr = udp_connection.recvfrom(BUFFER)

        if recv_message:
            decoded_message = recv_message.decode('utf-8')
            if decoded_message == 'exit':
                print("The server side just ended the connection. Enter 'exit' to end the connection.\n")
                break
            print(f"Server message: {decoded_message}") 

    print("Exiting...\n")     
    close_connection(udp_connection)
    
def main():
    connection = connecting()
    conversation(connection)

if __name__ == "__main__":
    main()
