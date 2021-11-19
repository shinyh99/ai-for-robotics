# %% Quiz 7
import math

mu = 10
sigma = 2
x = 8

print(
    1
    / math.sqrt(2 * math.pi * sigma ** 2)
    * math.exp(-1 / 2 * (x - mu) ** 2 / sigma ** 2)
)

# %% Quiz 8
from math import *


def f(mu, sigma2, x):
    return 1 / sqrt(2 * pi * sigma2) * exp(-0.5 * (x - mu) ** 2 / sigma2)


print(f(10, 4, 10))

# %% Quiz 13
mu = 10
nu = 13

sigma2 = 2
rigma2 = 2

mu_new = 1 / (sigma2 + rigma2) * (rigma2 * mu + sigma2 * nu)
sigma2_new = 1 / (1 / sigma2 + 1 / rigma2)

print(mu_new)
print(sigma2_new)

# %% Quiz 17

# Kalman Filter Measurement Update
def update(
    mean1: float, var1: float, mean2: float, var2: float
) -> list[float, float]:
    new_mean = 1 / (var1 + var2) * (var2 * mean1 + var1 * mean2)
    new_var = 1 / (1 / var1 + 1 / var2)
    return [new_mean, new_var]


# Kalman Filter Motion Update
def predict(
    mean1: float, var1: float, mean2: float, var2: float
) -> list[float, float]:
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]


mu = 0
sig = 10000

# Measurement
measurement_sig = 4
measurements = [5, 6, 7, 9, 10]

# Motion
motion_sig = 2
motion = [1, 1, 2, 1, 1]

for i in range(len(measurements)):
    mu, sig = update(mu, sig, measurements[i], measurement_sig)
    print(f"update:     {mu}, {sig}")
    mu, sig = predict(mu, sig, motion[i], motion_sig)
    print(f"predict:    {mu}, {sig}")

print(mu, sig)
