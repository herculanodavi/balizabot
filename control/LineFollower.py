import math

DEBUG = True

class LineFollower:
    def __init__(self):
        self.normalSpeed = 25
        self.V_RATIO = 50  # Is not calculated
        self.desiredVelocity = self.normalSpeed
        self.desiredAngle = []

        

    def normalize(self, vector):
        magnitude = math.sqrt(vector.x ** 2 + vector.y ** 2)
        if magnitude == 0:
            return
        [vector.x, vector.y] = [vector.x/magnitude, vector.y/magnitude]
        return vector

    def setControlData(self, car, desired_position, line_ref):
        #if DEBUG is True:
            #print "(%d, %d)" % (line_ref.x, line_ref.y)
        if (desired_position.x - car.pose.x) * line_ref.x + (desired_position.y - car.pose.y) * line_ref.y < 0:
            line_ref.x = -line_ref.x
            line_ref.y = -line_ref.y

        line_ref = self.normalize(line_ref)

        rotation = car.pose.rotation
        phiLine = math.atan2(line_ref.y, line_ref.x)# ref angle
        positionError = math.sqrt((car.pose.x - desired_position.x) * (car.pose.x - desired_position.x) +
                                  (car.pose.y - desired_position.y) * (car.pose.y - desired_position.y))
        lineError = car.pose.x * line_ref.y - car.pose.y * line_ref.x + \
                    line_ref.x * desired_position.y - line_ref.y * desired_position.x
        phiError = phiLine - rotation
        #k1, k2, k3 e k4 sao constantes carteadas de controle
        k1 = 0.002
        k2 = 0.002
        k3 = 1
        k4 = 1
        if math.fabs(positionError) > 10:
            proportionalError = k1 * lineError + k2 * phiError
        else:
            self.desiredAngle = 0
            self.desiredVelocity = 0
            return
        if proportionalError > 1:
            proportionalError = 1
        elif proportionalError <-1:
            proportionalError = -1
        self.desiredAngle = math.asin(proportionalError) * 180.0 / math.pi
        # self.desiredVelocity = self.normalSpeed/(1.0 + k3 * positionError + k4 * phiError)
        if DEBUG is True:
            print "1 %f" % positionError
            print "2 %f" % lineError
            print "3 %f" % phiError
            print "4 %f" %(k1 * lineError + k2 * phiError)
            print "5 %f" % self.desiredAngle







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
