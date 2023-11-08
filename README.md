# Challenge_Wifi

Este challenge comprueba si un dispositivo se encuentra dentro de la red Wifi.

El reto devuelve la dirección 'MAC' del dispositivo objetivo si está en la red y '0000' en caso contrario.

Esto permite el control parental. Por ejemplo, permite saber si el smartphone del padre y los dispositivos del hijo están en la misma red.

## Funcionamiento

Utiliza la biblioteca `getmac`, que puede instalarse con `pip install getmac`.
