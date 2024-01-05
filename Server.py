import socket
import http.server
import threading

#initialize a socket object, specifying address family and protocol
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#name the socket aka bind the socket to a host machine address and a port on the machine
server_socket.bind(('', 8000))

#Listening for incoming connections,  providing value for backlog
server_socket.listen(4)

#Define Handler to handle the requests
class ServerHandler(http.server.BaseHTTPRequestHandler):
        #Override the do_GET to handle GET requests
        def do_GET(self):

                #Send a 200 OK response
                self.send_response(200)

                #Send response headers
                self.send_header('content-type', 'text/html')
                self.end_headers()

                #Write the response body
                self.wfile.write("<html><body><h1>Responding from MARS, Hello Earth</h1></body></html>")

#Define a function for handling each connection
def handle_connection(client_socket, client_address):

        #create a handler object using the client socket
        handler=ServerHandler(client_socket, client_address, server_socket)

        #Handle request and response
        handler.handle()

        #close connection



#Use loop to accept connections from clients
        #Accept a connection from a client
try:
        while True:
                client_socket, client_address= server_socket.accept()
                print("Connection established with ", client_address)
                #Create a new thread to handle the connection
                thread =threading.Thread(target=handle_connection, args=(client_socket, client_address))
                thread.start()
except:
        print("Error in connection")


