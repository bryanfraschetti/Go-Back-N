import socket
import sys
#import pickle

## For Python 3

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)

base = 0
N = 2
nxtSeqNum = 0
message = ['0','1','2','3','4','5','6','7','8','9']
ackNum = 0

try:
	while(base < len(message) - 1):
		while nxtSeqNum <= base + N - 1:
			sys.stderr.write('sending "%s"' % message[nxtSeqNum])
			sock.sendto(message[nxtSeqNum].encode(), server_address)
			nxtSeqNum +=1

		sys.stderr.write('\nwaiting to receive ack')
		
		while (ackNum<base + N - 1):
			ackNum, server = sock.recvfrom(4096)
			ackNum = int(ackNum.decode())
			sys.stderr.write('\nReceived ack ' + str(ackNum))

		base = ackNum
	



finally:
	sys.stderr.write('\nclosing socket')
		
	

sock.close()

