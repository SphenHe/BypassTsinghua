import random
import numpy as np
import matplotlib.pyplot as plt

data = []
with open("LinearClassifierTrain.dat", 'r') as file:
    for line in file:
        if line.strip():  # Skip empty lines
            parts = line.split()
            x1 = float(parts[0])
            x2 = float(parts[1])
            y = int(parts[2])
            data.append((x1, x2, y))

# y = kx + b

n = 10000

max_epsilon = -100
max_k = -100
max_b = -100

for i in range(n):
    k = random.uniform(0, 10)
    b = random.uniform(-20, 20)
    epsilon = 0
    for x1, x2, y in data:
        if y == 1 and x2 < k * x1 + b:
            epsilon += 1
        elif y == -1 and x2 > k * x1 + b:
            epsilon += 1
    if epsilon > max_epsilon:
        max_epsilon = epsilon
        max_k = k
        max_b = b
print(f"Max epsilon: {max_epsilon}")
print(f"Max k: {max_k}")
print(f"Max b: {max_b}")

data = []
with open("LinearClassifierTest.dat", 'r') as file:
    for line in file:
        if line.strip():  # Skip empty lines
            parts = line.split()
            x1 = float(parts[0])
            x2 = float(parts[1])
            y = int(parts[2])
            data.append((x1, x2, y))

max_epsilon2 = -100
max_k2 = -100
max_b2 = -100

for i in range(n):
    k = random.uniform(0, 10)
    b = random.uniform(-20, 20)
    epsilon = 0
    for x1, x2, y in data:
        if y == 1 and x2 < k * x1 + b:
            epsilon += 1
        elif y == -1 and x2 > k * x1 + b:
            epsilon += 1
    if epsilon > max_epsilon2:
        max_epsilon2 = epsilon
        max_k2 = k
        max_b2 = b

print(f"Max epsilon2: {max_epsilon2}")
print(f"Max k2: {max_k2}")
print(f"Max b2: {max_b2}")

# plot data and line
plt.figure(figsize=(10, 6))
for x1, x2, y in data:
    if y == 1:
        plt.scatter(x1, x2, color='blue', label='Class 1' if 'Class 1' not in plt.gca().get_legend_handles_labels()[1] else "")
    else:
        plt.scatter(x1, x2, color='red', label='Class -1' if 'Class -1' not in plt.gca().get_legend_handles_labels()[1] else "")
x = np.linspace(-10, 10, 100)
y = max_k * x + max_b
plt.plot(x, y, color='green', label='Decision Boundary')
x = np.linspace(-10, 10, 100)
y = max_k2 * x + max_b2
plt.plot(x, y, color='orange', label='Decision Boundary Test')
plt.title('Linear Classifier Decision Boundary')
plt.xlabel('x1')
plt.ylabel('x2')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

