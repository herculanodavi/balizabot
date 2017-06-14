from modeling.Modeling import Modeling
from control import LineFollower
from control import Park
from modeling import Pose2D
from modeling import Vector2
from communication import SendData
from decision_making import DecisionMaking
from time import sleep

DEBUG = False
FORWARD = 1
BACKWARD = -1

model = Modeling()
park = Park()
control = LineFollower.LineFollower()
decision_making = DecisionMaking.DecisionMaking()
communication = SendData.SendData()
# VAI PEGAR AS LINHAS SIM
model.init()
model.init()
model.init()
model.init()
model.init()
model.init()
model.init()

sleep(10)
chegou = False

while(!chegou):
    model.update()
    decision_making.update(model)
    if DEBUG is True:
        print 'extern line_ref = (%d, %d)' % (decision_making.line_ref.x, decision_making.line_ref.y)
    control.setControlData(model.car, decision_making.desired_position, decision_making.line_ref)

    # dutyMotor1 = control.desiredVelocity()
    # dutyMotor2 = control.desiredVelocity()
    # servoAngle = control.desiredAngle()

    # Condição de parada
    if control.desiredVelocity == 0:
        chegou = True

    direcao1 = FORWARD
    direcao2 = FORWARD

    communication.send(direcao1, direcao2, control.desiredVelocity, control.desiredVelocity, -control.desiredAngle)


# Movimento KeyFrame

movimentos = park.do()

for i in range 0,4,1:
    communication.send(movimentos[i][0], movimentos[i][1], movimentos[i][2], movimentos[i][3], movimentos[i][4])
    sleep(movimentos[i][5])
    # Parando após o movimento
    communication.send(1, 1, 0, 0, 0)
    sleep(0.5)
