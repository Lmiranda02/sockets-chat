# imports
import socket
import threading


class ChatServer:
    clients_list = []
    clients_artifacts = {}
    last_received_message = ""

    def __init__(self):
        self.server_socket = None
        self.create_listening_server()

    def create_listening_server(self):

        self.server_socket = socket.socket(socket.AF_INET,
                                           socket.SOCK_STREAM)
        local_ip = '127.0.0.1'
        local_port = 10319
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((local_ip, local_port))
        print("Listening for incoming messages..")
        self.server_socket.listen(5)
        self.receive_messages_in_a_new_thread()

    def receive_messages(self, so):
        client_address = so.getpeername()
        while True:
            incoming_buffer = so.recv(1024).decode('utf-8')
            if not incoming_buffer:
                socket, (ip, port) = so.getpeername()
                print(f'[SERVER] Cliente {ip}:{port} desconectado.')
                self.broadcast_to_all_clients(so, f'[SERVER] Cliente {ip}:{port} desconectado.')
                self.remove_client_artifacts((ip, port))  # Eliminar artefactos del cliente desconectado
                break
            elif incoming_buffer.startswith('artifacts:'):
                artifacts = incoming_buffer.split(':')[1].strip()  # Obtener los artefactos enviados por el cliente
                self.associate_artifacts(client_address, artifacts)  # Asociar los artefactos al cliente
            else:
                self.last_received_message = incoming_buffer
                self.broadcast_to_all_clients(so)
        so.close()

    def broadcast_to_all_clients(self, senders_socket):
        for client in self.clients_list:
            socket, (ip, port) = client
            if socket is not senders_socket:
                socket.sendall(self.last_received_message.encode('utf-8'))

    def receive_messages_in_a_new_thread(self):
        while True:
            client = so, (ip, port) = self.server_socket.accept()
            self.add_to_clients_list(client)
            print('Connected to ', ip, ':', str(port))
            t = threading.Thread(target=self.receive_messages, args=(so,))
            t.start()

    def add_to_clients_list(self, client):
        if client not in self.clients_list:
            self.clients_list.append(client)
            socket, (ip, port) = client
            print(f'[SERVER] Cliente {ip}:{port} conectado.')
            for c in self.clients_list:
                if c is not client:
                    c[0].sendall(f'[SERVER] Cliente {ip}:{port} conectado.\n'.encode('utf-8'))
    
    def remove_client_artifacts(self, client_address):
        if client_address in self.clients_artifacts:
            del self.clients_artifacts[client_address]

    def associate_artifacts(self, client_address, artifacts):
        self.clients_artifacts[client_address] = artifacts.split(',')


if __name__ == "__main__":
    ChatServer()