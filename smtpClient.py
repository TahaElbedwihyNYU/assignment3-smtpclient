from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.    
    # Fill in start
    mailFrom = "MAIL FROM:<te2215@nyu.edu>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTO = "RCPT TO:<te2215@nyu.edu>\r\n"
    clientSocket.send(rcptTO.encode())
    recv3 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send message data.
    message = "Subject: This is URGENT!\r\n" \
              "I am writing to you to speak on your car's extended warranty.\r\n" \
              ".\r\n"  # Ending with a dot
    if recv4[:3] == "354":
        clientSocket.send(message.encode())

    recv5 = clientSocket.recv(1024).decode()

    # Fill in start
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit = "QUIT"
    if message[-3] == ".":
        clientSocket.send(quit.encode())
        clientSocket.close()

    # recv6 = clientSocket.recv(1024).decode()
    # # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')