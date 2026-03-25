
import math
import time
import sys

# Configurações do círculo
RAIO_X = 14    # Largura
RAIO_Y = 7     # Altura
CENTRO_X = 18  # Centro horizontal
CENTRO_Y = 9   # Centro vertical

def animar_circulo():
    angulo = 0
    # Limpa a tela uma vez no início
    print("\033[2J", end="")

    try:
        while True:
            # 1. Calcular a posição usando coordenadas polares
            # x = r * cos(theta), y = r * sin(theta)
            x = int(CENTRO_X + RAIO_X * math.cos(angulo))
            y = int(CENTRO_Y + RAIO_Y * math.sin(angulo))

            # 2. Mover o cursor para a posição (ANSI: \033[linha;colunaH)
            # Nota: No terminal, Y é linha e X é coluna
            sys.stdout.write(f"\033[{y};{x}H*")
            sys.stdout.flush()

            # 3. Esperar um pouco para criar o efeito de animação
            time.sleep(0.05)

            # 4. Apagar o rastro (opcional: comente para desenhar o círculo fixo)
            sys.stdout.write(f"\033[{y};{x}H ")

            # Incrementar o ângulo
            angulo += 0.1
            if angulo > 2 * math.pi:
                angulo = 0
                
    except KeyboardInterrupt:
        # Move o cursor para baixo ao sair (Ctrl+C)
        print("\033[25;1H\nAnimação encerrada.")

animar_circulo()
