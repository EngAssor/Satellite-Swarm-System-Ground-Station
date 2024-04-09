import socket
#import schedule
import time

command = ''


def Swarm_from_base_to_swarm():
    print('Waiting For Ground Station Connection to be Established... ')
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect(('192.168.1.8', port))  # connect to the server
    print("Connection from Ground Station is Established Successfully ✔ ")
    print('Sending The Beacon...')
    Swarm_Beacon = 'The Swarm Satellite Beacon'  # take input
    client_socket.send(Swarm_Beacon.encode())
    print('The Beacon is Sent Successfully ✔ ')
    global command

    while command != 'close':
        print('Waiting For Ground Station Command...')
        command = client_socket.recv(1024).decode()
        print('Received Command From Ground Station : ' + command)
        ack = command[0:33]
        ack = ack + '11111111'
        print('Sending The Swarm Satellite Acknowledge... ')
        #client_socket.send(f'The Swarm Acknowledge : {ack}'.encode())
        print('The Swarm Satellite Acknowledge Sent Successfully ✔')
        print('Establishing Connection With Satellite...')
        client_socket.send("data".encode())
       # Data_Recevied_From_Satellite = Swarm_from_swarm_to_sat()
        #print('Sending Data To Ground Station...')
        #if command[33:41] == '00001001':
         #   client_socket.send(Data_Recevied_From_Satellite)
        #else:
         #   client_socket.send(Data_Recevied_From_Satellite.encode())
        #print('Data Sent Successfully ✔')

    client_socket.close()  # close the connection





def Swarm_from_swarm_to_sat():
    # get the hostname
    host = socket.gethostname()
    port = 6000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind(('', port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection From Satellite is Established At : " + str(address))
    Satellite_Beacon = conn.recv(1024).decode()
    print('Recevied Beacon From Swarm Satellite : ' + Satellite_Beacon)
    # while True:

    # x = GUI()
    # receive data stream. it won't accept data packet greater than 1024 bytes
    print('Sending The Ground Station Command...')
    conn.send(command.encode())  # send data to the client
    print(f'Ground Station Command {command} Sent Successfully ✔')
    print('Waiting For Satellite Acknowledge...')
    Satellite_Acknowledge = conn.recv(1024).decode()
    print('Received Acknowledge From Satellite : ' + Satellite_Acknowledge)
    print('Waiting For Data From Satellite...')
    if command[33:41] == '00001001':
        Satellite_Data_Response = conn.recv(1073741824)
    else:
        Satellite_Data_Response = conn.recv(1073741824).decode()
    print('Data Recevied Successfully ✔')
    return Satellite_Data_Response

    conn.close()  # close the connection


if __name__ == '__main__':
    Swarm_from_base_to_swarm()