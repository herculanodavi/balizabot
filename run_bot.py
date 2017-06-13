from modeling.Modeling import Modeling
from control import LineFollower
from modeling import Pose2D
from modeling import Vector2
from communication import SendData
from decision_making import DecisionMaking
from time import sleep

DEBUG = False
FORWARD = 1
BACKWARD = -1

model = Modeling()
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

TEST = True

while(1):
    model.update()
    decision_making.update(model)
    if DEBUG is True:
        print 'extern line_ref = (%d, %d)' % (decision_making.line_ref.x, decision_making.line_ref.y)
    control.setControlData(model.car, decision_making.desired_position, decision_making.line_ref)

    # dutyMotor1 = control.desiredVelocity()
    # dutyMotor2 = control.desiredVelocity()
    # servoAngle = control.desiredAngle()
    #
    direcao1 = FORWARD
    direcao2 = FORWARD
    communication.send(direcao1, direcao2, control.desiredVelocity, control.desiredVelocity, -control.desiredAngle)
