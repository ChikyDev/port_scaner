# Escáner de Puertos en Python

Un escáner de puertos TCP simple desarrollado en Python utilizando la librería `socket`.

## Descripción

Este proyecto es un escáner de puertos básico que permite analizar un rango de puertos en un host objetivo para detectar cuáles están abiertos.

El script intenta establecer una conexión TCP con cada puerto del rango especificado y muestra aquellos que responden correctamente.

Este proyecto está pensado como práctica para aprender sobre:

- Redes
- Puertos TCP
- Programación con sockets en Python
- Escaneo básico de red

## Características

- Escaneo de un rango configurable de puertos
- Detección de puertos TCP abiertos
- Timeout para evitar conexiones lentas
- Script sencillo y fácil de entender

## Tecnologías utilizadas

- Python
- Librería `socket`

## Uso

1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/python-port-scanner.git
```

2. Entrar en la carpeta del proyecto

```bash
cd python-port-scanner
```

3. Ejecutar el script

```bash
python puertos.py
```

## Ejemplo de salida

```
Escaneando 192.168.0.1 puertos 1 -- 1000
Puertos abiertos: [22, 80, 443]
```

## Cómo funciona

El script intenta conectarse a cada puerto utilizando un socket TCP.

```python
socket.connect_ex((host, port))
```

Si el resultado es `0`, significa que el puerto está abierto.

## Aviso

Este proyecto es únicamente para fines educativos.  
Solo debes escanear sistemas que te pertenezcan o para los que tengas permiso explícito.

## Autor

Proyecto personal de aprendizaje sobre redes y ciberseguridad.
