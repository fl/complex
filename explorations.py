import numpy as np
import matplotlib as plt

RESOLUTION = 99
NITER = 20

real = np.linspace(-2, 2, RESOLUTION)
imag = np.linspace(-2, 2, RESOLUTION)
C = real + 1j*imag[:,None]
Z = 0.*C
Mask = np.ones_like(C, dtype=bool)

for i in range(NITER):
    Mask[2*np.sin(Z) > 2] = False
    Z[Mask] = Z[Mask]**(2)
    Output += Mask
Output = Output / NITER

plt.figure(figsize=(8,8))
plt.imshow(Output, cmap='gray')
