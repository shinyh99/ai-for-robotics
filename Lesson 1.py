# %% Lecture 13

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ["green", "red", "red", "green", "green"]
Z = "red"
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = Z == world[i]
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    return q


print(sense(p, Z))


# %% Lecture 14

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ["green", "red", "red", "green", "green"]
Z = "red"
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = Z == world[i]
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))

    q = [x / sum(q) for x in q]
    return q


print(sense(p, Z))

# %% Lecture 16

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ["green", "red", "red", "green", "green"]
measurements = ["red", "green"]
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = Z == world[i]
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


for item in measurements:
    p = sense(p, item)


print(p)


# %% Lesson 19
# Program a function that returns a new distribution
# q, shifted to the right by U units. If U=0, q should
# be the same as p.

p = [0, 1, 0, 0, 0]
world = ["green", "red", "red", "green", "green"]
measurements = ["red", "green"]
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = Z == world[i]
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


def move(p, U):
    q = []
    for i in range(len(p)):
        q.append(p[(i - U) % len(p)])
    return q


print(move(p, 1))


# %% Lesson 23
# Modify the move function to accommodate the added
# probabilities of overshooting or undershooting
# the intended destination.

p = [0, 1, 0, 0, 0]
world = ["green", "red", "red", "green", "green"]
measurements = ["red", "green"]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = Z == world[i]
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i - U) % len(p)]
        s = s + pOvershoot * p[(i - U - 1) % len(p)]
        s = s + pUndershoot * p[(i - U + 1) % len(p)]
        q.append(s)
    return q


print(move(p, 1))


# %% Lesson 25
# Write code that makes the robot move twice and then prints
# out the resulting distribution, starting with the initial
# distribution p = [0, 1, 0, 0, 0]

p = [0, 1, 0, 0, 0]
world = ["green", "red", "red", "green", "green"]
measurements = ["red", "green"]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = Z == world[i]
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i - U) % len(p)]
        s = s + pOvershoot * p[(i - U - 1) % len(p)]
        s = s + pUndershoot * p[(i - U + 1) % len(p)]
        q.append(s)
    return q


print(move(move(p, 1), 1))

# %% Lesson 26
# write code that moves 1000 times and then prints the
# resulting probability distribution.

p = [0, 1, 0, 0, 0]
world = ["green", "red", "red", "green", "green"]
measurements = ["red", "green"]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = Z == world[i]
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i - U) % len(p)]
        s = s + pOvershoot * p[(i - U - 1) % len(p)]
        s = s + pUndershoot * p[(i - U + 1) % len(p)]
        q.append(s)
    return q


for i in range(1000):
    p = move(p, 1)
print(p)
