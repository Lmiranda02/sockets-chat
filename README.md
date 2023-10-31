# Chat de Granjerxs

Este proyecto es un chat de mensajería desarrollado en Python que permite a múltiples usuarios comunicarse en tiempo real a través de una red local o de Internet. El chat está diseñado específicamente para la comunidad de Granjerxs, donde los usuarios pueden intercambiar mensajes y experiencias sobre sus granjas virtuales.
Características principales
- Identificadores Únicos: Cada usuario debe tener un identificador único en el chat, lo que se logra utilizando las direcciones IP y puertos únicos de los clientes.
- Mensajes en Tiempo Real: Los mensajes enviados por un usuario son transmitidos instantáneamente a todos los demás participantes en el chat.
- Bienvenida y Despedida: Cuando un usuario se conecta o desconecta, se muestra un mensaje de bienvenida o despedida tanto en el servidor como en el chat del usuario.
- Sistema de Nombres Únicos: El servidor verifica que los nombres de usuario sean únicos y solicita uno nuevo si ya está en uso.
- Fácil de Usar: La interfaz simple y amigable permite a los usuarios conectarse, chatear y desconectarse sin problemas.

# Instrucciones de uso
## Configuración del servidor

- Clone este repositorio en su máquina local.
- Ejecute el servidor utilizando el archivo servidor.py.
- El servidor estará en espera de conexiones entrantes.

# Configuración del cliente

- Clone este repositorio en la máquina del cliente.
- Ejecute el cliente utilizando el archivo cliente.py.
- Ingrese un nombre de usuario único cuando se lo solicite. El servidor utilizará la dirección IP y el puerto del cliente para garantizar la unicidad del nombre.
- ¡Bienvenid@ al chat de Granjerxs! Ahora puedes comenzar a chatear.
- Escriba "salir" para desconectarse del chat.
