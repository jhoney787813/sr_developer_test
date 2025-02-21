# Sección 1: 

## Parte 1: Preguntas Teóricas (15 minutos)


## 1. Diferencia entre un servidor web y un servidor de aplicaciones

Para entender la diferencia, pensemos en un restaurante:
- **Servidor Web**: Es como el mesero. Su trabajo es recibir las peticiones de los clientes (usuarios en un navegador), llevarlas a la cocina (servidor) y devolver el plato servido (una página web).
- **Servidor de Aplicaciones**: Es la cocina completa, que no solo entrega platos listos (páginas HTML) sino que también hace preparaciones más complejas (procesa lógica de negocio y maneja datos dinámicos).

### Cuándo usar cada uno:
- **Servidor Web **: Cuando solo necesitas servir contenido estático (HTML, imágenes, CSS, JS) o actuar como proxy inverso.
  **Ejemplos:** Nginx, Apache,vite
- **Servidor de Aplicaciones **: Cuando tu aplicación requiere procesamiento de datos, acceso a bases de datos, autenticación.
  **Ejemplos:** Tomcat, JBoss, .NET Core, Node.js)

**Ejemplo práctico:**
Si tenés un blog estático, con HTML y CSS, un servidor web como Nginx es suficiente. Pero si querés un sistema de reservas para un hotel, necesitás un servidor de aplicaciones que maneje lógica de negocio podriamos implementar uno con Spring Boot en Java o .NET Core en C#.

---


## 2. ¿Por qué usar AWS Lambda en lugar de AWS EC2?

AWS Lambda y AWS EC2 son dos formas diferentes de ejecutar código en la nube:
- **AWS EC2 (Elastic Compute Cloud)**: Es como alquilar un apartamento, lo configurás y lo mantenés encendido para lo que necesités.
- **AWS Lambda**: Es como pedir un taxi, solo pagás cuando lo usás. No tenés que preocuparte por mantenimiento ni infraestructura.

### Ejemplo de uso:
Si tenés una aplicación web que necesita un backend corriendo constantemente, EC2 es la opción ideal. Pero si solo necesitás ejecutar código en eventos específicos (como procesar imágenes cuando un usuario las sube), AWS Lambda es mejor porque solo se ejecuta cuando es necesario y reduce costos.

Ejemplo práctico:
- **AWS Lambda**: Un sistema de notificaciones por correo electrónico. Cada vez que un usuario se registra, Lambda envía un correo sin necesidad de un servidor corriendo todo el tiempo.
- **AWS EC2**: Un servidor web para una tienda en línea que está siempre disponible para recibir pedidos.

---

## 3. Diferencia entre SQL y NoSQL

- **SQL (Ej: MySQL, PostgreSQL, SQL Server)**: Usa tablas y relaciones estructuradas. Ideal cuando tenés datos bien organizados, como registros de clientes y pedidos.
- **NoSQL (Ej: MongoDB, Cassandra, Redis)**: No usa tablas tradicionales, sino documentos o claves-valor. Es mejor cuando los datos son más dinámicos y no necesitan una estructura fija.

### ¿Cuándo usar MongoDB en lugar de MySQL?

- **Usar MySQL**: Cuando necesitás transacciones fuertes, como en un banco donde se deben registrar depósitos y retiros de manera precisa.
- **Usar MongoDB**: Cuando manejás datos flexibles y sin una estructura definida, como una red social donde cada usuario puede tener perfiles con información distinta.

Ejemplo práctico:
- **MySQL**: Un sistema de facturación donde cada factura tiene un cliente, productos y precios bien estructurados.
- **MongoDB**: Una aplicación de reseñas de productos, donde cada usuario puede incluir distintos tipos de datos (texto, imágenes, videos, comentarios) sin una estructura fija.


