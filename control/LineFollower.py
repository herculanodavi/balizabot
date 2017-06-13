import math

DEBUG = True


class LineFollower:
    def __init__(self):
        self.normalSpeed = 35
        self.V_RATIO = 50  # Is not calculated
        self.desiredVelocity = self.normalSpeed
        self.desiredAngle = []

    def setControlData(self, car, desired_position, line_ref):
        # if DEBUG is True:
        # print "(%d, %d)" % (line_ref.x, line_ref.y)
        # if (desired_position.x - car.pose.x) * line_ref.x + (desired_position.y - car.pose.y) * line_ref.y < 0:
        #     line_ref.x = -line_ref.x
        #     line_ref.y = -line_ref.y

        rotation = car.pose.rotation
        phi_line = math.atan2(line_ref.y, line_ref.x)  # ref angle
        position_error = math.sqrt((car.pose.x - desired_position.x) * (car.pose.x - desired_position.x) +
                                  (car.pose.y - desired_position.y) * (car.pose.y - desired_position.y))
        line_error = car.pose.y - desired_position.y
        phi_error = (rotation - phi_line) * 180 / math.pi
        # k1, k2, k3 e k4 sao constantes carteadas de controle
        k_line = 0.018
        k_phi = 0.03
        k3 = 1
        k4 = 1
        if math.fabs(desired_position.x - car.pose.x) > 10:
            proportional_error = k_line * line_error + k_phi * phi_error
        else:
            self.desiredAngle = 0
            self.desiredVelocity = 0
            return
        if proportional_error > 1:
            proportional_error = 1
        elif proportional_error < -1:
            proportional_error = -1
        self.desiredAngle = math.asin(proportional_error) * 180.0 / math.pi
        # self.desiredVelocity = self.normalSpeed/(1.0 + k3 * positionError + k4 * phiError)
        if DEBUG is True:
            print "1 %f" % position_error
            print "2: %f" % (line_error*k_line)
            print "3 %f" % (phi_error*k_phi)
            print "4 %f" %(k_line * line_error + k_phi * phi_error)
            print "5 %f" % self.desiredAngle
#
# void LineControl::setControlData(representations::Player &player, modeling::WorldModel &wm,
#                                     Pose2D desiredPosition, Vector2<double> lineRef, double velocity) {
#     if ((desiredPosition.translation.x - player.getPose().translation.x) * lineRef.x +
#         (desiredPosition.translation.y - player.getPose().translation.y) * lineRef.y < 0)
#         lineRef = -lineRef;
#
#     lineRef = normalize(lineRef)
#
#     //double angularVelocity = player.getAngularVelocity();
#     //double robotVelocity = player.getVelocity();
#     double maxVelocity = velocity; // Max velocity reference
#     double rotation = player.getRotation();  //player angle
#     double phiLine = atan2(lineRef.y, lineRef.x);  //ref angle
#     double radius = representations::Player::WHEEL_RADIUS;
#     double distanceWheels = representations::Player::DISTANCE_WHEELS;
#     double wr = 0;
#     double wl = 0;
#     double vratio = V_RATIO;
#     double positionError = sqrt(
#             (player.getPose().translation.x - desiredPosition.translation.x) *
#             (player.getPose().translation.x - desiredPosition.translation.x)
#             + (player.getPose().translation.y - desiredPosition.translation.y) *
#               (player.getPose().translation.y - desiredPosition.translation.y));
#     double lineError = player.getPosition().x * lineRef.y - player.getPosition().y * lineRef.x
#                        + lineRef.x * desiredPosition.translation.y - lineRef.y * desiredPosition.translation.x;
#     double K_PHI = 2 * KSI * W_N;
#     double K_H = W_N / (2 * KSI * maxVelocity);
#     //Saturation
#
#     //Angular error
#     double phiErro = phiLine - rotation;
#
#
#     //Anti wind up
#
#     if (positionError < 0.04) {
#         desiredWheelSpeed.left = 0.0;
#         desiredWheelSpeed.right = 0.0;
#         return;
#     }
#
#     if (rotation > M_PI / 3)
#         rotation = M_PI / 3;
#     if (rotation < -M_PI / 3)
#         rotation = -M_PI / 3;
#     //Change of state
#
#     //Velocity control
#
#     //Do control
#
#     //Integrative
#     if (positionError < 0.15) {
#         maxVelocity = 10;
#         K_H = W_N / (2 * KSI * fabs(maxVelocity));
#     }
#     if (phiErro > M_PI)
#         phiErro -= 2 * M_PI;
#     if (phiErro < -M_PI)
#         phiErro += 2 * M_PI;
#     if (phiErro < -M_PI / 2) {
#         phiErro += M_PI;
#         maxVelocity = -maxVelocity;
#         vratio = -vratio;
#     }
#     if (phiErro > M_PI / 2) {
#         phiErro -= M_PI;
#         maxVelocity = -maxVelocity;
#         vratio = -vratio;
#     }
#     // controle da velocidade  da roda direita
#     wr = maxVelocity + distanceWheels * (K_PHI * (K_H * lineError + phiErro)) / (2 * radius);
#     // controle da velocidade da roda esquerda
#     wl = maxVelocity - distanceWheels * (K_PHI * (K_H * lineError + phiErro)) / (2 * radius);
#     //Stop condition
#
#     //TODO: Change constants instead of multiplying by (M_PI/30);
#     desiredWheelSpeed.left = wl;
#     desiredWheelSpeed.right = wr;
#
# }
#
# }
# }
