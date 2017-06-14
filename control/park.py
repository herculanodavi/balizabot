import math

DEBUG = True
FORWARD = 1
BACKWARD = -1


class Park:
    def __init__(self):
        self.normalSpeed = 25
        self.V_RATIO = 50  # Is not calculated
        self.desiredVelocity = self.normalSpeed
        self.desiredAngle = []

    def do(self):
        # Matriz de movimentos KeyFrame: Movimentos[i] = [direcao1, direcao2, dutyMotor1, dutyMotor2, servoAngle, duracao]
        # Consideração KeyFrame: phi_line aprox 0º, carro aprox na desiredPosition (x e y)

        movimentos = [][]

        # Movimento 1: Movimento devagar para trás
        movimentos[0][0] = BACKWARD
        movimentos[0][1] = BACKWARD
        movimentos[0][2] = self.normalSpeed      # Movimento devagar
        movimentos[0][3] = self.normalSpeed      # Movimento devagar
        movimentos[0][4] = 0
        movimentos[0][5] = 1                     # Duracao movimento

        # Movimento 2: Curva leve para esquerda para trás
        movimentos[1][0] = BACKWARD
        movimentos[1][1] = BACKWARD
        movimentos[1][2] = self.normalSpeed      # Movimento devagar contando com a esterção do volante (RODA DA ESQUERDA)
        movimentos[1][3] = self.normalSpeed + 5  # Movimento devagar contando com a esterção do volante (RODA DA DIREITA)
        movimentos[1][4] = 60    # CONFERIR SE A DIREÇÃO ESTÁ CERTA
        movimentos[1][5] = 1  # Duracao movimento

        # Movimento 3: Movimento devagar para trás (para entrar na vaga)
        movimentos[0][0] = BACKWARD
        movimentos[0][1] = BACKWARD
        movimentos[0][2] = self.normalSpeed  # Movimento devagar
        movimentos[0][3] = self.normalSpeed  # Movimento devagar
        movimentos[0][4] = 0
        movimentos[0][5] = 1  # Duracao movimento

        # Movimento 4: Reverso do movimento 2
        movimentos[1][0] = BACKWARD
        movimentos[1][1] = BACKWARD
        movimentos[1][2] = self.normalSpeed +5  # Movimento devagar contando com a esterção do volante (RODA DA ESQUERDA)
        movimentos[1][3] = self.normalSpeed     # Movimento devagar contando com a esterção do volante (RODA DA DIREITA)
        movimentos[1][4] = - 60  # CONFERIR SE A DIREÇÃO ESTÁ CERTA
        movimentos[1][5] = 1  # Duracao movimento

        return movimentos