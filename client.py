import ftplib


# Start of client FTP Server connection
def start():
    server_name=input("Please enter the server name:\n")
    port_num=input("Please enter the port number:\n")
    return server_name, port_num


# Makes the client connection to server
def make_client(ip, port):
    ftp = ftplib.FTP('')
    ftp.connect(ip, int(port))
    ftp.login()
    return ftp


# Lists the directories in server
def filelist(ftp):
    print("List files in directory: ")
    print(ftp.retrlines('List'))
    print("\n\n")


# Retrieves a file from the server
def retrieve(ftp):
    filename= input("Enter filename you want to retrieve:\n")
    # create file to store retrieved data in
    try:
        localfile = open(filename, 'wb')
        ftp.retrbinary('RETR '+filename, localfile.write, 1024)
        localfile.close()
        print("File Retrieved \n\n")
    except IOError:
        print("Cannot retrieve file\n\n")
    except ftplib.all_errors:
        print("Error: ftp error \n")


# Stores file in server
def store(ftp):
    filename=input("Enter filename you want to store:\n")
    try:
        ftp.storbinary("STOR "+ filename, open(filename, 'r'))
    except IOError:
        print("File does not exist \n")
    except ftplib.all_errors:
        print("Error: ftp error \n")


# End client connection to server
def quit(ftp):
    print("quit")
    ftp.quit()


def main():
    ftp_connection=None
    while ftp_connection is None:
        server_name, port_num = start()
        try:
            ftp_connection = make_client(server_name, port_num)
        except ftplib.all_errors:
            print("Could not connect to server, try again\n")
            ftp_connection = None

    command = None
    while command != "quit":
        command = input("Enter Command: LIST, RETRIEVE, STORE, QUIT: ")
        if command.lower() == "list":
            filelist(ftp_connection)
        elif command.lower() == "retrieve":
            retrieve(ftp_connection)
        elif command.lower() == "store":
            store(ftp_connection)
        elif command.lower() == "quit":
            quit(ftp_connection)
            command = "quit"
        else:
            print("Invalid command, please try again\n\n")


if __name__ == "__main__":
    main()

