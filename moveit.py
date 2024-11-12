import pyautogui
import time
import random

def movimiento_anti_inactividad(intervalo=3, desplazamiento_max=500):

    try:
        # Obtiene el tamaño de la pantalla para limitar el rango de movimiento
        ancho_pantalla, alto_pantalla = pyautogui.size()
        
        while True:
            # Obtén la posición actual del ratón
            x, y = pyautogui.position()
            
            # Calcula una nueva posición aleatoria dentro del rango permitido en la pantalla
            x_nuevo = x + random.randint(-desplazamiento_max, desplazamiento_max)
            y_nuevo = y + random.randint(-desplazamiento_max, desplazamiento_max)
            
            # Limita la posición a los bordes de la pantalla
            x_nuevo = max(0, min(ancho_pantalla - 1, x_nuevo))
            y_nuevo = max(0, min(alto_pantalla - 1, y_nuevo))
            
            # Mueve el ratón a la nueva posición calculada
            pyautogui.moveTo(x_nuevo, y_nuevo, duration=0.5)  # Pequeña duración para suavizar el movimiento
            
            # Espera el tiempo de intervalo antes de repetir
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("Programa terminado por el usuario.")

movimiento_anti_inactividad()
