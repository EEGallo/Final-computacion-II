# Informe de Diseño de ChatConnect

## Decisión de Diseño: Uso de Sockets

Se utilizan sockets para la comunicación cliente-servidor debido a su eficiencia y facilidad de implementación en aplicaciones de red.

## Decisión de Diseño: Interfaz Gráfica de Usuario (GUI)

Se implementó una interfaz gráfica simple utilizando Tkinter para proporcionar una experiencia de usuario más intuitiva y amigable.

## Justificación del Uso de Hilos

Se emplean hilos de ejecución múltiple para manejar conexiones concurrentes de clientes, asegurando así una comunicación eficiente y sin bloqueos.

## Uso de Mensajería Asincrónica

La aplicación implementa la recepción y envío asincrónico de mensajes para optimizar el rendimiento y mejorar la experiencia de usuario durante la comunicación en tiempo real.

## Decisiones de Seguridad

Actualmente, la aplicación no implementa cifrado de mensajes. Esto podría ser una mejora importante para futuras versiones, garantizando la seguridad y privacidad de las comunicaciones.

