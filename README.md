# Movimiento Anti-Inactividad para Ratón en Python

Este script permite simular actividad en la computadora moviendo el cursor del ratón a intervalos regulares. El movimiento abarca un área considerable de la pantalla para imitar la actividad humana y evitar que el sistema detecte inactividad.

## Descripción

Este programa utiliza la biblioteca `pyautogui` para realizar movimientos del ratón en intervalos de tiempo definidos por el usuario. Cada movimiento tiene una posición aleatoria dentro de un rango amplio, cubriendo una parte significativa de la pantalla para parecer más natural. 

Es ideal para situaciones en las que se necesita mantener la computadora activa sin intervención constante, evitando bloqueos automáticos, suspensión, o activación de protectores de pantalla.

## Requisitos

- Python 3
- Biblioteca `pyautogui`

## Instalación

1. Clona el repositorio en tu máquina local o descarga el archivo.

2. Instala la biblioteca `pyautogui` si no la tienes:

    ```bash
    pip install pyautogui
    ```

## Uso

Para ejecutar el programa, abre una terminal en el directorio del script y usa:

```bash
python anti_inactividad.py
```

El ratón se moverá cada 10 segundos (o el intervalo definido en el código) dentro de un rango de 500 píxeles desde su posición actual. Puedes modificar el intervalo de tiempo y el rango de movimiento en el código para adaptarlo a tus necesidades.

## Personalización

- **intervalo**: Cambia el valor del parámetro `intervalo` en la función `movimiento_anti_inactividad()` para modificar el tiempo en segundos entre movimientos.
- **desplazamiento_max**: Ajusta el valor de `desplazamiento_max` para aumentar o reducir la distancia del movimiento en píxeles.

## Advertencia

Este programa está diseñado para uso personal y no se recomienda su uso en entornos donde la actividad simulada esté en contra de las políticas de la organización o del software que se esté utilizando.

## Contribuciones

¡Contribuciones y mejoras son bienvenidas! Si tienes ideas para mejorar este script, siéntete libre de hacer un fork y enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.
