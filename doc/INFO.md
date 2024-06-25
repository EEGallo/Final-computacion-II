# Informe de Diseño de ChatConnect


## Uso de asyncio para Manejo de Operaciones de Red

 La aplicación ha sido refactorizada para utilizar asyncio en el manejo de operaciones de red. asyncio permite gestionar eficientemente conexiones concurrentes sin bloqueos, mejorando así la escalabilidad y el rendimiento del servidor.

## Justificación del Uso de Hilos

Se emplean hilos de ejecución múltiple para manejar conexiones concurrentes de clientes, asegurando así una comunicación eficiente y sin bloqueos.

## Uso de Mensajería Asincrónica

Se ha integrado un sistema de recepción y envío de mensajes de manera asincrónica utilizando asyncio. Esto optimiza el rendimiento y la capacidad de respuesta de la aplicación, permitiendo a los usuarios enviar y recibir mensajes en tiempo real sin interrupciones.

# Implementación de Threading para Manejo de Interfaz Gráfica

Se ha integrado threading para manejar la interfaz gráfica de usuario (GUI) en la parte del cliente. Esto asegura que la interfaz sea receptiva y no se bloquee mientras el cliente envía y recibe mensajes a través del servidor. Threading es especialmente útil en este contexto, ya que permite ejecutar tareas simultáneamente, manteniendo separadas las operaciones de red y la interfaz gráfica.


## Decisiones de Seguridad

Actualmente, la aplicación no implementa cifrado de mensajes. Esto podría ser una mejora importante para futuras versiones, garantizando la seguridad y privacidad de las comunicaciones.

