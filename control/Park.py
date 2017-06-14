import math

DEBUG = True
FORWARD = 1
BACKWARD = -1


class Park:
    def __init__(self):
        self.normalSpeed = 20
        self.V_RATIO = 50  # Is not calculated
        self.desiredVelocity = self.normalSpeed
        self.desiredAngle = []

    def do(self):
        # Matriz de movimentos KeyFrame: Movimentos[i] = [direcao1, direcao2, dutyMotor1, dutyMotor2, servoAngle, duracao]
        # Consideracao KeyFrame: phi_line aprox 0, carro aprox na desiredPosition (x e y)

        movimentos = []
        linha = []

        # Movimento 1: Movimento devagar para frente
        linha += [FORWARD]
        linha += [FORWARD]
        linha += [self.normalSpeed]      # Movimento devagar
        linha += [self.normalSpeed]      # Movimento devagar
        linha += [-15]
        linha += [2.2]                     # Duracao movimento
        movimentos.append(linha)
        linha = []

        # Movimento 2: Curva leve para esquerda para tras
        linha += [BACKWARD]
        linha += [BACKWARD]
        linha += [self.normalSpeed + 5]      # Movimento devagar contando com a estercao do volante (RODA DA DIREITA)
        linha += [self.normalSpeed + 10]  # Movimento devagar contando com a estercao do volante (RODA DA DIREITA)
        linha += [90] # CONFERIR SE A DIRECAO ESTA CERTA
        linha += [1.5]  # Duracao movimento
        movimentos.append(linha)
        linha = []

        # # Movimento 3: Movimento devagar para tras (para entrar na vaga)
        # linha += [BACKWARD]
        # linha += [BACKWARD]
        # linha += [self.normalSpeed]  # Movimento devagar
        # linha += [self.normalSpeed]  # Movimento devagar
        # linha += [0]
        # linha += [1]  # Duracao movimento
        # movimentos.append(linha)
        # linha = []

        # Movimento 4: Reverso do movimento 2
        linha += [BACKWARD]
        linha += [BACKWARD]
        linha += [self.normalSpeed + 10]  # Movimento devagar contando com a estercao do volante (RODA DA DIREITA)
        linha += [self.normalSpeed + 5]  # Movimento devagar contando com a estercao do volante (RODA DA DIREITA)
        linha += [-90]  # CONFERIR SE A DIRECAO ESTA CERTA
        linha += [1.5]  # Duracao movimento
        movimentos.append(linha)
        linha = []

        # Movimento 1: Movimento devagar para frente
        linha += [FORWARD]
        linha += [FORWARD]
        linha += [self.normalSpeed]  # Movimento devagar
        linha += [self.normalSpeed]  # Movimento devagar
        linha += [20]
        linha += [2]  # Duracao movimento
        movimentos.append(linha)
        linha = []

        return movimentos