from pixels import wait, onXY, setXY, show
from animations import colorSpectrum

print("\nWelcome to da blinkenlights 2 ")

x = 0
y = 0
c = 0
while y < 8:
    while x < 8:
        onXY(x, y, colorSpectrum(c, 10))
        x = x + 1
        c = (c + 0.01) % 1
        wait(0.1)
    y = y + 1
    x = 0


def reihe(reihe, color):
    l = [(i, j) for i in range(8) for j in range(8) if i + j == reihe and j < 9 and i < 9]
    for led in l:
        setXY(led[0], led[1], color)
    show()


for x in range(15):
    reihe(x, colorSpectrum((x * 0.11) % 1, 10))
    wait(1)
