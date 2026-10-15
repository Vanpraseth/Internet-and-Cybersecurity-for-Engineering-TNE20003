import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 2107)
    messages = ["TNE20003:Hello, Server!", "TNE20003:Testing Message"]
    
    for msg in messages:
        print(f"Sending: {msg}")
        client_socket.sendto(msg.encode(), server_address)
    
        data, _ = client_socket.recvfrom(1024)
        print(f"Received: {data.decode()}")

    client_socket.close()

udp_client()
