import socket
dec_key = input("Enter encryption key: ")

if len(dec_key)==40:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(),3213))

    message= s.recv(1000)
    message=message.decode("utf-8")
    val= dec_key[::-1]
    decripter = dict(zip(val, dec_key))

    message= "".join([decripter[words] for words in message])
    print(message)
else:
    print ("Unauthorized !! ")

