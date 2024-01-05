import socket
import http.client

#create a socket
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connection to the server address and a port on the server
client_socket.connect(('127.0.0.2', 8000))
print("Successful connection to server")

#create an HTTPconnection using the socket object
connection=http.client.HTTPConnection('127.0.0.2', 8000)

#send a GET request to the server
connection.request('GET', '/')

#GET response from the server
response=connection.getresponse()

#print status code and the reason phrase
print(response.status, response.reason)

#print the response headers
print(response.getheaders())

#print the response body
print(response.read())

#close the connection
connection.close()
