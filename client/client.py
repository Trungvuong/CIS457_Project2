'''
This runs the client side of our FTP Server 
we have created.

@author Trung-Vuong Pham, Ryan Eisenbarth, and Kevin Holekboer

'''
import os, socket
from ftplib import FTP

# Client object
ftp = FTP('')

# Flag for connection status
connection = False

# Starts the FTP Server connection
def start(ip, port):
        ftp.connect(ip, int(port))
        ftp.login()
        print('Connection successful!')
        connection = True
        main()

# Stores files of client and keyword in search
def localDirectory():
    ip = socket.gethostbyname(socket.gethostname())
    new_file = open("new.txt", "w")
    new_file.write(ip + "\n")
    curr = os.listdir()
    for f in curr:
        new_file.write(f + "\n")
    new_file.close()
    return
    
# Retrieves a file from the server
def retrieve(filename):
    # Open file to store retrieved data in
    try:
        retr_file = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, retr_file.write, 1024)
        retr_file.close()
        print("File Retrieved \n\n")
    except IOError:
        print("Cannot retrieve file\n\n")
    except ftplib.all_errors:
        print("Error: ftp error \n")


# Stores file in server
def store(filename):
    try:
        ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
        print('Upload successful for ' + filename)
    except IOError:
        print("File does not exist \n")
    except ftplib.error_reply:
        print("Error: reply error \n")
    except ftplib.error_temp:
        print("Error: temp error \n")
    except ftplib.error_perm:
        print("Error: perm error \n")
    except ftplib.error_proto:
        print("Error: proto error \n")

# Retrieves the file that is being searched for by the user
def search(keyword):
    file_search = open("findme.txt", "w")
    file_search.write(str(keyword))
    file_search.close()
    
    # Connects to central server
    ftp.connect('127.0.0.1', 3001)
    ftp.login()
    save_file = 'findme.txt'
    ftp.storbinary('STOR ' + save_file, open(save_file, 'rb'))
    ftp.quit()
    os.remove('findme.txt')

# The main loop that does all the program prompts
def main():
    response = input('>>> ')
    connection = False

    # Establishing FTP connection with CONNECT command
    if 'CONNECT' in response:
        argument = response.split()
        if len(argument) == 3:
            start(argument[1], argument[2])
            argument = []
            main()
        else:
            print("CONNECT needs an ip address and port number!\n")
            main()

    # Handles LIST command
    elif 'LIST' in response:
        ftp.retrlines('LIST')
        main()
    # RETRIEVE command thats retrieves the file
    elif 'RETRIEVE' in response:
        argument = response.split()
        if len(argument) == 2:
            retrieve(argument[1])
            main()
        else:
            print("RETRIEVE needs a file as argument!\n")
            main()
    # This does the STORE command to store file on server side
    elif 'STORE' in response:
        argument = response.split()
        if len(argument) == 2:
            store(argument[1])
            main()
        else:
            print("STORE needs a filename as an argument!\n")
            main()
    # Proceeds to search for file
    elif 'SEARCH' in response:
        argument = response.split()
        if len(argument) == 2:
            search(argument[1])
        main()
    # Quits the FTP Server
    elif 'QUIT' in response:
        ftp.quit()
        print('Disconnecting')
    else:
        print('The commands are CONNECT <ip address, port>, QUIT, LIST, RETRIEVE <filename>, and STORE <filename>')
        main()
if __name__ == "__main__":
    print('Welcome to the GV-Nap File Sharing System. \nThe FTP Client is ready. \nUse the CONNECT command to begin.')
    main()

