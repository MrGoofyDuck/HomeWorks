import numpy as np

kilometers = np.zeros(3, dtype=int)
weights = np.zeros(3, dtype=int)

for i in range(3):
    kilometers[i] = int(input(f"Enter kilometers for box {i + 1}: "))
    weights[i] = int(input(f"Enter weight for box {i + 1}: "))

while np.sum(weights) != 713:
    print("Cargo not found. Try again.")
    kilometers += np.random.randint(-5, 6, size=3)
    print(f"Boxes moved by {kilometers[-3:]} kilometers.")
    kilometers[:3] = [int(input(f"Enter new kilometers for box {i + 1}: ")) for i in range(3)]
    weights[:3] = [int(input(f"Enter new weight for box {i + 1}: ")) for i in range(3)]

print("Cargo found! Martians can continue their journey.")
