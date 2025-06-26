import socket 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("socket created")
    ##sender ke file me ip add receiver ka aayega hamesha
    #and receiver me receiver ka he aayega khud ka 
    ip = "192.168.1.66"
    port = 8888
    complete_add = (ip,port)
    s.bind(complete_add)        ##binding the socket

    while True:
        message , senders_address = s.recvfrom(1024)
        ##limit //size 1024 bytes

        print("Raw Message",message)
        print("Sender Address",senders_address)

        decoded_msg = message.decode("ascii")
        print("Decoded Message",decoded_msg)

except Exception as e:
    print("An error occured",e)