## Practia 11. Escanér de puertos.

[MY_SCAN](./My_SCAN.py) en este script se despliega un menú en el que usuario puede elegir entre varias opciones, ya sea un escaneo UDP, escaneo de la red mediante ping, hacer detección de sistemas operativo o un escaneo de puertos completo.

[SCAN_PORTV1](./SCAN_PORTV1.py) script que realiza un escaneo de puertos y nos devuelve una lista con los puertos que se encuentran abiertos. El escaneo se lleva a cabo en la dirección IP que debe ser ingresada como primero argumento y se escanean el rango de puertos ingresados en el segundo argumento.

[SCAN_PORTV2](./SCAN_PORTV2.py) script que escanea puertos predeterminados en un rango de IP.

[SCAN_PORTV3](./SCAN_PORTV3.py) este script hace un escaneo de puertos en una IP especificada, lo hace creando un hilo por cada puerto a probar. Es necesario agregar como argumentos la IP y el rango de puertos.