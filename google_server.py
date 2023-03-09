import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to Google server
sock.connect(("www.google.com", 80))

# Send malicious data
sock.send("GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# Receive response
response = sock.recv(4096)

# Print response
print(response)