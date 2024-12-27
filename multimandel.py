import matplotlib.pyplot as plt
import numpy as np

plt.style.use("default")
plt.set_cmap("magma")

RESOLUTION = 300
ITERATIONS = 16

real = np.linspace(-2.0, 1.0, RESOLUTION)
imag = np.linspace(-2.0, 2.0, RESOLUTION)

def iterate(t, c):
    z = 0 * c
    mask = np.ones_like(c, dtype=bool)
    out = np.zeros_like(c, dtype=int)

    for i in range(ITERATIONS):
        mask[z**(i / ITERATIONS + 0.1) > 2.0] = False
        z[mask] = z[mask]**2 + c[mask]
        c *= np.exp(1j * np.pi / ITERATIONS /2)
        c *= np.exp(2j * t * np.pi)
        c *= 1.1
        out += mask

    out = out / ITERATIONS

    return out

t = np.linspace(0, 1, 20)
for i in range(t.shape[0]):
    c = real + 1j * imag[:, None]
    c *= 0.5

    out = iterate(t[i], c)
    plt.figure(figsize=(5, 5))
    plt.imsave(f"{i:03d}.png", out, cmap="magma")
