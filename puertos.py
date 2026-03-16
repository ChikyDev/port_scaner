import socket

def detectar_puertos(host, host_start=1, host_end=5000):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    print(f'Escaneando {host}, puertos {host_start} -- {host_end}')

    abiertos = []

    for puertos in range(host_start , host_end + 1):
        try:
            resultado = sock.connect_ex(host, puertos)
            if resultado == 0:
                abiertos.append(puertos)
        except KeyboardInterrupt:
            print('\n Escaneo interrumpido por el usuario')
        except Exception:
            pass
    sock.close()
    if abiertos:
        print(f'Puertos abiertos: {abiertos}')
    else:
        print('No se encontro ningun puerto abierto')
    
detectar_puertos('192.168.0.0')
        
