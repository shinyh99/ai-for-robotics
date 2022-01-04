import random
import numpy as np
import matplotlib.pyplot as plt
from multipledispatch import dispatch

# ------------------------------------------------
#
# this is the Robot class
#


class Robot(object):
    def __init__(self, length=20.0):
        """
        Creates robot and initializes location/orientation to 0, 0, 0.
        """
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0
        self.length = length
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.steering_drift = 0.0

    def set(self, x, y, orientation):
        """
        Sets a robot coordinate.
        """
        self.x = x
        self.y = y
        self.orientation = orientation % (2.0 * np.pi)

    def set_noise(self, steering_noise, distance_noise):
        """
        Sets the noise parameters.
        """
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = steering_noise
        self.distance_noise = distance_noise

    def set_steering_drift(self, drift):
        """
        Sets the systematical steering drift parameter
        """
        self.steering_drift = drift

    def move(
        self,
        steering,
        distance,
        tolerance=0.001,
        max_steering_angle=np.pi / 4.0,
    ):
        """
        steering = front wheel steering angle, limited by max_steering_angle
        distance = total distance driven, most be non-negative
        """
        if steering > max_steering_angle:
            steering = max_steering_angle
        if steering < -max_steering_angle:
            steering = -max_steering_angle
        if distance < 0.0:
            distance = 0.0

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise)
        distance2 = random.gauss(distance, self.distance_noise)

        # apply steering drift
        steering2 += self.steering_drift

        # Execute motion
        turn = np.tan(steering2) * distance2 / self.length

        if abs(turn) < tolerance:
            # approximate by straight line motion
            self.x += distance2 * np.cos(self.orientation)
            self.y += distance2 * np.sin(self.orientation)
            self.orientation = (self.orientation + turn) % (2.0 * np.pi)
        else:
            # approximate bicycle model for motion
            radius = distance2 / turn
            cx = self.x - (np.sin(self.orientation) * radius)
            cy = self.y + (np.cos(self.orientation) * radius)
            self.orientation = (self.orientation + turn) % (2.0 * np.pi)
            self.x = cx + (np.sin(self.orientation) * radius)
            self.y = cy - (np.cos(self.orientation) * radius)

    def __repr__(self):
        return "[x=%.5f y=%.5f orient=%.5f]" % (
            self.x,
            self.y,
            self.orientation,
        )


############## ADD / MODIFY CODE BELOW ####################
# ------------------------------------------------------------------------
#
# run - does a single control run
def make_robot() -> Robot:
    robot = Robot()
    robot.set(0.0, 1.0, 0.0)
    robot.set_steering_drift(20.0 / 180.0 * np.pi)
    return robot


SPEED = 1.0
N = 500

# P
@dispatch(object, float)
def run(robot: Robot, tau_p):
    x_trajectory = []
    y_trajectory = []
    # TODO: your code here
    for i in range(N):
        steering = -tau_p * robot.y
        robot.move(steering, SPEED)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)

    return x_trajectory, y_trajectory


# PD
@dispatch(object, float, float)
def run(robot: Robot, tau_p, tau_d):
    x_trajectory = []
    y_trajectory = []
    prev_cte = robot.y
    # TODO: your code here
    for i in range(N):
        steering = -tau_p * robot.y - tau_d * (robot.y - prev_cte)
        prev_cte = robot.y
        robot.move(steering, SPEED)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)

    return x_trajectory, y_trajectory


# PID
@dispatch(object, float, float, float)
def run(robot: Robot, tau_p, tau_d, tau_i):
    x_trajectory = []
    y_trajectory = []
    prev_cte = robot.y
    integral_cte = 0.0
    # TODO: your code here
    for i in range(N):
        integral_cte += robot.y
        steering = (
            -tau_p * robot.y
            - tau_d * (robot.y - prev_cte)
            - tau_i * integral_cte
        )
        prev_cte = robot.y
        robot.move(steering, SPEED)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)

    return x_trajectory, y_trajectory


# Parameter optimization
def twiddle(tol=0.2):
    def run(robot: Robot, params):
        err = 0
        prev_cte = robot.y

        int_cte = 0
        for i in range(2 * N):
            cte = robot.y
            diff_cte = cte - prev_cte
            int_cte += cte
            prev_cte = cte
            steer = (
                -params[0] * cte - params[1] * diff_cte - params[2] * int_cte
            )
            robot.move(steer, SPEED)
            if i >= N:
                err += cte ** 2
        return err / N

    p = [0.0, 0.0, 0.0]
    dp = [1.0, 1.0, 1.0]

    best_err = run(make_robot(), p)
    n = 0
    while sum(dp) > tol:
        for i in range(len(p)):
            p[i] += dp[i]
            err = run(make_robot(), p)

            if err < best_err:
                best_err = err
                dp[i] *= 1.1
            else:
                p[i] -= 2 * dp[i]
                err = run(make_robot(), p)
                if err < best_err:
                    best_error = err
                    dp[i] *= 1.1
                else:
                    p[i] += dp[i]
                    dp[i] *= 0.9

        n += 1
        print("Twiddle #", n, p, " -> ", best_err)
    print(" ")
    return p


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 8))

tau_p = 0.2
tau_d = 3.0
tau_i = 0.004


x_trajectory, y_trajectory = run(make_robot(), tau_p)
n = len(x_trajectory)
ax1.plot(x_trajectory, y_trajectory, "g", label="P controller")
ax1.plot(x_trajectory, np.zeros(n), "r", label="reference")
ax1.set_title("P controller")

robot = Robot()
x_trajectory, y_trajectory = run(make_robot(), tau_p, tau_d)
n = len(x_trajectory)
ax2.plot(x_trajectory, y_trajectory, "g", label="PI controller")
ax2.plot(x_trajectory, np.zeros(n), "r", label="reference")
ax2.set_title("PI controller")

robot = Robot()
x_trajectory, y_trajectory = run(make_robot(), tau_p, tau_d, tau_i)
n = len(x_trajectory)
ax3.plot(x_trajectory, y_trajectory, "g", label="PID controller")
ax3.plot(x_trajectory, np.zeros(n), "r", label="reference")
ax3.set_title("PID controller")

optimized_params = twiddle(0.2)
robot = Robot()
x_trajectory, y_trajectory = run(make_robot(), *optimized_params)
n = len(x_trajectory)
ax4.plot(x_trajectory, y_trajectory, "g", label="PID controller")
ax4.plot(x_trajectory, np.zeros(n), "r", label="reference")
ax4.set_title("PID controller w/ optimized params")
plt.show()
