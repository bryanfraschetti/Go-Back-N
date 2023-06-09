import socket
import sys

## For Python 3

# Create a server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
sys.stderr.write('starting up on %s port %s' % server_address)
sock.bind(server_address)

base = 0
N = 5
expSeqNum = 0
collectedPackets = ''


# skip3 = True # lose an ack

while True:
    print("\n" + collectedPackets)
    sys.stderr.write('\nWaiting to receive message')
    
    data, address = sock.recvfrom(4096)

    sys.stderr.write('\nReceived %s bytes from %s' % (len(data), address))
    sys.stderr.write("\n" + data.decode())

    try:
        data.decode()
        if int(data.decode()) == expSeqNum:

            # #lose an ack
            # if(expSeqNum != 3 and skip3):
            #     sock.sendto(str(expSeqNum).encode(), address)
            #     print("\nSent ack " + str(expSeqNum))
            #     collectedPackets += str(expSeqNum) + " "
            #     expSeqNum += 1
            # else:
            #     skip3 = False
            #     collectedPackets += str(expSeqNum) + " "
            #     expSeqNum += 1

            sock.sendto(str(expSeqNum).encode(), address)
            print("\nSent ack " + str(expSeqNum))
            collectedPackets += str(expSeqNum) + " "
            expSeqNum += 1

        else:
            sys.stderr.write("\nReceived " + str(len(data)) + " bytes from " + str(address) + ". Discarding packet... sending ack " + str(expSeqNum-1) + ".")
            sent = sock.sendto(str(expSeqNum-1).encode(), address)
    except:
        print(data.decode())
        pass
    
    

