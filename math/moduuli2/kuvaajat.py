import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.linspace(-np.pi*3, np.pi*3, 256, endpoint=True)
sine = np.sin(x)
cosine = np.cos(x)


ax.plot(x, sine, label='Sine', color='blue', linewidth=1.5)
ax.plot(x, cosine, label='Cosine', color='red', linewidth=1.5)

ax.set_xlabel("Angle (rad)")
ax.set_ylabel("Amplitude")
ax.grid(True)
ax.legend()

plt.show()
