import matplotlib.pyplot as plt
import numpy as np

RESOLUTION = 500
NITER = 15

real = np.linspace(-2, 2, RESOLUTION)
imag = np.linspace(-2, 2, RESOLUTION)
C = real + 1j*imag[:,None]
Z = 0.*C
Mask = np.ones_like(C, dtype=bool)
Output = np.zeros_like(C, dtype=int)

for i in range(NITER):
    Mask[2*np.sin(Z) > 2] = False
    Z[Mask] = Z[Mask]**5.35 + C[Mask]
    Output += Mask
Output = Output / NITER

plt.figure(figsize=(8,8))
plt.yticks([])
plt.xticks([])
plt.title("Mandelbrot Experimente")
plt.imshow(Output)
plt.show()
