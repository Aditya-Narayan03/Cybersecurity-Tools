from socket import *
import sys

#checks if the port is open or closed
def toConnect(trgtHost, trgtPort):

    try:
        cnct = socket(AF_INET, SOCK_STREAM)
        cnct.connect((trgtHost, trgtPort))
        print(f'[+]{trgtPort}/tcp open')

    except:
        print(f'[-]{trgtPort}/tcp closed')


#resolves IP and provide hostname, also calls for checking port status
def portScan(trgtHost, portsList):

    try:
        #gets IP of host
        trgtIP = gethostbyname(trgtHost)
        print(f'\nThe IP Address for {trgtHost} : {trgtIP}')

    except:
        print(f'Cannot resolve domain name for {trgtHost}')
        return


    try:
        #resolving hostname for the IP provided
        trgtName = gethostbyaddr(trgtIP)
        print(f'Hostname for {trgtIP} is : {trgtName[0]}')

    except:
        print(f'Error!!!')

    #setting up default timeout
    setdefaulttimeout(1)

    print('-----------------------------------')
    for ports in portsList:

        print(f'\nScanning Port : {ports}')
        toConnect(trgtHost, ports)

    print('\n-----------------------------------')


#program starts here
if __name__ == '__main__':
    trgtHost = sys.argv[1]
    portsList = [22, 80]
    portScan(trgtHost, portsList)