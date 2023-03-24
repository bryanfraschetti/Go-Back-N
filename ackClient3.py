import socket
import sys
#import pickle

## For Python 3

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)

base = 0
N = 5
nxtSeqNum = 0
message = ['0','1','2','3','4','5','6','7','8','9']
ackNum = 0

skip4 = True #drop packet 4 on first transmission
# skip8 = False #drop packet 8 during retransmission
# skip0 = True #drop the first packet

try:
	while(base < len(message)):
		while nxtSeqNum <= base + N - 1:
			if(nxtSeqNum < len(message)):
				sys.stderr.write('\nsending "%s"' % message[nxtSeqNum])

				# if(nxtSeqNum == 4 and skip4):
				# 	nxtSeqNum = nxtSeqNum + 1
				# 	skip4 = False
				# 	continue
				
				# if(nxtSeqNum == 4 and not skip4):
				# 	skip8 = True

				# if(nxtSeqNum == 8 and skip8 and not skip4):
				# 	nxtSeqNum = nxtSeqNum + 1
				# 	skip8 = False
				# 	continue
				
				# if(nxtSeqNum == 0 and skip0):
				# 	nxtSeqNum = nxtSeqNum + 1
				# 	skip0 = False
				# 	continue
				

				sock.sendto(message[nxtSeqNum].encode(), server_address)
				nxtSeqNum +=1
			else:
				break

		sys.stderr.write('\nwaiting to receive ack')
				
		sock.settimeout(1)
		while(ackNum <= base + N - 1):
			try:
				ackNum, server = sock.recvfrom(4096)
				ackNum = int(ackNum.decode())
				print("\nReceived Ack " + str(ackNum))
				
			except:
				nxtSeqNum = ackNum + 1
				break

		base = ackNum + 1

finally:
	sys.stderr.write('\nclosing socket')



sock.close()

