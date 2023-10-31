import socket
import threading

# Diccionario para mantener un registro de los nombres de los clientes y sus sockets
clientes = {}

def broadcast_mensaje(mensaje, cliente_socket):
    for nombre_cliente, socket_cliente in clientes.items():
        if socket_cliente != cliente_socket:
            mensaje_con_nombre = f"{nombre_cliente}: {mensaje}"
            socket_cliente.send(mensaje_con_nombre.encode())

def manejar_cliente(cliente_socket):
    cliente_socket.send("NOMBRE".encode())
    nombre_cliente = cliente_socket.recv(1024).decode()
    
    while nombre_cliente in clientes:
        cliente_socket.send("El nombre ya está en uso. Intente con otro nombre.".encode())
        nombre_cliente = cliente_socket.recv(1024).decode()
    
    clientes[nombre_cliente] = cliente_socket
    bienvenida = f"[SERVER] Cliente {nombre_cliente} conectado."
    print(bienvenida)
    broadcast_mensaje(bienvenida, cliente_socket)
    
    # Enviar el mensaje "Nombre aceptado"
    cliente_socket.send("Nombre aceptado".encode())

    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode()
            if not mensaje:
                desconectado = f"[SERVER] Cliente {nombre_cliente} desconectado."
                print(desconectado)
                broadcast_mensaje(desconectado, cliente_socket)
                del clientes[nombre_cliente]
                cliente_socket.close()
                break
            else:
                broadcast_mensaje(mensaje, cliente_socket)
        except ConnectionAbortedError:
            print(f"[SERVER] Cliente {nombre_cliente} desconectado inesperadamente.")
            break

# Configura el socket del servidor
HOST = '127.0.0.1'
PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Esperando clientes...")

while True:
    client_socket, client_addr = server_socket.accept()
    cliente_thread = threading.Thread(target=manejar_cliente, args=(client_socket,))
    cliente_thread.start()
