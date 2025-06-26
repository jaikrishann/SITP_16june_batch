import socket 
try:
    ##creating sockets 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ##dgram -- datagram-- msg transfer
    ##ip add -- ipv4 address -- af inet -- address family
    print("socket created")
    ip = "192.168.1.66"
    port =     8888                         #0 - 65535
    target_add = (ip,port)
    message = input("Enter the message:-->")
    encoded_message = message.encode("ascii")
    s.sendto(encoded_message,target_add)
    print("message sent")
    s.close()
except Exception as e:
    print("An error occured",e)


    ##steps to run this project 
    #1 -- you have to connect with the same network 
    #2 -- port no same lene hai dono files me 
    #3 -- windos firewall off
    #4 -- sabse phele receiver file run karo



    ##list comphersion 
    ##file handling 
    ##generators , decorators 
    #methodoverloading and method overriding