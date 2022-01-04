# %%
array = [
    [-4, -3, -2, -1],
    [0, 1, 2, 3],
]
print(array[1][3])
print(len(array), len(array[1]))


# %%
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel("some numbers")
plt.show()

# %%
a = [1, 2, 3]
print(a)
print(*a)
