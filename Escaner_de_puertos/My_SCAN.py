#Israel Cuellar Mendez - 2077688
#Importamos las librerias a utilizar.
import nmap
print("Selecione el tipo de escaneo que desea hacer:" )
print("(1) Escaneo UDP.") 
print("(2) Escaneo completo.") 
print("(3) Detección de sistema operativo.") 
print("(4) Escaneo de red con ping.")
Sel = int(input())
print("Si selecciono la opcion 4 ingrese el rango de de ip en la que desea hacer ping ejemplo 127.0.0.1-100" )
ip = input("Ingrese el host a analizar")
if Sel == 1:
   #Se construye un Portscanner de Nmap
    escaner = nmap.PortScanner()
    #Realizamos un escaneo de tipo UDP utilizando el argumento -sU
    escaner.scan(ip,arguments="-sU")
    #Con un ciclo vamos analizando todos los puertos e imprimiendo los resultados
    for host in escaner.all_hosts():
        print(f"Escaneando host {host}...")
        for port in escaner[host]['udp']:
            state = escaner[host]['udp'][port]['state']
            print(f"El puerto {port} está {state}.")
elif Sel==2:
    #Definimos el rango de todos los puertos
    port_range = "1-65535"
    #Se construye un Portscanner de Nmap
    escaner = nmap.PortScanner()
    #Realizamos un escaneo en el rango de puertos dado 
    escaner.scan(ip,port_range)
    #Mediante un ciclo analizamos los puetos e imprime su estado
    for host in escaner.all_hosts():
        print(f"Escaneando host {host}...")
        for port in escaner[host]['tcp']:
            state = escaner[host]['tcp'][port]['state']
            print(f"El puerto {port} está {state}.")
elif Sel==3:
    #Definimos el rango de todos los puertos
    escaner = nmap.PortScanner()
    #Realizamos un escaneo con el argumento -O
    escaner.scan(ip, arguments="-O")
    #Damos el resultado del sistema operativo encontrado
    print(f"El sistema operativo detectado es: {escaner[ip]['osmatch'][0]['name']}")
elif Sel==4:
    #Definimos el rango de todos los puertos
    escaner = nmap.PortScanner()
    #Realizamos un escaneo con el argumento -sn
    escaner.scan(ip, arguments="-sn")
    #Se imprimen los host activos mendiante un ciclo 
    for host in escaner.all_hosts():
        if escaner[host].state() == "up":
            print(f"Host {host} está activo.")