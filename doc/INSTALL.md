# Instrucciones de Instalación

Para utilizar esta aplicación de sala de chat cliente-servidor, sigue estos pasos:

1. **Clonar el Repositorio**

git clone https://github.com/EEGallo/Final-computacion-II.git

2. **Instalar Dependencias**
Asegúrate de tener Python 3.12.3 instalado en tu sistema.

3. **Configurar y Ejecutar el Servidor**
- Abre una terminal y navega al directorio del servidor:
  ```
  cd Final-computacion-II/python server.py <host> -p <port>
  ```
- Reemplaza `<host>` y `<port>` con la dirección IP y el puerto deseados.

4. **Configurar y Ejecutar el Cliente**
- Abre otra terminal y navega al directorio del cliente:
  ```
  cd Final-computacion-II/python client.py <host> -p <port>
  python main.py <host> -p <port>
  ```
- Reemplaza `<host>` y `<port>` con la dirección IP y el puerto del servidor.

5. **Usar la Aplicación**
- Sigue las instrucciones en la interfaz de usuario para enviar y recibir mensajes.

¡Listo! Ahora puedes disfrutar de la sala de ChatConnect