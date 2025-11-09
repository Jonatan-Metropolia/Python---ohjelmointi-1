import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.linspace(-np.pi*3, np.pi*3, 300, endpoint=True)
sine = np.sin(x)
cosine = np.cos(x)

ax.plot(x, sine, label='sin', color='blue', linewidth=1.5)
ax.plot(x, cosine, label='cos', color='red', linewidth=1.5)

ax.set_title('Sine and Cosine waves')
ax.set_xlabel('Angle (rad')
ax.set_ylabel('Amplitude')

ax.legend()
ax.grid()

ticks = np.arange(-3*np.pi, 3.5*np.pi, np.pi/2)
labels = []
for t in ticks:
    n = t / (np.pi/2)
    if n == 0:
        label = r"$0$"
    elif n % 2 == 0:  # π, 2π, 3π...
        label = rf"${int(n/2)}\pi$" if abs(n) > 2 else (r"$-\pi$" if n == -2 else (r"$\pi$" if n == 2 else rf"${int(n/2)}\pi$"))
    else:  # π/2, 3π/2, ...
        sign = "-" if n < 0 else ""
        val = abs(int(n))
        label = rf"${sign}\frac{{{val}\pi}}{{2}}$" if val != 1 else rf"${sign}\frac{{\pi}}{{2}}$"
    labels.append(label)

ax.set_xticks(ticks)
ax.set_xticklabels(labels)

plt.show()