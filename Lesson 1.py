# # %% Lecture 13

# p = [0.2, 0.2, 0.2, 0.2, 0.2]
# world = ["green", "red", "red", "green", "green"]
# Z = "red"
# pHit = 0.6
# pMiss = 0.2


# def sense(p, Z):
#     q = []
#     for i in range(len(p)):
#         hit = Z == world[i]
#         q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
#     return q


# print(sense(p, Z))


# # %% Lecture 14

# p = [0.2, 0.2, 0.2, 0.2, 0.2]
# world = ["green", "red", "red", "green", "green"]
# Z = "red"
# pHit = 0.6
# pMiss = 0.2


# def sense(p, Z):
#     q = []
#     for i in range(len(p)):
#         hit = Z == world[i]
#         q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))

#     q = [x / sum(q) for x in q]
#     return q


# print(sense(p, Z))

# # %% Lecture 16

# p = [0.2, 0.2, 0.2, 0.2, 0.2]
# world = ["green", "red", "red", "green", "green"]
# measurements = ["red", "green"]
# pHit = 0.6
# pMiss = 0.2


# def sense(p, Z):
#     q = []
#     for i in range(len(p)):
#         hit = Z == world[i]
#         q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
#     s = sum(q)
#     for i in range(len(q)):
#         q[i] = q[i] / s
#     return q


# for item in measurements:
#     p = sense(p, item)


# print(p)


# # %% Lesson 19
# # Program a function that returns a new distribution
# # q, shifted to the right by U units. If U=0, q should
# # be the same as p.

# p = [0, 1, 0, 0, 0]
# world = ["green", "red", "red", "green", "green"]
# measurements = ["red", "green"]
# pHit = 0.6
# pMiss = 0.2


# def sense(p, Z):
#     q = []
#     for i in range(len(p)):
#         hit = Z == world[i]
#         q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
#     s = sum(q)
#     for i in range(len(q)):
#         q[i] = q[i] / s
#     return q


# def move(p, U):
#     q = []
#     for i in range(len(p)):
#         q.append(p[(i - U) % len(p)])
#     return q


# print(move(p, 1))


# # %% Lesson 23
# # Modify the move function to accommodate the added
# # probabilities of overshooting or undershooting
# # the intended destination.

# p = [0, 1, 0, 0, 0]
# world = ["green", "red", "red", "green", "green"]
# measurements = ["red", "green"]
# pHit = 0.6
# pMiss = 0.2
# pExact = 0.8
# pOvershoot = 0.1
# pUndershoot = 0.1


# def sense(p, Z):
#     q = []
#     for i in range(len(p)):
#         hit = Z == world[i]
#         q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
#     s = sum(q)
#     for i in range(len(q)):
#         q[i] = q[i] / s
#     return q


# def move(p, U):
#     q = []
#     for i in range(len(p)):
#         s = pExact * p[(i - U) % len(p)]
#         s = s + pOvershoot * p[(i - U - 1) % len(p)]
#         s = s + pUndershoot * p[(i - U + 1) % len(p)]
#         q.append(s)
#     return q


# print(move(p, 1))


# # %% Lesson 25
# # Write code that makes the robot move twice and then prints
# # out the resulting distribution, starting with the initial
# # distribution p = [0, 1, 0, 0, 0]

# p = [0, 1, 0, 0, 0]
# world = ["green", "red", "red", "green", "green"]
# measurements = ["red", "green"]
# pHit = 0.6
# pMiss = 0.2
# pExact = 0.8
# pOvershoot = 0.1
# pUndershoot = 0.1


# def sense(p, Z):
#     q = []
#     for i in range(len(p)):
#         hit = Z == world[i]
#         q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
#     s = sum(q)
#     for i in range(len(q)):
#         q[i] = q[i] / s
#     return q


# def move(p, U):
#     q = []
#     for i in range(len(p)):
#         s = pExact * p[(i - U) % len(p)]
#         s = s + pOvershoot * p[(i - U - 1) % len(p)]
#         s = s + pUndershoot * p[(i - U + 1) % len(p)]
#         q.append(s)
#     return q


# print(move(move(p, 1), 1))

# # %% Lesson 26
# # write code that moves 1000 times and then prints the
# # resulting probability distribution.

# p = [0, 1, 0, 0, 0]
# world = ["green", "red", "red", "green", "green"]
# measurements = ["red", "green"]
# pHit = 0.6
# pMiss = 0.2
# pExact = 0.8
# pOvershoot = 0.1
# pUndershoot = 0.1


# def sense(p, Z):
#     q = []
#     for i in range(len(p)):
#         hit = Z == world[i]
#         q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
#     s = sum(q)
#     for i in range(len(q)):
#         q[i] = q[i] / s
#     return q


# def move(p, U):
#     q = []
#     for i in range(len(p)):
#         s = pExact * p[(i - U) % len(p)]
#         s = s + pOvershoot * p[(i - U - 1) % len(p)]
#         s = s + pUndershoot * p[(i - U + 1) % len(p)]
#         q.append(s)
#     return q


# for i in range(1000):
#     p = move(p, 1)
# print(p)


# %% Localization Problem
# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up


def localize(
    colors: list[str],
    measurements: list[list[str]],
    motions: list[list[int, int]],
    sensor_right: float,
    p_move: float,
):
    sensor_wrong = 1 - sensor_right
    p_stay = 1 - p_move

    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

    def move(p, motion) -> list[list[float]]:
        aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]

        for i in range(len(p)):
            for j in range(len(p[i])):
                aux[i][j] = (
                    p_move
                    * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])]
                ) + (p_stay * p[i][j])

        return aux

    def sense(
        p: list[list[float]],
        colors: list[list[str]],
        measurement: list[float, float],
    ) -> list[list[float]]:
        aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]

        s = 0.0
        for i in range(len(p)):
            for j in range(len(p[i])):
                hit = measurement == colors[i][j]
                aux[i][j] = p[i][j] * (
                    hit * sensor_right + (1 - hit) * sensor_wrong
                )
                s += aux[i][j]

        # Normalize
        for i in range(len(aux)):
            for j in range(len(aux[i])):
                aux[i][j] /= s
        return aux

    # >>> Insert your code here <<<
    for ith_motion in range(len(motions)):
        p = move(p, motions[ith_motion])
        p = sense(p, colors, measurements[ith_motion])

    return p


def show(p):
    rows = [
        "[" + ",".join(map(lambda x: "{0:.5f}".format(x), r)) + "]" for r in p
    ]
    print("[" + ",\n ".join(rows) + "]")


#############################################################
# For the following test case, your output should be
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [
    ["R", "G", "G", "R", "R"],
    ["R", "R", "G", "R", "R"],
    ["R", "R", "G", "G", "R"],
    ["R", "R", "R", "R", "R"],
]
measurements = ["G", "G", "G", "G", "G"]
motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
p = localize(colors, measurements, motions, sensor_right=0.7, p_move=0.8)


show(p)  # displays your answer


# # %% Test
# A = [[0, 1], [2, 3]]

# for i, (y, x) in enumerate(A):
#     print(y, x)

# %%
