import socket
import threading

def recibir_mensajes(client_socket):
    while True:
        mensaje = client_socket.recv(1024).decode()
        print(mensaje)

# Configura el socket del cliente
HOST = '127.0.0.1'
PORT = 8080
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    nombre = input("Ingrese su nombre: ")
    client_socket.send(nombre.encode())
    
    respuesta = client_socket.recv(1024).decode()
    if respuesta == "Nombre aceptado":
        break
    elif respuesta == "El nombre ya está en uso. Intente con otro nombre.":
        print(respuesta)

bienvenida = f"¡Bienvenid@ al chat de Granjerxs, {nombre}!"
print(bienvenida)
print("Comience a chatear (escriba 'salir' para desconectarse).")

# Inicia un hilo para recibir mensajes del servidor
recibir_thread = threading.Thread(target=recibir_mensajes, args=(client_socket,))
recibir_thread.start()

while True:
    mensaje = input()
    if mensaje == "salir":
        break
    client_socket.send(mensaje.encode())

client_socket.close()