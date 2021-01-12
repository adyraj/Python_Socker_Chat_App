import socket
import os
import threading

os.system('tput setaf 2')
os.system('figlet -c Chat App')
os.system('tput setaf 3')

# IP Address and Port Number
server_ip = "192.168.43.86"
server_port = 1234

client_ip = input("Enter Host IP to Chat: ")
print()
client_port = 1234


# Network Address Family: IPv4
add_family = socket.AF_INET

# UDP protocol
protocol = socket.SOCK_DGRAM

s = socket.socket( add_family, protocol )
s.bind(( server_ip, server_port )) 

os.system("tput setaf 1")
print("Send Msg\t\t\t\t\t\t\tReceived Msg")


def send_data():
    while True:
        #Send data to Host
        os.system("tput setaf 5")
        data = input().encode()
        s.sendto(data, ( client_ip, client_port ))

        if data.decode() == 'Bye' or data.decode() == 'bye':
            os.system('tput setaf 2')
            os.system('figlet -c Thank You !!')
            os.system('tput setaf 3')
            os.system("tput setaf 9")
            os._exit(1)

def receive_data():
    while True:
        # Receive data from network
        x = s.recvfrom(1024)
        data = x[0].decode()
        clientip = x[1][0]

        os.system("tput setaf 6")
        print("\t\t\t\t\t\t\t\t" + data)
        os.system("tput setaf 5")

        if data == 'Bye' or data  == 'bye':
            os.system('tput setaf 2')
            os.system('figlet -c Thank You !!')
            os.system("tput setaf 9")
            os._exit(1)

# Craete two thread
t1 = threading.Thread( target = send_data )
t2 = threading.Thread( target = receive_data )

# Start the thread
t1.start()
t2.start()
