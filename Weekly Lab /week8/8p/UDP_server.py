import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_address = ('localhost', 2107)
    server_socket.bind(server_address)
    
    print("Server is listening on port 2107...")
    
    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        
        print(f"Received message: {message} from {client_address}")

        if message.startswith("TNE20003:"):
            user_message = message[len("TNE20003:"):]
            response = f"TNE20003:A:{user_message}"
        else:
            response = "TNE20003:E:Invalid message format"

        server_socket.sendto(response.encode(), client_address)

udp_server()
