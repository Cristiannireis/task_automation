import pyautogui as positionMouse
import pyautogui as tempoEspera

# tempo de espera para o computador processar

tempoEspera.sleep(1)

# movendo o mouse até a poição iniciar

positionMouse.moveTo(529, 747)

# tempo de espera
tempoEspera.sleep(2)

# Clicando na posição

positionMouse.click(529, 747)

# tempo de espera
tempoEspera.sleep(1)

#Escrevendo a palavra calculadora / calc

positionMouse.typewrite('calc')

# tempo de espera
tempoEspera.sleep(2)


# movendo mouse até o app da calculadora
positionMouse.click(541, 185)


#print(positionMouse.position())